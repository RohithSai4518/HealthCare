"""
Unit Tests for Clinical Decision Support System (CDSS) Engines
"""

import unittest
from cdss.cardiology import CardiologyCalculators
from cdss.nephrology import NephrologyCalculators
from cdss.critical_care import CriticalCareCalculators


class TestCDSSCalculators(unittest.TestCase):

    def test_cha2ds2_vasc(self):
        res = CardiologyCalculators.calculate_cha2ds2_vasc(
            age=76,  # +2
            is_female=True,  # +1
            congestive_heart_failure=True,  # +1
            hypertension=True,  # +1
            stroke_or_tia_history=False,
            vascular_disease=False,
            diabetes=True,  # +1
        )
        self.assertEqual(res["score"], 6)
        self.assertEqual(res["risk_category"], "HIGH")

    def test_ckd_epi_2021(self):
        res = NephrologyCalculators.calculate_ckd_epi_2021(
            serum_creatinine_mg_dl=1.1,
            age=55,
            is_female=False,
        )
        self.assertTrue(res["egfr_ml_min_1_73m2"] > 0)
        self.assertIn(res["kdigo_stage"], ["G1", "G2", "G3a", "G3b", "G4", "G5"])

    def test_qsofa_high_risk(self):
        res = CriticalCareCalculators.calculate_qsofa(
            respiratory_rate=24,  # +1
            altered_mental_status=True,  # +1
            systolic_bp=95,  # +1
        )
        self.assertEqual(res["qsofa_score"], 3)
        self.assertTrue(res["high_risk_sepsis_mortality"])


if __name__ == "__main__":
    unittest.main()
