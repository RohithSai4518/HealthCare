"""
Antimicrobial Stewardship & Empiric Infectious Disease Guidelines
Empiric coverage matrices for community and hospital acquired infections.
"""

from typing import Dict, List, Any


class AntimicrobialStewardship:
    """Hospital Empiric Antibiotic Therapy Guidance."""

    _REGIMENS: Dict[str, Dict[str, Any]] = {
        "CAP_OUTPATIENT_HEALTHY": {
            "condition": "Community-Acquired Pneumonia (Outpatient, no comorbidities)",
            "primary_regimen": "Amoxicillin 1g PO TID OR Doxycycline 100mg PO BID",
            "duration_days": 5,
            "alternative_allergy": "Azithromycin 500mg Day 1, then 250mg daily (if local pneumococcal macrolide resistance < 25%)",
        },
        "CAP_INPATIENT_NON_SEVERE": {
            "condition": "Community-Acquired Pneumonia (Inpatient Ward, Non-ICU)",
            "primary_regimen": "Ceftriaxone 1g-2g IV daily + Azithromycin 500mg IV/PO daily",
            "duration_days": 5,
            "alternative_allergy": "Respiratory Fluoroquinolone: Levofloxacin 750mg IV/PO daily OR Moxifloxacin 400mg daily",
        },
        "HAP_VAP_HIGH_RISK": {
            "condition": "Hospital-Acquired Pneumonia / Ventilator-Associated Pneumonia (High MRSA/Pseudomonas risk)",
            "primary_regimen": "Vancomycin 15-20 mg/kg IV q8-12h (Target trough 15-20) + Cefepime 2g IV q8h + Tobramycin 7 mg/kg IV daily",
            "duration_days": 7,
            "alternative_allergy": "Linezolid 600mg IV q12h + Aztreonam 2g IV q8h + Ciprofloxacin 400mg IV q8h",
        },
        "ACUTE_UNCOMPLICATED_CYSTITIS": {
            "condition": "Uncomplicated Urinary Tract Infection (Female)",
            "primary_regimen": "Nitrofurantoin Monohydrate/Macrocrystals 100mg PO BID with meals for 5 days OR TMP-SMX (Bactrim DS) 1 tab PO BID for 3 days",
            "duration_days": 5,
            "alternative_allergy": "Fosfomycin Trometamol 3g single oral dose powder",
        },
        "ACUTE_PYELONEPHRITIS": {
            "condition": "Acute Pyelonephritis (Inpatient)",
            "primary_regimen": "Ceftriaxone 1g-2g IV daily OR Ciprofloxacin 400mg IV q12h",
            "duration_days": 10,
            "alternative_allergy": "Gentamicin 5-7 mg/kg IV daily + Ampicillin",
        },
        "INTRA_ABDOMINAL_COMPLICATED": {
            "condition": "Complicated Intra-abdominal Infection (Secondary Peritonitis)",
            "primary_regimen": "Piperacillin-Tazobactam (Zosyn) 3.375g - 4.5g IV q6h (extended infusion over 4 hours)",
            "duration_days": 4,
            "alternative_allergy": "Ciprofloxacin 400mg IV q12h + Metronidazole 500mg IV q8h",
        },
    }

    @classmethod
    def get_empiric_regimen(cls, infection_code: str) -> Dict[str, Any]:
        return cls._REGIMENS.get(infection_code, {
            "condition": "Unknown Infection Code",
            "primary_regimen": "Consult Clinical Infectious Disease specialist.",
            "duration_days": 7,
        })
