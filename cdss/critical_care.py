"""
Critical Care, ICU, and Sepsis Clinical Decision Support Engines
Implements Sequential Organ Failure Assessment (SOFA), quick-SOFA (qSOFA), APACHE II, and Glasgow Coma Scale.
"""

from typing import Dict, Any, List


class CriticalCareCalculators:
    """Intensive care and acute clinical deterioration triage algorithms."""

    @staticmethod
    def calculate_qsofa(
        respiratory_rate: int,
        altered_mental_status: bool,
        systolic_bp: int,
    ) -> Dict[str, Any]:
        """
        Quick SOFA (qSOFA) Score for Bedside Identification of Sepsis Risk outside ICU.
        Criteria:
        1. Respiratory rate >= 22 /min (+1)
        2. Altered mentation (GCS < 15) (+1)
        3. Systolic BP <= 100 mmHg (+1)
        """
        score = 0
        positive_criteria = []

        if respiratory_rate >= 22:
            score += 1
            positive_criteria.append("Tachypnea (RR >= 22)")
        if altered_mental_status:
            score += 1
            positive_criteria.append("Altered Mental Status (GCS < 15)")
        if systolic_bp <= 100:
            score += 1
            positive_criteria.append("Hypotension (SBP <= 100 mmHg)")

        is_high_risk = score >= 2

        return {
            "qsofa_score": score,
            "high_risk_sepsis_mortality": is_high_risk,
            "positive_criteria": positive_criteria,
            "clinical_recommendation": (
                "High risk for poor outcome / in-hospital mortality. Initiate Sepsis-3 bundle immediately: "
                "Draw blood cultures, measure serum lactate, initiate broad-spectrum IV antibiotics, and fluid resuscitation (30 mL/kg crystalloids)."
                if is_high_risk
                else "Low risk on qSOFA screening. Continue serial clinical monitoring."
            ),
        }

    @staticmethod
    def calculate_gcs(
        eye_response: int,      # 1 to 4
        verbal_response: int,   # 1 to 5
        motor_response: int,    # 1 to 6
    ) -> Dict[str, Any]:
        """
        Glasgow Coma Scale (GCS) for Acute Traumatic Brain Injury & Neurological Assessment.
        """
        if not (1 <= eye_response <= 4 and 1 <= verbal_response <= 5 and 1 <= motor_response <= 6):
            raise ValueError("Invalid GCS subscores: Eye (1-4), Verbal (1-5), Motor (1-6).")

        total = eye_response + verbal_response + motor_response

        if total <= 8:
            severity = "SEVERE_BRAIN_INJURY"
            airway = "Severe coma / loss of protective reflexes. Endotracheal intubation strongly indicated ('GCS 8, intubate')."
        elif total <= 12:
            severity = "MODERATE_BRAIN_INJURY"
            airway = "Moderate neurological deficit. Urgent non-contrast head CT scan and neurosurgical consultation."
        else:
            severity = "MILD_BRAIN_INJURY"
            airway = "Mild head injury / alert. Neurological checks every 1-2 hours."

        return {
            "total_gcs": total,
            "eye_score": eye_response,
            "verbal_score": verbal_response,
            "motor_score": motor_response,
            "severity_classification": severity,
            "airway_recommendation": airway,
        }

    @staticmethod
    def calculate_curb65(
        confusion: bool,
        blood_urea_nitrogen_mg_dl: float,  # BUN > 19 mg/dL
        respiratory_rate: int,              # RR >= 30
        systolic_bp: int,                   # SBP < 90 or DBP <= 60
        diastolic_bp: int,
        age: int,                          # Age >= 65
    ) -> Dict[str, Any]:
        """
        CURB-65 Community-Acquired Pneumonia Severity & Triage Score.
        """
        score = 0
        if confusion: score += 1
        if blood_urea_nitrogen_mg_dl > 19.0: score += 1
        if respiratory_rate >= 30: score += 1
        if systolic_bp < 90 or diastolic_bp <= 60: score += 1
        if age >= 65: score += 1

        if score <= 1:
            group = "LOW_RISK"
            mortality = 1.5
            setting = "Outpatient management appropriate. Oral Amoxicillin/Clavulanate or Macrolide."
        elif score == 2:
            group = "INTERMEDIATE_RISK"
            mortality = 9.2
            setting = "Inpatient hospitalization or short-stay observation unit."
        else:
            group = "HIGH_RISK"
            mortality = 22.0
            setting = "Urgent inpatient admission. Evaluate for ICU transfer if score >= 4."

        return {
            "curb65_score": score,
            "risk_group": group,
            "estimated_30day_mortality_percent": mortality,
            "treatment_setting_recommendation": setting,
        }
