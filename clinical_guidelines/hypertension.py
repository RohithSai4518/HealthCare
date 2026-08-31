"""
AHA/ACC and JNC8 Evidence-Based Hypertension Management Protocol
Stepped-care pharmacological titration algorithms and lifestyle intervention logic.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional


@dataclass
class HypertensionEvaluation:
    bp_stage: str
    target_blood_pressure: str
    recommended_first_line_agents: List[str]
    combination_therapy_required: bool
    lifestyle_recommendations: List[str]
    follow_up_interval_weeks: int
    clinical_notes: str


class HypertensionGuideline:
    """AHA/ACC 2017 & JNC8 Hypertension Clinical Decision Support Protocol."""

    @staticmethod
    def evaluate(
        systolic_bp: int,
        diastolic_bp: int,
        has_diabetes: bool = False,
        has_ckd: bool = False,
        is_black_ethnicity: bool = False,
        age: int = 50,
        has_ascvd: bool = False,
        has_hfref: bool = False,
    ) -> HypertensionEvaluation:
        """Evaluates patient blood pressure against ACC/AHA and JNC8 clinical practice guidelines."""

        # 1. Determine Blood Pressure Category (ACC/AHA 2017)
        if systolic_bp < 120 and diastolic_bp < 80:
            stage = "NORMAL"
            target = "< 120/80 mmHg"
            first_line = []
            combo = False
            fup = 52  # Yearly
            notes = "Reassess blood pressure annually; maintain heart-healthy lifestyle habits."
        elif systolic_bp <= 129 and diastolic_bp < 80:
            stage = "ELEVATED"
            target = "< 120/80 mmHg"
            first_line = []
            combo = False
            fup = 12  # Recheck in 3-6 months
            notes = "Non-pharmacological therapy (DASH diet, sodium restriction < 2300 mg/d, aerobic exercise)."
        elif systolic_bp <= 139 or diastolic_bp <= 89:
            stage = "STAGE_1_HYPERTENSION"
            target = "< 130/80 mmHg"
            
            # If ASCVD or 10-year risk >= 10% or diabetes/CKD -> start monotherapy
            if has_ascvd or has_diabetes or has_ckd or age >= 65:
                if is_black_ethnicity and not has_ckd:
                    first_line = ["Thiazide Diuretic (Chlorthalidone 12.5-25mg/d)", "Dihydropyridine CCB (Amlodipine 5mg/d)"]
                elif has_ckd:
                    first_line = ["ACE Inhibitor (Lisinopril 10-20mg/d)", "ARB (Losartan 50mg/d)"]
                else:
                    first_line = ["ACE Inhibitor", "ARB", "Dihydropyridine CCB", "Thiazide Diuretic"]
                combo = False
                fup = 4
                notes = "Initiate single first-line antihypertensive agent; reassess in 1 month."
            else:
                first_line = []
                combo = False
                fup = 12
                notes = "6-month trial of rigorous lifestyle modification before starting pharmacotherapy."
        else:
            stage = "STAGE_2_HYPERTENSION"
            target = "< 130/80 mmHg"
            combo = True
            fup = 4

            if is_black_ethnicity and not has_ckd:
                first_line = [
                    "Thiazide Diuretic (Chlorthalidone 25mg) + Dihydropyridine CCB (Amlodipine 5mg)",
                    "ARB (Losartan 50mg) + Dihydropyridine CCB (Amlodipine 5mg)",
                ]
            elif has_ckd:
                first_line = [
                    "ACE Inhibitor (Lisinopril 20mg) + Dihydropyridine CCB (Amlodipine 5mg)",
                    "ARB (Losartan 50mg) + Thiazide Diuretic (Chlorthalidone 12.5mg)",
                ]
            elif has_hfref:
                first_line = [
                    "ARNI (Sacubitril/Valsartan) or ACEI/ARB + Beta-Blocker (Metoprolol Succinate/Carvedilol) + MRA (Spironolactone)",
                ]
            else:
                first_line = [
                    "ACE Inhibitor (Lisinopril 20mg) + Dihydropyridine CCB (Amlodipine 5mg)",
                    "ARB (Losartan 50mg) + Thiazide Diuretic (Chlorthalidone 12.5mg)",
                ]
            notes = "Prompt initiation of 2 first-line agents of different classes (dual therapy). Monthly titration until controlled."

        lifestyle = [
            "DASH Dietary Pattern: Rich in fruits, vegetables, whole grains, low-fat dairy.",
            "Dietary Sodium Reduction: Optimal target < 1500 mg/day (minimum < 2300 mg/day).",
            "Physical Activity: 90-150 min/week of moderate-to-vigorous aerobic exercise.",
            "Weight Reduction: Aim for BMI 18.5 - 24.9 kg/m2 (expect ~1 mmHg SBP drop per kg lost).",
            "Alcohol Moderation: <= 2 drinks/day for men, <= 1 drink/day for women.",
        ]

        return HypertensionEvaluation(
            bp_stage=stage,
            target_blood_pressure=target,
            recommended_first_line_agents=first_line,
            combination_therapy_required=combo,
            lifestyle_recommendations=lifestyle,
            follow_up_interval_weeks=fup,
            clinical_notes=notes,
        )
