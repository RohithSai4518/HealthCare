"""
Laboratory Diagnostics & Reference Assay Encyclopedia
LOINC standards, clinical indications, diagnostic utility, and biological reference ranges.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from core.enums import AbnormalityFlag, LabTestCategory
from domain.laboratory import ReferenceRange


@dataclass(frozen=True)
class LabDiagnosticAssay:
    loinc_code: str
    cpt_code: str
    test_name: str
    category: LabTestCategory
    specimen: str
    reference_range: ReferenceRange
    clinical_utility: str
    critical_panic_action: str


class LabEncyclopedia:
    """Master diagnostic pathology encyclopedia."""

    _ASSAYS: Dict[str, LabDiagnosticAssay] = {}

    @classmethod
    def initialize(cls):
        if cls._ASSAYS:
            return

        assays = [
            LabDiagnosticAssay(
                loinc_code="718-7",
                cpt_code="85025",
                test_name="Hemoglobin (Hgb)",
                category=LabTestCategory.HEMATOLOGY,
                specimen="Whole Blood (Lavender Top EDTA)",
                reference_range=ReferenceRange(low_value=13.5, high_value=17.5, unit_of_measure="g/dL", critical_low=7.0, critical_high=20.0),
                clinical_utility="Evaluation of anemia, polycythemia, acute hemorrhage, and transfusion requirements.",
                critical_panic_action="Notify ordering physician immediately for emergency packed RBC transfusion protocol if symptomatic.",
            ),
            LabDiagnosticAssay(
                loinc_code="2345-7",
                cpt_code="82947",
                test_name="Fasting Plasma Glucose (FPG)",
                category=LabTestCategory.BIOCHEMISTRY,
                specimen="Fluoride Oxalate Plasma (Grey Top) or Serum",
                reference_range=ReferenceRange(low_value=70.0, high_value=99.0, unit_of_measure="mg/dL", critical_low=45.0, critical_high=400.0),
                clinical_utility="Diagnosis of diabetes mellitus, impaired fasting glucose, and acute hypoglycemia monitoring.",
                critical_panic_action="For severe hypoglycemia (<45 mg/dL), administer IV Dextrose 50% immediately. For severe hyperglycemia (>400 mg/dL), evaluate for DKA/HHS.",
            ),
            LabDiagnosticAssay(
                loinc_code="2160-0",
                cpt_code="82565",
                test_name="Serum Creatinine",
                category=LabTestCategory.BIOCHEMISTRY,
                specimen="Serum (Gold SST)",
                reference_range=ReferenceRange(low_value=0.7, high_value=1.3, unit_of_measure="mg/dL", critical_high=5.0),
                clinical_utility="Assessment of glomerular filtration rate (GFR) and acute kidney injury (AKI).",
                critical_panic_action="Check electrolytes for concomitant hyperkalemia; prepare for urgent nephrology review.",
            ),
            LabDiagnosticAssay(
                loinc_code="2823-3",
                cpt_code="84132",
                test_name="Serum Potassium (K+)",
                category=LabTestCategory.BIOCHEMISTRY,
                specimen="Serum (Gold SST) - avoid hemolysis",
                reference_range=ReferenceRange(low_value=3.5, high_value=5.0, unit_of_measure="mmol/L", critical_low=2.8, critical_high=6.2),
                clinical_utility="Electrolyte balance, cardiac conduction, and renal tubular function assessment.",
                critical_panic_action="Urgent 12-lead ECG for peaked T waves / arrhythmias. Administer IV Calcium gluconate, Insulin + Dextrose, or Lokelma.",
            ),
        ]

        for assay in assays:
            cls._ASSAYS[assay.loinc_code] = assay

    @classmethod
    def get_assay(cls, loinc_code: str) -> Optional[LabDiagnosticAssay]:
        cls.initialize()
        return cls._ASSAYS.get(loinc_code.strip())
