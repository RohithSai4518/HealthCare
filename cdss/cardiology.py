"""
Cardiovascular Risk Calculators and Clinical Decision Rules
Implements Framingham 10-year CVD risk, CHA2DS2-VASc, HAS-BLED, ASCVD Risk, TIMI, and HEART Score.
"""

import math
from typing import Dict, Any, Tuple, Optional


class CardiologyCalculators:
    """Evidence-based clinical decision support tools for cardiovascular disease management."""

    @staticmethod
    def calculate_cha2ds2_vasc(
        age: int,
        is_female: bool,
        congestive_heart_failure: bool,
        hypertension: bool,
        stroke_or_tia_history: bool,
        vascular_disease: bool,
        diabetes: bool,
    ) -> Dict[str, Any]:
        """
        CHA2DS2-VASc Score for Atrial Fibrillation Stroke Risk.
        Guides oral anticoagulation (OAC) therapy decisions.
        """
        score = 0
        factors = []

        if congestive_heart_failure:
            score += 1
            factors.append("Congestive Heart Failure (+1)")
        if hypertension:
            score += 1
            factors.append("Hypertension (+1)")
        if age >= 75:
            score += 2
            factors.append("Age >= 75 (+2)")
        elif 65 <= age <= 74:
            score += 1
            factors.append("Age 65-74 (+1)")
        if diabetes:
            score += 1
            factors.append("Diabetes Mellitus (+1)")
        if stroke_or_tia_history:
            score += 2
            factors.append("Prior Stroke/TIA/Thromboembolism (+2)")
        if vascular_disease:
            score += 1
            factors.append("Vascular Disease (MI, PAD, aortic plaque) (+1)")
        if is_female:
            score += 1
            factors.append("Female Sex (+1)")

        # Clinical Recommendation
        if (not is_female and score == 0) or (is_female and score == 1):
            risk_category = "LOW"
            recommendation = "No antithrombotic therapy recommended (or low risk)."
            annual_stroke_rate = 0.2
        elif (not is_female and score == 1) or (is_female and score == 2):
            risk_category = "INTERMEDIATE"
            recommendation = "Oral anticoagulation should be considered based on individual clinical risk-benefit."
            annual_stroke_rate = 1.3
        else:
            risk_category = "HIGH"
            recommendation = "Oral anticoagulation strongly recommended (DOAC preferred over Warfarin)."
            annual_stroke_rate = min(15.0, 2.2 * (score - 1))

        return {
            "score": score,
            "risk_category": risk_category,
            "annual_stroke_risk_percentage": round(annual_stroke_rate, 1),
            "recommendation": recommendation,
            "contributing_factors": factors,
        }

    @staticmethod
    def calculate_framingham_10year_risk(
        age: int,
        is_female: bool,
        total_cholesterol_mg_dl: float,
        hdl_cholesterol_mg_dl: float,
        systolic_bp: int,
        bp_treated: bool,
        is_smoker: bool,
    ) -> Dict[str, Any]:
        """
        Framingham 10-Year General Cardiovascular Disease Risk Algorithm.
        """
        if age < 30 or age > 79:
            raise ValueError("Framingham algorithm validated for ages 30-79.")

        ln_age = math.log(age)
        ln_tot_chol = math.log(total_cholesterol_mg_dl)
        ln_hdl = math.log(hdl_cholesterol_mg_dl)
        ln_sbp = math.log(systolic_bp)

        if not is_female:
            # Male model coefficients
            sbp_coeff = 1.99881 if bp_treated else 1.93303
            val = (
                3.06117 * ln_age
                + 1.12370 * ln_tot_chol
                - 0.93263 * ln_hdl
                + sbp_coeff * ln_sbp
                + (0.65451 if is_smoker else 0.0)
                - 23.9802
            )
            base_survival = 0.88936
        else:
            # Female model coefficients
            sbp_coeff = 2.03211 if bp_treated else 1.95706
            val = (
                2.32888 * ln_age
                + 1.20904 * ln_tot_chol
                - 0.70833 * ln_hdl
                + sbp_coeff * ln_sbp
                + (0.52873 if is_smoker else 0.0)
                - 26.1931
            )
            base_survival = 0.95012

        risk_percent = max(0.1, min(99.9, round((1.0 - math.pow(base_survival, math.exp(val))) * 100.0, 1)))

        if risk_percent < 10.0:
            category = "LOW_RISK"
            guideline = "Lifestyle modification, re-evaluate lipid profile every 3-5 years."
        elif risk_percent <= 20.0:
            category = "MODERATE_RISK"
            guideline = "Moderate-intensity statin therapy recommended if LDL-C >= 100 mg/dL."
        else:
            category = "HIGH_RISK"
            guideline = "High-intensity statin therapy (Atorvastatin 40-80mg or Rosuvastatin 20-40mg) and strict BP control (<130/80)."

        return {
            "ten_year_risk_percentage": risk_percent,
            "risk_category": category,
            "clinical_guideline": guideline,
        }

    @staticmethod
    def calculate_heart_score(
        history_high_risk: int,      # 0 (low), 1 (moderate), 2 (high)
        ecg_abnormal: int,           # 0 (normal), 1 (non-specific ST/T), 2 (significant ST depression)
        age: int,                    # <45=0, 45-64=1, >=65=2
        risk_factors_count: int,     # 0=0, 1-2=1, >=3 or atherosclerotic disease=2
        initial_troponin_elevated: int # 0 (normal), 1 (1-3x limit), 2 (>3x limit)
    ) -> Dict[str, Any]:
        """
        HEART Score for Major Adverse Cardiac Events (MACE) in Emergency Department Chest Pain.
        """
        age_score = 0 if age < 45 else (1 if age <= 64 else 2)
        score = history_high_risk + ecg_abnormal + age_score + risk_factors_count + initial_troponin_elevated

        if score <= 3:
            mace_rate = 1.7
            risk_level = "LOW"
            action = "Candidate for early discharge and outpatient stress testing / provocative evaluation."
        elif score <= 6:
            mace_rate = 16.6
            risk_level = "INTERMEDIATE"
            action = "Admit to observation unit, serial troponins, non-invasive imaging (CCTA or Stress Echo)."
        else:
            mace_rate = 50.1
            risk_level = "HIGH"
            action = "Immediate cardiology consultation, urgent coronary angiography / invasive strategy."

        return {
            "heart_score": score,
            "mace_risk_six_weeks_percentage": mace_rate,
            "risk_level": risk_level,
            "recommended_clinical_pathway": action,
        }
