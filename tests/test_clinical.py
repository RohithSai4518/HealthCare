"""
Unit Tests for HealthSphere Clinical EHR & Vitals Subsystem
"""

import unittest
from core.enums import EncounterStatus, EncounterType, Gender
from domain.clinical import Vitals
from repositories.memory_repo import (
    AppointmentRepository,
    DoctorRepository,
    EncounterRepository,
    PatientRepository,
)
from services.appointment_service import AppointmentService
from services.clinical_service import ClinicalService
from services.patient_service import PatientService


class TestClinicalService(unittest.TestCase):

    def setUp(self):
        self.patient_repo = PatientRepository()
        self.doctor_repo = DoctorRepository()
        self.encounter_repo = EncounterRepository()
        self.appointment_repo = AppointmentRepository()

        self.patient_service = PatientService(self.patient_repo)
        self.appointment_service = AppointmentService(
            self.appointment_repo, self.doctor_repo, self.patient_repo
        )
        self.clinical_service = ClinicalService(
            self.encounter_repo, self.patient_repo, self.doctor_repo, self.appointment_repo
        )

        self.patient = self.patient_service.register_patient(
            first_name="Marcus", last_name="Aurelius", date_of_birth="1975-04-26", gender=Gender.MALE
        )
        self.doctor = self.appointment_service.register_doctor(
            license_number="LIC-MD-10101",
            first_name="Galen",
            last_name="Pergamon",
            specialty="Internal Medicine",
        )

    def test_vitals_calculations(self):
        v = Vitals(
            systolic_bp=135,
            diastolic_bp=88,
            heart_rate_bpm=72,
            respiratory_rate=16,
            temperature_celsius=38.5,
            spo2_percentage=94.0,
            height_cm=180.0,
            weight_kg=81.0,
        )
        # BMI = 81 / (1.8^2) = 81 / 3.24 = 25.0
        self.assertEqual(v.bmi, 25.0)
        self.assertEqual(v.bp_category, "STAGE_1_HYPERTENSION")
        self.assertTrue(v.is_feverish)
        self.assertTrue(v.is_hypoxic)

    def test_encounter_workflow(self):
        # 1. Start encounter
        encounter = self.clinical_service.start_encounter(
            patient_id=self.patient.id,
            attending_doctor_id=self.doctor.id,
            encounter_type=EncounterType.OUTPATIENT,
            chief_complaint="Chest congestion and cough",
        )
        self.assertEqual(encounter.status, EncounterStatus.IN_PROGRESS)

        # 2. Attach vitals
        vitals = self.clinical_service.record_vitals(
            encounter_id=encounter.id,
            systolic_bp=120,
            diastolic_bp=80,
            heart_rate_bpm=76,
            respiratory_rate=16,
            temperature_celsius=37.1,
            spo2_percentage=98.0,
            height_cm=175.0,
            weight_kg=70.0,
        )
        self.assertIsNotNone(encounter.vitals)

        # 3. Add diagnosis & SOAP Note
        self.clinical_service.add_diagnosis(
            encounter_id=encounter.id,
            icd10_code="J20.9",
            description="Acute bronchitis, unspecified",
            is_primary=True,
        )
        soap = self.clinical_service.document_soap_note(
            encounter_id=encounter.id,
            subjective="Productive cough for 5 days.",
            objective="Bilateral rhonchi on auscultation.",
            assessment="Acute infectious bronchitis.",
            plan="Prescribe supportive bronchodilator and fluids.",
            author_doctor_id=self.doctor.id,
        )
        self.assertIsNotNone(encounter.clinical_note)
        self.assertEqual(len(encounter.diagnoses), 1)

        # 4. Discharge encounter
        closed = self.clinical_service.complete_encounter(
            encounter.id, "Discharged with home care plan."
        )
        self.assertEqual(closed.status, EncounterStatus.DISCHARGED)


if __name__ == "__main__":
    unittest.main()
