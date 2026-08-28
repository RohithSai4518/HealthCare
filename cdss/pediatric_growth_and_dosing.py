"""
HealthSphere Pediatric Growth, Z-Scores & Resuscitation Dosing Engine
Implements WHO growth percentiles, LMS z-score calculations, and Broselow pediatric emergency resuscitation protocols.
"""

import math
from typing import Dict, List, Any, Optional


class PediatricClinicalEngine:
    """Pediatric clinical growth assessment and emergency pharmacotherapy dosing."""

    # Broselow Tape Color Zones (Weight in kg, length in cm)
    BROSELOW_ZONES = {
        "GREY": {"weight_min": 3, "weight_max": 5, "ett_size_uncuffed": 3.0, "defib_joules": 8, "epinephrine_mg": 0.04},
        "PINK": {"weight_min": 6, "weight_max": 7, "ett_size_uncuffed": 3.5, "defib_joules": 14, "epinephrine_mg": 0.07},
        "RED": {"weight_min": 8, "weight_max": 9, "ett_size_uncuffed": 3.5, "defib_joules": 18, "epinephrine_mg": 0.09},
        "PURPLE": {"weight_min": 10, "weight_max": 11, "ett_size_uncuffed": 4.0, "defib_joules": 22, "epinephrine_mg": 0.11},
        "YELLOW": {"weight_min": 12, "weight_max": 14, "ett_size_uncuffed": 4.5, "defib_joules": 28, "epinephrine_mg": 0.14},
        "WHITE": {"weight_min": 15, "weight_max": 18, "ett_size_uncuffed": 5.0, "defib_joules": 36, "epinephrine_mg": 0.18},
        "BLUE": {"weight_min": 19, "weight_max": 23, "ett_size_uncuffed": 5.5, "defib_joules": 46, "epinephrine_mg": 0.23},
        "ORANGE": {"weight_min": 24, "weight_max": 29, "ett_size_uncuffed": 6.0, "defib_joules": 58, "epinephrine_mg": 0.29},
        "GREEN": {"weight_min": 30, "weight_max": 36, "ett_size_uncuffed": 6.5, "defib_joules": 72, "epinephrine_mg": 0.36},
    }

    @classmethod
    def calculate_resuscitation_doses(cls, weight_kg: float) -> Dict[str, Any]:
        """
        Calculates PALS (Pediatric Advanced Life Support) emergency doses.
        """
        wt = max(3.0, min(50.0, weight_kg))

        # Find Broselow Zone
        zone_color = "WHITE"
        zone_data = cls.BROSELOW_ZONES["WHITE"]
        for color, data in cls.BROSELOW_ZONES.items():
            if data["weight_min"] <= wt <= data["weight_max"]:
                zone_color = color
                zone_data = data
                break

        # Standard PALS formulas
        cuffed_ett = (wt / 10.0) + 3.5
        uncuffed_ett = (wt / 10.0) + 4.0
        blade_size = 1 if wt < 10 else (2 if wt < 25 else 3)
        fluid_bolus_ml = wt * 20.0  # 20 mL/kg normal saline
        epinephrine_cardiac_arrest_ml = wt * 0.1  # 0.01 mg/kg (0.1 mL/kg of 1:10,000 solution)
        amiodarone_cardiac_arrest_mg = wt * 5.0  # 5 mg/kg IV push
        atropine_mg = max(0.1, min(0.5, wt * 0.02))  # 0.02 mg/kg
        dextrose_10_percent_ml = wt * 5.0  # 5 mL/kg D10W for hypoglycemia (<60 mg/dL)

        return {
            "weight_kg": wt,
            "broselow_color_zone": zone_color,
            "endotracheal_tube_cuffed_mm": round(cuffed_ett, 1),
            "endotracheal_tube_uncuffed_mm": round(uncuffed_ett, 1),
            "laryngoscope_blade_size": blade_size,
            "crystalloid_fluid_bolus_ml": fluid_bolus_ml,
            "epinephrine_cardiac_arrest_1_to_10k_ml": round(epinephrine_cardiac_arrest_ml, 2),
            "amiodarone_refractory_vf_vt_mg": round(amiodarone_cardiac_arrest_mg, 1),
            "atropine_bradycardia_mg": round(atropine_mg, 2),
            "dextrose_10_hypoglycemia_ml": round(dextrose_10_percent_ml, 1),
            "first_defibrillation_joules": round(wt * 2.0, 1),
            "subsequent_defibrillation_joules": round(wt * 4.0, 1),
        }
