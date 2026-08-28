"""
Unit Tests for HealthSphere Massive Knowledge Bases, Catalogs, and Clinical Calculators
"""

import unittest
from knowledge_base.icd10_full_master import FullICD10MasterRegistry
from knowledge_base.cpt_full_master import FullCPTMasterRegistry
from cdss.full_clinical_calculators import ComprehensiveClinicalCalculators


class TestMassiveCatalogs(unittest.TestCase):

    def test_icd10_registry_population(self):
        count = FullICD10MasterRegistry.count()
        self.assertTrue(count >= 800, f"Expected >= 800 ICD-10 entries, found {count}")

    def test_cpt_registry_population(self):
        count = FullCPTMasterRegistry.count()
        self.assertTrue(count >= 800, f"Expected >= 800 CPT entries, found {count}")

    def test_meld_na_score_calculation(self):
        res = ComprehensiveClinicalCalculators.calculate_meld_na(
            serum_bilirubin_mg_dl=2.5,
            serum_creatinine_mg_dl=1.8,
            inr=1.9,
            serum_sodium_mmol_l=130.0,
        )
        self.assertTrue(6 <= res["meld_na_score"] <= 40)
        self.assertIn("estimated_90_day_mortality_percent", res)

    def test_wells_pe_score(self):
        res = ComprehensiveClinicalCalculators.calculate_wells_pe_score(
            clinical_signs_dvt=True,
            pe_number_one_diagnosis=True,
            heart_rate_over_100=True,
            immobilization_or_surgery_past_4_weeks=False,
            previous_dvt_or_pe=False,
            hemoptysis=False,
            malignancy_active=False,
        )
        self.assertEqual(res["wells_score"], 7.5)
        self.assertTrue(res["pe_clinically_likely"])


if __name__ == "__main__":
    unittest.main()
