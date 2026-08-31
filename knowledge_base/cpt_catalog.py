"""
CPT & HCPCS Master Medical Procedures and Services Catalog
Coding and Relative Value Units (RVU) for clinical billing.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CPTEntry:
    code: str
    description: str
    category: str
    rvu_total: float
    standard_fee: float


class CPTCatalog:
    """Master medical procedure and billing catalog."""

    _ENTRIES: Dict[str, CPTEntry] = {}

    @classmethod
    def initialize(cls):
        if cls._ENTRIES:
            return

        cpt_data = [
            ("99202", "Office/outpatient visit, new patient, straightforward MDM, 15-29 mins", "Evaluation & Management", 2.14, 95.00),
            ("99203", "Office/outpatient visit, new patient, low MDM, 30-44 mins", "Evaluation & Management", 3.25, 145.00),
            ("99204", "Office/outpatient visit, new patient, moderate MDM, 45-59 mins", "Evaluation & Management", 4.88, 220.00),
            ("99205", "Office/outpatient visit, new patient, high MDM, 60-74 mins", "Evaluation & Management", 6.22, 290.00),
            ("99211", "Office visit, established patient, minimal evaluation (nurse visit)", "Evaluation & Management", 0.65, 35.00),
            ("99212", "Office visit, established patient, straightforward MDM, 10-19 mins", "Evaluation & Management", 1.58, 70.00),
            ("99213", "Office visit, established patient, low MDM, 20-29 mins", "Evaluation & Management", 2.56, 115.00),
            ("99214", "Office visit, established patient, moderate MDM, 30-39 mins", "Evaluation & Management", 3.72, 175.00),
            ("99215", "Office visit, established patient, high MDM, 40-54 mins", "Evaluation & Management", 5.12, 245.00),
            ("99281", "Emergency department visit, straightforward MDM", "Emergency Services", 1.15, 60.00),
            ("99283", "Emergency department visit, moderate complexity", "Emergency Services", 2.85, 160.00),
            ("99285", "Emergency department visit, high complexity with immediate threat", "Emergency Services", 5.60, 350.00),
            ("93000", "Electrocardiogram (ECG/EKG), routine 12-lead with interpretation and report", "Cardiovascular", 0.61, 45.00),
            ("93306", "Echocardiography, transthoracic, complete with Doppler and color flow", "Cardiovascular", 6.80, 420.00),
            ("71045", "Radiologic examination, chest; single view (Chest X-ray)", "Radiology", 0.45, 65.00),
            ("71046", "Radiologic examination, chest; 2 views (PA and Lateral)", "Radiology", 0.62, 85.00),
            ("70450", "Computed tomography, head or brain; without contrast", "Radiology", 4.20, 380.00),
            ("74177", "Computed tomography, abdomen and pelvis; with contrast material", "Radiology", 8.45, 650.00),
            ("80053", "Comprehensive Metabolic Panel (CMP) 14 clinical assays", "Pathology & Laboratory", 0.40, 45.00),
            ("85025", "Complete Blood Count (CBC) with automated differential", "Pathology & Laboratory", 0.32, 35.00),
            ("80061", "Lipid Panel (Total Cholesterol, HDL, Triglycerides, Calc LDL)", "Pathology & Laboratory", 0.50, 40.00),
            ("83036", "Hemoglobin A1c (Glycated hemoglobin assay)", "Pathology & Laboratory", 0.45, 38.00),
        ]

        for code, desc, cat, rvu, fee in cpt_data:
            cls._ENTRIES[code] = CPTEntry(code=code, description=desc, category=cat, rvu_total=rvu, standard_fee=fee)

    @classmethod
    def get_by_code(cls, code: str) -> Optional[CPTEntry]:
        cls.initialize()
        return cls._ENTRIES.get(code.strip())
