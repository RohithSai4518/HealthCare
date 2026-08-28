"""
Unit Tests for HealthSphere Pharmacy & Medication Safety Subsystem
"""

import unittest
from core.enums import AllergyCategory, AllergySeverity, DrugForm, Gender, PrescriptionStatus
from core.exceptions import DrugInteractionError, InsufficientStockError
from domain.patient import Allergy
from repositories.memory_repo import (
    DoctorRepository,
    InventoryRepository,
    MedicationRepository,
    PatientRepository,
    PrescriptionRepository,
)
from services.appointment_service import AppointmentService
from services.patient_service import PatientService
from services.pharmacy_service import PharmacyService


class TestPharmacyService(unittest.TestCase):

    def setUp(self):
        self.med_repo = MedicationRepository()
        self.rx_repo = PrescriptionRepository()
        self.inv_repo = InventoryRepository()
        self.patient_repo = PatientRepository()
        self.doctor_repo = DoctorRepository()

        self.patient_service = PatientService(self.patient_repo)
        self.appointment_service = AppointmentService(
            None, self.doctor_repo, self.patient_repo
        )
        self.pharmacy_service = PharmacyService(
            self.med_repo, self.rx_repo, self.inv_repo, self.patient_repo, self.doctor_repo
        )

        self.patient = self.patient_service.register_patient(
            first_name="Arthur", last_name="Dent", date_of_birth="1980-03-11", gender=Gender.MALE
        )
        self.doctor = self.appointment_service.register_doctor(
            license_number="LIC-MD-3344", first_name="Leonard", last_name="McCoy"
        )

        self.aspirin = self.pharmacy_service.register_medication(
            ndc_code="0054-0007-25", generic_name="Aspirin", brand_name="Bayer", unit_price=10.0
        )
        self.warfarin = self.pharmacy_service.register_medication(
            ndc_code="0054-0010-25", generic_name="Warfarin", brand_name="Coumadin", unit_price=20.0
        )
        self.ibuprofen = self.pharmacy_service.register_medication(
            ndc_code="0054-0015-25", generic_name="Ibuprofen", brand_name="Advil", unit_price=8.0
        )

    def test_drug_interaction_detection(self):
        # Warfarin + Aspirin interaction check
        warnings = self.pharmacy_service.check_safety(
            self.patient.id, ["Warfarin", "Aspirin"]
        )
        self.assertTrue(len(warnings) > 0)
        self.assertEqual(warnings[0]["type"], "DRUG_INTERACTION")
        self.assertEqual(warnings[0]["severity"], "MAJOR")

    def test_allergy_contraindication_block(self):
        self.patient.add_allergy(
            Allergy(
                allergen="Aspirin",
                category=AllergyCategory.MEDICATION,
                severity=AllergySeverity.LIFE_THREATENING,
                reaction_symptoms="Severe Bronchospasm",
            )
        )
        self.patient_repo.save(self.patient)

        with self.assertRaises(DrugInteractionError):
            self.pharmacy_service.create_prescription(
                patient_id=self.patient.id,
                doctor_id=self.doctor.id,
                items_data=[{"medication_id": self.aspirin.id, "total_quantity": 10}],
            )

    def test_dispense_and_inventory_decrement(self):
        # Restock inventory
        self.pharmacy_service.restock_inventory(
            medication_id=self.ibuprofen.id,
            batch_number="BAT-1001",
            quantity=50,
            unit_cost=3.0,
        )
        self.assertEqual(self.inv_repo.get_total_stock(self.ibuprofen.id), 50)

        # Create prescription
        rx = self.pharmacy_service.create_prescription(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            items_data=[{"medication_id": self.ibuprofen.id, "total_quantity": 14}],
        )
        self.assertEqual(rx.status, PrescriptionStatus.ACTIVE)

        # Dispense
        dispensed_rx = self.pharmacy_service.dispense_prescription(rx.id, pharmacist_id="PHARM-01")
        self.assertEqual(dispensed_rx.status, PrescriptionStatus.DISPENSED)
        self.assertEqual(self.inv_repo.get_total_stock(self.ibuprofen.id), 36)

    def test_insufficient_stock_error(self):
        rx = self.pharmacy_service.create_prescription(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            items_data=[{"medication_id": self.ibuprofen.id, "total_quantity": 100}],
        )
        with self.assertRaises(InsufficientStockError):
            self.pharmacy_service.dispense_prescription(rx.id, pharmacist_id="PHARM-01")


if __name__ == "__main__":
    unittest.main()
