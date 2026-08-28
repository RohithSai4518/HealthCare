"""
Unit Tests for HealthSphere Laboratory Information System (LIS) Subsystem
"""

import unittest
from core.enums import AbnormalityFlag, Gender, LabOrderStatus, LabTestCategory
from domain.laboratory import ReferenceRange
from repositories.memory_repo import (
    DoctorRepository,
    LabOrderRepository,
    LabTestTypeRepository,
    PatientRepository,
)
from services.appointment_service import AppointmentService
from services.lab_service import LabService
from services.patient_service import PatientService


class TestLabService(unittest.TestCase):

    def setUp(self):
        self.order_repo = LabOrderRepository()
        self.type_repo = LabTestTypeRepository()
        self.patient_repo = PatientRepository()
        self.doctor_repo = DoctorRepository()

        self.patient_service = PatientService(self.patient_repo)
        self.appointment_service = AppointmentService(
            None, self.doctor_repo, self.patient_repo
        )
        self.lab_service = LabService(
            self.order_repo, self.type_repo, self.patient_repo, self.doctor_repo
        )

        self.patient = self.patient_service.register_patient(
            first_name="Bruce", last_name="Banner", date_of_birth="1969-12-18", gender=Gender.MALE
        )
        self.doctor = self.appointment_service.register_doctor(
            license_number="LIC-MD-5566", first_name="Stephen", last_name="Strange"
        )

    def test_reference_range_evaluations(self):
        ref = ReferenceRange(
            low_value=13.5,
            high_value=17.5,
            unit_of_measure="g/dL",
            critical_low=7.0,
            critical_high=20.0,
        )
        self.assertEqual(ref.evaluate(15.0), AbnormalityFlag.NORMAL)
        self.assertEqual(ref.evaluate(12.0), AbnormalityFlag.LOW)
        self.assertEqual(ref.evaluate(18.5), AbnormalityFlag.HIGH)
        self.assertEqual(ref.evaluate(6.5), AbnormalityFlag.CRITICAL_LOW)
        self.assertEqual(ref.evaluate(21.0), AbnormalityFlag.CRITICAL_HIGH)

    def test_lab_order_workflow_and_critical_flag(self):
        glucose_test = self.type_repo.get_by_code("LOINC-2345-7")
        self.assertIsNotNone(glucose_test)

        # 1. Order test
        order = self.lab_service.order_lab_tests(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            test_type_ids=[glucose_test.id],
            clinical_indication="Suspected diabetic ketoacidosis",
        )
        self.assertEqual(order.status, LabOrderStatus.ORDERED)

        # 2. Collect specimen
        self.lab_service.collect_specimen(
            order_id=order.id, technician_id="TECH-002", barcode="SPM-GLU-990"
        )
        self.assertEqual(order.status, LabOrderStatus.SAMPLE_COLLECTED)

        # 3. Submit critical high result (450 mg/dL > critical 400)
        self.lab_service.submit_results(
            order_id=order.id,
            measurements=[{"test_type_id": glucose_test.id, "value": 450.0}],
            technician_notes="Panic value confirmed by repeat assay.",
        )
        self.assertEqual(order.status, LabOrderStatus.COMPLETED)
        self.assertTrue(order.has_critical_values)
        self.assertEqual(order.results[0].flag, AbnormalityFlag.CRITICAL_HIGH)


if __name__ == "__main__":
    unittest.main()
