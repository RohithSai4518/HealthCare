"""
GINA (Global Initiative for Asthma) Stepped Care Decision Protocols
"""

from typing import Dict, List, Any


class AsthmaGuideline:
    """GINA Stepped Care Protocol for Adolescents and Adults."""

    @staticmethod
    def get_track_1_step(step: int) -> Dict[str, Any]:
        """GINA Track 1: Preferred reliever is low-dose ICS-Formoterol."""
        steps = {
            1: {
                "step": 1,
                "classification": "Mild Intermittent Asthma",
                "controller_and_reliever": "As-needed low dose ICS-Formoterol (Budesonide/Formoterol 160/4.5 mcg 1 puff PRN)",
                "notes": "No regular daily controller required; takes ICS every time reliever is used.",
            },
            2: {
                "step": 2,
                "classification": "Mild Persistent Asthma",
                "controller_and_reliever": "As-needed low dose ICS-Formoterol OR daily low dose maintenance ICS + SABA PRN",
                "notes": "Significantly reduces severe exacerbation risk compared to SABA monotherapy.",
            },
            3: {
                "step": 3,
                "classification": "Moderate Persistent Asthma",
                "controller_and_reliever": "Daily maintenance low dose ICS-Formoterol + as-needed low dose ICS-Formoterol (SMART)",
                "notes": "Single Inhaler Maintenance and Reliever Therapy (SMART).",
            },
            4: {
                "step": 4,
                "classification": "Severe Persistent Asthma",
                "controller_and_reliever": "Daily maintenance medium dose ICS-Formoterol + as-needed low dose ICS-Formoterol",
                "notes": "Assess inhaler technique, adherence, and comorbid rhinosinusitis.",
            },
            5: {
                "step": 5,
                "classification": "Refractory Severe Asthma",
                "controller_and_reliever": "Daily high dose ICS-LABA + add-on LAMA (Tiotropium) + phenotypic biologic evaluation (Anti-IgE, Anti-IL5/5R, Anti-IL4R)",
                "notes": "Refer to severe asthma specialist center for biologic therapy.",
            },
        }
        return steps.get(step, steps[2])
