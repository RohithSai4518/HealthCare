"""
Unit Tests for HealthSphere Patient Management Subsystem
"""

import unittest
from core.enums import AllergyCategory, AllergySeverity, BloodGroup, Gender, MaritalStatus
from core.exceptions import EntityNotFoundError, ValidationError
from domain.models import Address, ContactInfo, InsurancePolicy
from domain.patient import Allergy, EmergencyContact, MedicalHistoryRecord
from repositories.memory_repo import PatientRepository
from services.patient_service import PatientService


class TestPatientService(unittest.TestCase):

    def setUp(self):
        self.patient_repo = PatientRepository()
        self.patient_service = PatientService(self.patient_repo)

    def test_patient_registration_success(self):
        patient = self.patient_service.register_patient(
            first_name="Jane",
            last_name="Doe",
            date_of_birth="1988-04-15",
            gender=Gender.FEMALE,
            blood_group=BloodGroup.A_POSITIVE,
            marital_status=MaritalStatus.MARRIED,
            address=Address("123 Health Ave", "Metropolis", "CA", "90210"),
            contact=ContactInfo(phone_primary="555-0199", email="jane.doe@example.org"),
        )
        self.assertIsNotNone(patient.id)
        self.assertTrue(patient.mrn.startswith("MRN-"))
        self.assertEqual(patient.full_name, "Jane Doe")
        self.assertEqual(patient.blood_group, BloodGroup.A_POSITIVE)
        self.assertEqual(self.patient_repo.count(), 1)

    def test_patient_registration_validation_failure(self):
        with self.assertRaises(ValidationError):
            self.patient_service.register_patient(
                first_name="",
                last_name="Doe",
                date_of_birth="1988-04-15",
                gender=Gender.FEMALE,
            )

    def test_search_and_retrieval(self):
        p1 = self.patient_service.register_patient(
            first_name="Alice", last_name="Walker", date_of_birth="1990-01-01", gender=Gender.FEMALE
        )
        p2 = self.patient_service.register_patient(
            first_name="Bob", last_name="Smith", date_of_birth="1985-05-12", gender=Gender.MALE
        )

        results = self.patient_service.search_patients("Walker")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, p1.id)

        by_mrn = self.patient_service.get_patient_by_mrn(p2.mrn)
        self.assertEqual(by_mrn.id, p2.id)

    def test_add_allergy_and_history(self):
        patient = self.patient_service.register_patient(
            first_name="Charlie", last_name="Brown", date_of_birth="1995-10-20", gender=Gender.MALE
        )
        allergy = Allergy(
            allergen="Penicillin",
            category=AllergyCategory.MEDICATION,
            severity=AllergySeverity.SEVERE,
            reaction_symptoms="Anaphylaxis risk",
        )
        self.patient_service.add_patient_allergy(patient.id, allergy)

        updated_patient = self.patient_service.get_patient_by_id(patient.id)
        self.assertEqual(len(updated_patient.allergies), 1)
        self.assertEqual(updated_patient.allergies[0].allergen, "Penicillin")

        history = MedicalHistoryRecord(
            condition_or_procedure="Tonsillectomy",
            diagnosed_or_performed_date="2010-06-15",
        )
        self.patient_service.add_medical_history(patient.id, history)
        self.assertEqual(len(updated_patient.medical_history), 1)


if __name__ == "__main__":
    unittest.main()
