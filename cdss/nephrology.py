"""
Nephrology & Renal Function Clinical Decision Support Calculators
Implements CKD-EPI 2021 eGFR, Cockcroft-Gault CrCl, and KDIGO Chronic Kidney Disease Staging.
"""

from typing import Dict, Any, List


class NephrologyCalculators:
    """Clinical algorithms for renal clearance and drug dosage adjustments."""

    @staticmethod
    def calculate_ckd_epi_2021(
        serum_creatinine_mg_dl: float,
        age: int,
        is_female: bool,
    ) -> Dict[str, Any]:
        """
        2021 CKD-EPI Creatinine Equation (Race-Free standard).
        Formula: eGFR = 142 * min(Scr/kappa, 1)^alpha * max(Scr/kappa, 1)^-1.200 * 0.9938^Age * (1.012 if female)
        """
        if serum_creatinine_mg_dl <= 0:
            raise ValueError("Serum creatinine must be a positive value.")
        if age < 18:
            raise ValueError("CKD-EPI formula is validated for adult patients (age >= 18). Use Schwartz for pediatrics.")

        kappa = 0.7 if is_female else 0.9
        alpha = -0.241 if is_female else -0.302
        scr_k = serum_creatinine_mg_dl / kappa

        term1 = min(scr_k, 1.0) ** alpha
        term2 = max(scr_k, 1.0) ** -1.200
        age_term = 0.9938 ** age
        female_mult = 1.012 if is_female else 1.000

        egfr = 142.0 * term1 * term2 * age_term * female_mult
        egfr_rounded = round(egfr, 1)

        # KDIGO Staging
        if egfr_rounded >= 90.0:
            stage = "G1"
            description = "Normal or High renal function"
        elif egfr_rounded >= 60.0:
            stage = "G2"
            description = "Mildly decreased renal function"
        elif egfr_rounded >= 45.0:
            stage = "G3a"
            description = "Mildly to moderately decreased renal function"
        elif egfr_rounded >= 30.0:
            stage = "G3b"
            description = "Moderately to severely decreased renal function"
        elif egfr_rounded >= 15.0:
            stage = "G4"
            description = "Severely decreased renal function"
        else:
            stage = "G5"
            description = "Kidney failure (End-Stage Renal Disease - ESRD)"

        return {
            "egfr_ml_min_1_73m2": egfr_rounded,
            "kdigo_stage": stage,
            "stage_description": description,
            "requires_dose_adjustment": egfr_rounded < 50.0,
        }

    @staticmethod
    def calculate_cockcroft_gault_crcl(
        serum_creatinine_mg_dl: float,
        age: int,
        weight_kg: float,
        is_female: bool,
    ) -> Dict[str, Any]:
        """
        Cockcroft-Gault Creatinine Clearance Calculator for Pharmacokinetic Dosing.
        CrCl (mL/min) = [(140 - age) * weight(kg)] / [72 * Scr(mg/dL)] * (0.85 if female)
        """
        if serum_creatinine_mg_dl <= 0 or weight_kg <= 0 or age <= 0:
            raise ValueError("Parameters must be positive non-zero numbers.")

        numerator = (140 - age) * weight_kg
        denominator = 72.0 * serum_creatinine_mg_dl
        crcl = (numerator / denominator) * (0.85 if is_female else 1.0)
        crcl_rounded = round(crcl, 1)

        # Renal dosing tier
        if crcl_rounded >= 90.0:
            tier = "NORMAL_CLEARANCE"
            notes = "Standard drug dosing."
        elif crcl_rounded >= 60.0:
            tier = "MILD_IMPAIRMENT"
            notes = "Standard dosing for most drugs; monitor narrow therapeutic index agents."
        elif crcl_rounded >= 30.0:
            tier = "MODERATE_IMPAIRMENT"
            notes = "Reduce dose or extend dosing interval for renally eliminated medications (e.g., Vancomycin, Enoxaparin, Novel Oral Anticoagulants)."
        elif crcl_rounded >= 15.0:
            tier = "SEVERE_IMPAIRMENT"
            notes = "Significant dose reductions required. Avoid Metformin, NSAIDs, and Nitrofurantoin."
        else:
            tier = "END_STAGE_RENAL_FAILURE"
            notes = "Hemodialysis / peritoneal dialysis dosing protocols required."

        return {
            "creatinine_clearance_ml_min": crcl_rounded,
            "renal_tier": tier,
            "dosing_guidance": notes,
        }
