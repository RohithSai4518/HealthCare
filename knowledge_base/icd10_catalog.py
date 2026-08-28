"""
ICD-10-CM Master Diagnostic Codification Catalog
Standard diagnostic classifications across all human organ systems.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class ICD10Entry:
    code: str
    description: str
    chapter: str
    category: str
    is_chronic: bool = False
    requires_hcc: bool = False


class ICD10Catalog:
    """Master disease and diagnostic encyclopedia."""

    _ENTRIES: Dict[str, ICD10Entry] = {}

    @classmethod
    def initialize(cls):
        if cls._ENTRIES:
            return

        diagnoses = [
            # Infectious & Parasitic Diseases (A00-B99)
            ("A00.0", "Cholera due to Vibrio cholerae 01, biovar cholerae", "Infectious", "Intestinal infectious diseases", False, False),
            ("A02.0", "Salmonella enteritis", "Infectious", "Intestinal infectious diseases", False, False),
            ("A04.7", "Enterocolitis due to Clostridium difficile", "Infectious", "Intestinal infectious diseases", False, True),
            ("A08.4", "Viral intestinal infection, unspecified", "Infectious", "Intestinal infectious diseases", False, False),
            ("A09", "Infectious gastroenteritis and colitis, unspecified", "Infectious", "Intestinal infectious diseases", False, False),
            ("A41.9", "Sepsis, unspecified organism", "Infectious", "Sepsis", False, True),
            ("B20", "Human immunodeficiency virus [HIV] disease", "Infectious", "Viral infections", True, True),
            ("B34.9", "Viral infection, unspecified", "Infectious", "Viral infections", False, False),
            ("B37.0", "Candidal stomatitis (Oral thrush)", "Infectious", "Mycoses", False, False),

            # Neoplasms (C00-D49)
            ("C18.9", "Malignant neoplasm of colon, unspecified", "Neoplasms", "Digestive organs", True, True),
            ("C34.90", "Malignant neoplasm of unspecified part of bronchus or lung", "Neoplasms", "Respiratory organs", True, True),
            ("C50.919", "Malignant neoplasm of unspecified site of female breast", "Neoplasms", "Breast", True, True),
            ("C61", "Malignant neoplasm of prostate", "Neoplasms", "Male genital organs", True, True),
            ("C90.00", "Multiple myeloma not having achieved remission", "Neoplasms", "Lymphoid/hematopoietic", True, True),

            # Endocrine, Nutritional & Metabolic (E00-E89)
            ("E03.9", "Hypothyroidism, unspecified", "Endocrine", "Thyroid disorders", True, False),
            ("E05.90", "Thyrotoxicosis without thyrotoxic crisis or storm", "Endocrine", "Thyroid disorders", True, False),
            ("E10.9", "Type 1 diabetes mellitus without complications", "Endocrine", "Diabetes", True, True),
            ("E11.9", "Type 2 diabetes mellitus without complications", "Endocrine", "Diabetes", True, True),
            ("E11.65", "Type 2 diabetes mellitus with hyperglycemia", "Endocrine", "Diabetes", True, True),
            ("E11.40", "Type 2 diabetes mellitus with diabetic neuropathy, unspecified", "Endocrine", "Diabetes", True, True),
            ("E11.22", "Type 2 diabetes mellitus with diabetic chronic kidney disease", "Endocrine", "Diabetes", True, True),
            ("E66.01", "Morbid (severe) obesity due to excess calories", "Endocrine", "Obesity", True, True),
            ("E78.00", "Pure hypercholesterolemia, unspecified", "Endocrine", "Lipid metabolism", True, False),
            ("E78.5", "Hyperlipidemia, unspecified", "Endocrine", "Lipid metabolism", True, False),
            ("E87.1", "Hypo-osmolality and hyponatremia", "Endocrine", "Fluid & electrolyte", False, False),
            ("E87.6", "Hypokalemia", "Endocrine", "Fluid & electrolyte", False, False),

            # Mental & Behavioral Disorders (F01-F99)
            ("F10.20", "Alcohol dependence, uncomplicated", "Mental Health", "Substance use", True, True),
            ("F32.9", "Major depressive disorder, single episode, unspecified", "Mental Health", "Mood disorders", True, True),
            ("F41.1", "Generalized anxiety disorder", "Mental Health", "Anxiety disorders", True, False),
            ("F43.10", "Post-traumatic stress disorder, unspecified", "Mental Health", "Stress disorders", True, False),

            # Circulatory System (I00-I99)
            ("I10", "Essential (primary) hypertension", "Circulatory", "Hypertensive diseases", True, False),
            ("I11.0", "Hypertensive heart disease with heart failure", "Circulatory", "Hypertensive diseases", True, True),
            ("I12.9", "Hypertensive chronic kidney disease with stage 1 through stage 4 CKD", "Circulatory", "Hypertensive diseases", True, True),
            ("I20.9", "Angina pectoris, unspecified", "Circulatory", "Ischemic heart diseases", True, True),
            ("I21.9", "Acute myocardial infarction, unspecified", "Circulatory", "Ischemic heart diseases", False, True),
            ("I25.10", "Atherosclerotic heart disease of native coronary artery without angina pectoris", "Circulatory", "Ischemic heart diseases", True, True),
            ("I48.91", "Unspecified atrial fibrillation", "Circulatory", "Arrhythmias", True, True),
            ("I50.9", "Heart failure, unspecified", "Circulatory", "Heart failure", True, True),
            ("I50.22", "Chronic systolic (congestive) heart failure", "Circulatory", "Heart failure", True, True),
            ("I63.9", "Cerebral infarction, unspecified (Ischemic Stroke)", "Circulatory", "Cerebrovascular diseases", False, True),
            ("I73.9", "Peripheral vascular disease, unspecified", "Circulatory", "Arterial diseases", True, True),

            # Respiratory System (J00-J99)
            ("J00", "Acute nasopharyngitis [common cold]", "Respiratory", "Acute upper respiratory", False, False),
            ("J02.9", "Acute pharyngitis, unspecified", "Respiratory", "Acute upper respiratory", False, False),
            ("J06.9", "Acute upper respiratory infection, unspecified", "Respiratory", "Acute upper respiratory", False, False),
            ("J18.9", "Pneumonia, unspecified organism", "Respiratory", "Lower respiratory infections", False, True),
            ("J20.9", "Acute bronchitis, unspecified", "Respiratory", "Lower respiratory infections", False, False),
            ("J44.9", "Chronic obstructive pulmonary disease, unspecified", "Respiratory", "Chronic lower respiratory", True, True),
            ("J45.909", "Unspecified asthma, uncomplicated", "Respiratory", "Chronic lower respiratory", True, False),

            # Digestive System (K00-K95)
            ("K21.9", "Gastro-esophageal reflux disease without esophagitis", "Digestive", "Esophagus & stomach", True, False),
            ("K25.9", "Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation", "Digestive", "Esophagus & stomach", False, False),
            ("K35.80", "Unspecified acute appendicitis", "Digestive", "Appendix", False, False),
            ("K70.30", "Alcoholic cirrhosis of liver without ascites", "Digestive", "Liver diseases", True, True),
            ("K76.0", "Fatty (change of) liver, not elsewhere classified (NAFLD)", "Digestive", "Liver diseases", True, False),
            ("K80.20", "Calculus of gallbladder without cholecystitis without obstruction", "Digestive", "Gallbladder & bile ducts", False, False),

            # Musculoskeletal System (M00-M99)
            ("M06.9", "Rheumatoid arthritis, unspecified", "Musculoskeletal", "Inflammatory polyarthropathies", True, True),
            ("M17.9", "Osteoarthritis of knee, unspecified", "Musculoskeletal", "Osteoarthritis", True, False),
            ("M54.5", "Low back pain, unspecified", "Musculoskeletal", "Dorsopathies", False, False),
            ("M81.0", "Age-related osteoporosis without current pathological fracture", "Musculoskeletal", "Bone density disorders", True, False),

            # Genitourinary System (N00-N99)
            ("N18.3", "Chronic kidney disease, stage 3 (moderate)", "Genitourinary", "Renal failure", True, True),
            ("N18.4", "Chronic kidney disease, stage 4 (severe)", "Genitourinary", "Renal failure", True, True),
            ("N18.6", "End stage renal disease", "Genitourinary", "Renal failure", True, True),
            ("N39.0", "Urinary tract infection, site not specified", "Genitourinary", "Urinary system", False, False),
            ("N40.0", "Benign prostatic hyperplasia without lower urinary tract symptoms", "Genitourinary", "Male genital organs", True, False),
        ]

        for code, desc, chap, cat, chronic, hcc in diagnoses:
            cls._ENTRIES[code] = ICD10Entry(
                code=code,
                description=desc,
                chapter=chap,
                category=cat,
                is_chronic=chronic,
                requires_hcc=hcc,
            )

    @classmethod
    def get_by_code(cls, code: str) -> Optional[ICD10Entry]:
        cls.initialize()
        return cls._ENTRIES.get(code.strip().upper())

    @classmethod
    def search(cls, query: str) -> List[ICD10Entry]:
        cls.initialize()
        q = query.lower().strip()
        return [
            entry for entry in cls._ENTRIES.values()
            if q in entry.code.lower() or q in entry.description.lower() or q in entry.category.lower()
        ]

    @classmethod
    def count(cls) -> int:
        cls.initialize()
        return len(cls._ENTRIES)
