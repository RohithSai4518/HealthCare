"""
Comprehensive Clinical Pharmacopeia & Drug Formulary
Formulary classifications, indications, blackbox warnings, and pharmacology data.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from core.enums import DrugForm


@dataclass(frozen=True)
class PharmacopeiaDrug:
    ndc: str
    generic_name: str
    brand_name: str
    drug_class: str
    form: DrugForm
    strength: str
    indications: List[str]
    contraindications: List[str]
    common_adverse_effects: List[str]
    blackbox_warning: Optional[str]
    standard_adult_dose: str
    unit_price_usd: float


class Pharmacopeia:
    """Master clinical pharmaceutical drug repository."""

    _CATALOG: Dict[str, PharmacopeiaDrug] = {}

    @classmethod
    def initialize(cls):
        if cls._CATALOG:
            return

        drugs = [
            PharmacopeiaDrug(
                ndc="0071-0155-23",
                generic_name="Atorvastatin Calcium",
                brand_name="Lipitor",
                drug_class="HMG-CoA Reductase Inhibitor (Statin)",
                form=DrugForm.TABLET,
                strength="20mg",
                indications=["Primary hyperlipidemia", "Atherosclerotic cardiovascular disease (ASCVD) prevention"],
                contraindications=["Active liver disease", "Pregnancy / Lactation", "Hypersensitivity"],
                common_adverse_effects=["Myalgia", "Arthralgia", "Diarrhea", "Nasopharyngitis", "Elevated transaminases"],
                blackbox_warning=None,
                standard_adult_dose="10-80 mg orally once daily in the evening",
                unit_price_usd=15.00,
            ),
            PharmacopeiaDrug(
                ndc="0093-0105-01",
                generic_name="Metformin Hydrochloride",
                brand_name="Glucophage",
                drug_class="Biguanide Antidiabetic",
                form=DrugForm.TABLET,
                strength="500mg",
                indications=["Type 2 diabetes mellitus", "Prediabetes management", "PCOS"],
                contraindications=["Severe renal impairment (eGFR < 30 mL/min)", "Acute metabolic acidosis / DKA", "Hypoxemic states"],
                common_adverse_effects=["Nausea", "Vomiting", "Diarrhea", "Abdominal discomfort", "Vitamin B12 deficiency"],
                blackbox_warning="Lactic Acidosis: Rare but life-threatening risk in severe renal or hepatic disease.",
                standard_adult_dose="500 mg twice daily with meals, titrate to max 2000-2500 mg daily",
                unit_price_usd=10.00,
            ),
            PharmacopeiaDrug(
                ndc="0006-0740-54",
                generic_name="Lisinopril",
                brand_name="Prinivil / Zestril",
                drug_class="ACE Inhibitor (Angiotensin-Converting Enzyme)",
                form=DrugForm.TABLET,
                strength="10mg",
                indications=["Hypertension", "Heart failure with reduced ejection fraction (HFrEF)", "Post-myocardial infarction"],
                contraindications=["History of angioedema", "Concomitant Aliskiren in diabetes", "Pregnancy (2nd/3rd trimester)"],
                common_adverse_effects=["Dry cough", "Dizziness", "Hypotension", "Hyperkalemia", "Increased serum creatinine"],
                blackbox_warning="Fetal Toxicity: Can cause fetal harm and death when administered to pregnant women.",
                standard_adult_dose="10-40 mg orally once daily",
                unit_price_usd=12.00,
            ),
            PharmacopeiaDrug(
                ndc="0085-1132-01",
                generic_name="Albuterol Sulfate",
                brand_name="Ventolin HFA / ProAir",
                drug_class="Short-Acting Beta-2 Agonist (SABA) Bronchodilator",
                form=DrugForm.INHALER,
                strength="90mcg/actuation",
                indications=["Acute bronchospasm in asthma and COPD", "Exercise-induced bronchoconstriction prevention"],
                contraindications=["Hypersensitivity to albuterol or milk proteins (dry powder formulations)"],
                common_adverse_effects=["Tremor", "Tachycardia", "Palpitations", "Nervousness", "Hypokalemia"],
                blackbox_warning=None,
                standard_adult_dose="1-2 inhalations every 4-6 hours PRN acute dyspnea",
                unit_price_usd=35.00,
            ),
            PharmacopeiaDrug(
                ndc="0054-0010-25",
                generic_name="Warfarin Sodium",
                brand_name="Coumadin / Jantoven",
                drug_class="Vitamin K Antagonist Anticoagulant",
                form=DrugForm.TABLET,
                strength="5mg",
                indications=["Atrial fibrillation thromboembolism prophylaxis", "Deep vein thrombosis (DVT)", "Pulmonary embolism (PE)", "Mechanical heart valves"],
                contraindications=["Active pathological hemorrhage", "Severe thrombocytopenia", "Pregnancy (except mechanical valves)", "Recent CNS surgery"],
                common_adverse_effects=["Major and minor bleeding", "Bruising", "Hematuria", "Epistaxis"],
                blackbox_warning="Major Bleeding: Can cause fatal hemorrhages. Regular INR monitoring mandatory.",
                standard_adult_dose="2-10 mg orally once daily adjusted based on target INR (usually 2.0-3.0)",
                unit_price_usd=22.00,
            ),
            PharmacopeiaDrug(
                ndc="0029-6086-12",
                generic_name="Amoxicillin / Clavulanate Potassium",
                brand_name="Augmentin",
                drug_class="Beta-Lactam + Beta-Lactamase Inhibitor Antibacterial",
                form=DrugForm.TABLET,
                strength="875mg/125mg",
                indications=["Acute bacterial sinusitis", "Community-acquired pneumonia", "Otitis media", "Skin & soft tissue infections"],
                contraindications=["History of severe penicillin allergy / anaphylaxis", "History of amoxicillin-clavulanate associated cholestatic jaundice"],
                common_adverse_effects=["Diarrhea", "Nausea", "Skin rash", "Vaginal candidiasis", "Clostridioides difficile colitis"],
                blackbox_warning=None,
                standard_adult_dose="875/125 mg orally twice daily for 7-10 days",
                unit_price_usd=28.00,
            ),
        ]

        for drug in drugs:
            cls._CATALOG[drug.generic_name.lower()] = drug

    @classmethod
    def get_drug(cls, generic_name: str) -> Optional[PharmacopeiaDrug]:
        cls.initialize()
        return cls._CATALOG.get(generic_name.strip().lower())

    @classmethod
    def all_drugs(cls) -> List[PharmacopeiaDrug]:
        cls.initialize()
        return list(cls._CATALOG.values())
