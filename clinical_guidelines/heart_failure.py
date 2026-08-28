"""
AHA/ACC/HFSA Guideline-Directed Medical Therapy (GDMT) for Heart Failure
Four pillars of HFrEF therapy, dosing titration, and volume management protocols.
"""

from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class HeartFailureEvaluation:
    nyha_functional_class: str
    hf_category: str  # HFrEF (<=40%), HFmrEF (41-49%), HFpEF (>=50%)
    gdmt_four_pillars: List[str]
    diuretic_plan: str
    contraindication_alerts: List[str]
    monitoring_parameters: List[str]


class HeartFailureGuideline:
    """Heart Failure Clinical Guideline Decision Support."""

    @staticmethod
    def evaluate(
        lvef_percent: int,
        nyha_class: int,  # 1 to 4
        systolic_bp: int,
        serum_potassium_mmol_l: float,
        egfr_ml_min: float,
        has_volume_overload: bool,
    ) -> HeartFailureEvaluation:
        """Generates GDMT recommendations based on LVEF and hemodynamic profile."""

        if lvef_percent <= 40:
            hf_cat = "HFrEF (Heart Failure with Reduced Ejection Fraction)"
        elif lvef_percent <= 49:
            hf_cat = "HFmrEF (Heart Failure with Mildly Reduced Ejection Fraction)"
        else:
            hf_cat = "HFpEF (Heart Failure with Preserved Ejection Fraction)"

        nyha_map = {
            1: "NYHA Class I: No limitation of physical activity.",
            2: "NYHA Class II: Slight limitation; comfortable at rest, ordinary activity causes fatigue/dyspnea.",
            3: "NYHA Class III: Marked limitation; comfortable at rest, less than ordinary activity causes symptoms.",
            4: "NYHA Class IV: Inability to carry on any physical activity without discomfort; symptoms at rest.",
        }
        nyha_str = nyha_map.get(nyha_class, "NYHA Class II")

        # Four Pillars of HFrEF GDMT
        pillars = []
        alerts = []

        # Pillar 1: ARNI / ACEI
        if systolic_bp >= 100 and egfr_ml_min >= 30:
            pillars.append("Pillar 1 (ARNI): Sacubitril/Valsartan 24/26 mg or 49/51 mg twice daily (preferred over ACEI/ARB)")
        elif systolic_bp < 90:
            alerts.append("Caution: SBP < 90 mmHg. Hold or titrate ARNI/ACEI carefully.")
            pillars.append("Pillar 1: Low-dose ACEI (Lisinopril 2.5-5mg) with close hemodynamic monitoring.")
        else:
            pillars.append("Pillar 1 (ACEI/ARB): Enalapril 2.5-10mg twice daily or Losartan 25-50mg daily.")

        # Pillar 2: Evidence-Based Beta-Blocker
        pillars.append("Pillar 2 (Beta-Blocker): Metoprolol Succinate (ER) 25-200mg daily, Carvedilol 3.125-25mg BID, or Bisoprolol 1.25-10mg daily.")

        # Pillar 3: Mineralocorticoid Receptor Antagonist (MRA)
        if serum_potassium_mmol_l < 5.0 and egfr_ml_min >= 30:
            pillars.append("Pillar 3 (MRA): Spironolactone 12.5-25mg daily or Eplerenone 25mg daily.")
        else:
            alerts.append(f"MRA Held: Serum Potassium is {serum_potassium_mmol_l} mmol/L (Must be < 5.0) or eGFR < 30.")

        # Pillar 4: SGLT2 Inhibitor
        pillars.append("Pillar 4 (SGLT2i): Empagliflozin 10mg daily OR Dapagliflozin 10mg daily (induces mortality benefit regardless of diabetes).")

        # Volume Management (Loop Diuretics)
        if has_volume_overload:
            diuretic = "Furosemide 20-40mg IV/oral daily (or Bumetanide 1mg) titrated to achieve euvolemia / dry weight."
        else:
            diuretic = "Maintain lowest effective maintenance diuretic dose to preserve stable euvolemic dry weight."

        monitoring = [
            "Daily morning weight tracking (report gain > 3 lbs in 24h or > 5 lbs in a week).",
            "Basic Metabolic Panel (Electrolytes, BUN, Creatinine) at 1-2 weeks following each GDMT titration.",
            "Serial BNP / NT-proBNP biomarker assessment.",
            "Repeat Transthoracic Echocardiogram (TTE) in 3-6 months to assess reverse remodeling / LVEF recovery.",
        ]

        return HeartFailureEvaluation(
            nyha_functional_class=nyha_str,
            hf_category=hf_cat,
            gdmt_four_pillars=pillars,
            diuretic_plan=diuretic,
            contraindication_alerts=alerts,
            monitoring_parameters=monitoring,
        )
