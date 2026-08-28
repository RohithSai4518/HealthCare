"""
Unit Tests for Extended Clinical Guidelines, Interaction Matrix, and 12-Lead ECG Engine
"""

import unittest
from clinical_guidelines.hypertension import HypertensionGuideline
from clinical_guidelines.diabetes import DiabetesGuideline
from clinical_guidelines.heart_failure import HeartFailureGuideline
from knowledge_base.expanded_interactions_full import FullInteractionMasterMatrix
from knowledge_base.expanded_lab_catalog_full import FullLabMasterCatalog
from telemetry.multi_lead_ecg_engine import TwelveLeadECGEngine


class TestExtendedClinicalSuites(unittest.TestCase):

    def test_hypertension_stage_2_guideline(self):
        eval_res = HypertensionGuideline.evaluate(
            systolic_bp=150,
            diastolic_bp=95,
            has_diabetes=True,
            has_ckd=False,
        )
        self.assertEqual(eval_res.bp_stage, "STAGE_2_HYPERTENSION")
        self.assertTrue(eval_res.combination_therapy_required)
        self.assertEqual(eval_res.follow_up_interval_weeks, 4)

    def test_diabetes_ada_guideline(self):
        eval_res = DiabetesGuideline.evaluate(
            hba1c_percentage=9.2,
            has_ascvd=True,
            has_heart_failure=True,
            egfr_ml_min=55.0,
        )
        self.assertEqual(eval_res.glycemic_control_status, "POORLY_CONTROLLED_DIABETES")
        self.assertTrue(len(eval_res.recommended_pharmacotherapy) >= 2)

    def test_heart_failure_hfref_guideline(self):
        eval_res = HeartFailureGuideline.evaluate(
            lvef_percent=32,
            nyha_class=3,
            systolic_bp=115,
            serum_potassium_mmol_l=4.4,
            egfr_ml_min=65.0,
            has_volume_overload=True,
        )
        self.assertIn("HFrEF", eval_res.hf_category)
        self.assertEqual(len(eval_res.gdmt_four_pillars), 4)

    def test_full_interaction_matrix_count(self):
        count = FullInteractionMasterMatrix.count()
        self.assertTrue(count >= 500, f"Expected >= 500 interaction rules, found {count}")

    def test_full_lab_catalog_count(self):
        count = FullLabMasterCatalog.count()
        self.assertTrue(count >= 300, f"Expected >= 300 lab assays, found {count}")

    def test_12_lead_ecg_synthesis(self):
        leads = TwelveLeadECGEngine.synthesize_12_leads(
            heart_rate_bpm=80, duration_seconds=1.0, sampling_rate_hz=100
        )
        self.assertEqual(len(leads), 12)
        self.assertIn("II", leads)
        self.assertIn("V1", leads)
        self.assertEqual(len(leads["II"]), 100)


if __name__ == "__main__":
    unittest.main()
