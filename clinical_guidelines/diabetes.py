"""
ADA Standards of Medical Care in Diabetes Management Protocol
Glycemic targets, SGLT2 inhibitor / GLP-1 receptor agonist pathways, and insulin titration rules.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional


@dataclass
class DiabetesEvaluation:
    glycemic_control_status: str
    target_hba1c: str
    recommended_pharmacotherapy: List[str]
    monitoring_frequency: str
    cardiovascular_renal_protection_notes: str
    preventive_care_checklist: List[str]


class DiabetesGuideline:
    """American Diabetes Association (ADA) Clinical Decision Support Engine."""

    @staticmethod
    def evaluate(
        hba1c_percentage: float,
        has_ascvd: bool = False,
        has_heart_failure: bool = False,
        has_ckd: bool = False,
        egfr_ml_min: float = 85.0,
        uacr_mg_g: float = 15.0,  # Urine Albumin-to-Creatinine Ratio
        age: int = 55,
        history_hypoglycemia: bool = False,
    ) -> DiabetesEvaluation:
        """Evaluates glycemic control and organ-protection pharmacotherapy."""

        # Determine target HbA1c
        if age >= 75 or history_hypoglycemia:
            target_a1c = "< 8.0% (Relaxed target to avoid fatal hypoglycemia)"
        elif age < 40 and not has_ascvd and not has_ckd:
            target_a1c = "< 6.5% (Stringent target if achievable without hypoglycemia)"
        else:
            target_a1c = "< 7.0% (Standard adult target)"

        if hba1c_percentage < 5.7:
            status = "NORMOGLYCEMIA"
        elif hba1c_percentage <= 6.4:
            status = "PREDIABETES"
        elif hba1c_percentage <= 7.0:
            status = "WELL_CONTROLLED_DIABETES"
        elif hba1c_percentage <= 8.5:
            status = "MODERATELY_UNCONTROLLED_DIABETES"
        else:
            status = "POORLY_CONTROLLED_DIABETES"

        meds = []
        # First-line baseline: Metformin + Lifestyle
        if egfr_ml_min >= 45.0:
            meds.append("Metformin 1000 mg twice daily (First-line insulin sensitizer)")
        elif egfr_ml_min >= 30.0:
            meds.append("Metformin 500 mg twice daily (Reduced dose for eGFR 30-44)")
        else:
            meds.append("Metformin Contraindicated (eGFR < 30 mL/min)")

        # Cardiorenal Protection Add-ons independent of baseline HbA1c
        cardio_notes = []
        if has_ascvd:
            meds.append("GLP-1 Receptor Agonist with proven CVD benefit (Semaglutide or Dulaglutide) OR SGLT2i (Empagliflozin)")
            cardio_notes.append("Proven MACE reduction in established ASCVD.")

        if has_heart_failure:
            meds.append("SGLT2 Inhibitor with proven HF benefit (Dapagliflozin 10mg or Empagliflozin 10mg daily)")
            cardio_notes.append("Reduces HF hospitalization and cardiovascular mortality.")

        if has_ckd or uacr_mg_g >= 30.0:
            meds.append("SGLT2 Inhibitor (Dapagliflozin/Empagliflozin) + Non-steroidal MRA (Finerenone) if eGFR >= 25 & K+ normal")
            cardio_notes.append("Slows CKD progression and reduces cardiovascular events.")

        if hba1c_percentage >= 10.0:
            meds.append("Basal Insulin (Glargine or Degludec 10 units / 0.1-0.2 units/kg subcutaneously at bedtime)")

        preventive = [
            "Annual Dilated Eye Examination for Diabetic Retinopathy screening.",
            "Annual Comprehensive Diabetic Foot Exam with 10g monofilament & pulses.",
            "Annual Urine Albumin-to-Creatinine Ratio (uACR) & eGFR testing.",
            "Influenza, Pneumococcal, RSV, and Hepatitis B Vaccinations.",
            "Continuous Glucose Monitoring (CGM) or regular Self-Monitoring of Blood Glucose (SMBG).",
        ]

        freq = "Every 3 months until target met, then every 6 months."

        return DiabetesEvaluation(
            glycemic_control_status=status,
            target_hba1c=target_a1c,
            recommended_pharmacotherapy=meds,
            monitoring_frequency=freq,
            cardiovascular_renal_protection_notes="; ".join(cardio_notes) if cardio_notes else "Standard glycemic targets apply.",
            preventive_care_checklist=preventive,
        )
