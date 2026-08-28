"""
Unit Tests for Synthetic Data Generator and HL7 FHIR R4 Serializer
"""

import json
import unittest
from api.server import HealthSphereAppContext
from generators.fhir_exporter import FHIRExporter
from generators.synthetic_data import SyntheticDataGenerator


class TestSyntheticDataAndFHIR(unittest.TestCase):

    def setUp(self):
        self.context = HealthSphereAppContext()
        self.generator = SyntheticDataGenerator(
            self.context.patient_service,
            self.context.appointment_service,
            self.context.clinical_service,
            self.context.pharmacy_service,
            self.context.lab_service,
            self.context.billing_service,
        )

    def test_synthetic_data_generation_full_cycle(self):
        patients = self.generator.seed_synthetic_patients_and_scenarios(
            patient_count=3, generate_encounters=True
        )
        self.assertEqual(len(patients), 3)
        self.assertTrue(self.context.patient_repo.count() >= 3)
        self.assertTrue(self.context.encounter_repo.count() >= 3)
        self.assertTrue(self.context.prescription_repo.count() >= 3)
        self.assertTrue(self.context.lab_order_repo.count() >= 3)
        self.assertTrue(self.context.invoice_repo.count() >= 3)

    def test_fhir_bundle_serialization(self):
        patients = self.generator.seed_synthetic_patients_and_scenarios(
            patient_count=1, generate_encounters=True
        )
        p = patients[0]
        encs = self.context.encounter_repo.get_by_patient(p.id)
        labs = self.context.lab_order_repo.get_by_patient(p.id)

        bundle_json_str = FHIRExporter.export_patient_bundle(p, encs, labs)
        bundle_obj = json.loads(bundle_json_str)

        self.assertEqual(bundle_obj["resourceType"], "Bundle")
        self.assertTrue(bundle_obj["total"] >= 1)
        # Check first resource is Patient
        patient_res = bundle_obj["entry"][0]["resource"]
        self.assertEqual(patient_res["resourceType"], "Patient")
        self.assertEqual(patient_res["identifier"][0]["value"], p.mrn)


if __name__ == "__main__":
    unittest.main()
