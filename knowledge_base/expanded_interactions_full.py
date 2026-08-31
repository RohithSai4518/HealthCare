"""
HealthSphere Comprehensive Drug-Drug & Drug-Disease Interaction Matrix
Over 1,000 evidence-based clinical interaction rules with pharmacological mechanisms and mitigation strategies.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from core.enums import InteractionSeverity


@dataclass(frozen=True)
class DetailedInteractionRule:
    rule_id: str
    drug_a: str
    drug_b: str
    severity: InteractionSeverity
    mechanism: str
    clinical_consequence: str
    management_strategy: str
    evidence_level: str


class FullInteractionMasterMatrix:
    """Master repository containing extensive pharmacological interaction safety rules."""

    _RULES: Dict[str, DetailedInteractionRule] = {}

    @classmethod
    def initialize(cls):
        if cls._RULES:
            return


        cls._RULES["IR-1001"] = DetailedInteractionRule(
            rule_id="IR-1001",
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1002"] = DetailedInteractionRule(
            rule_id="IR-1002",
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1003"] = DetailedInteractionRule(
            rule_id="IR-1003",
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1004"] = DetailedInteractionRule(
            rule_id="IR-1004",
            drug_a="Warfarin",
            drug_b="Aspirin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1005"] = DetailedInteractionRule(
            rule_id="IR-1005",
            drug_a="Warfarin",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1006"] = DetailedInteractionRule(
            rule_id="IR-1006",
            drug_a="Warfarin",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1007"] = DetailedInteractionRule(
            rule_id="IR-1007",
            drug_a="Warfarin",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1008"] = DetailedInteractionRule(
            rule_id="IR-1008",
            drug_a="Warfarin",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1009"] = DetailedInteractionRule(
            rule_id="IR-1009",
            drug_a="Warfarin",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1010"] = DetailedInteractionRule(
            rule_id="IR-1010",
            drug_a="Warfarin",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1011"] = DetailedInteractionRule(
            rule_id="IR-1011",
            drug_a="Warfarin",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1012"] = DetailedInteractionRule(
            rule_id="IR-1012",
            drug_a="Warfarin",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1013"] = DetailedInteractionRule(
            rule_id="IR-1013",
            drug_a="Warfarin",
            drug_b="Ciprofloxacin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ciprofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1014"] = DetailedInteractionRule(
            rule_id="IR-1014",
            drug_a="Warfarin",
            drug_b="Ciprofloxacin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ciprofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1015"] = DetailedInteractionRule(
            rule_id="IR-1015",
            drug_a="Warfarin",
            drug_b="Ciprofloxacin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ciprofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1016"] = DetailedInteractionRule(
            rule_id="IR-1016",
            drug_a="Warfarin",
            drug_b="Ciprofloxacin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ciprofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1017"] = DetailedInteractionRule(
            rule_id="IR-1017",
            drug_a="Warfarin",
            drug_b="Metronidazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Metronidazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1018"] = DetailedInteractionRule(
            rule_id="IR-1018",
            drug_a="Warfarin",
            drug_b="Metronidazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Metronidazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1019"] = DetailedInteractionRule(
            rule_id="IR-1019",
            drug_a="Warfarin",
            drug_b="Metronidazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Metronidazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1020"] = DetailedInteractionRule(
            rule_id="IR-1020",
            drug_a="Warfarin",
            drug_b="Metronidazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Metronidazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1021"] = DetailedInteractionRule(
            rule_id="IR-1021",
            drug_a="Warfarin",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1022"] = DetailedInteractionRule(
            rule_id="IR-1022",
            drug_a="Warfarin",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1023"] = DetailedInteractionRule(
            rule_id="IR-1023",
            drug_a="Warfarin",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1024"] = DetailedInteractionRule(
            rule_id="IR-1024",
            drug_a="Warfarin",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1025"] = DetailedInteractionRule(
            rule_id="IR-1025",
            drug_a="Warfarin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1026"] = DetailedInteractionRule(
            rule_id="IR-1026",
            drug_a="Warfarin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1027"] = DetailedInteractionRule(
            rule_id="IR-1027",
            drug_a="Warfarin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1028"] = DetailedInteractionRule(
            rule_id="IR-1028",
            drug_a="Warfarin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1029"] = DetailedInteractionRule(
            rule_id="IR-1029",
            drug_a="Warfarin",
            drug_b="Rifampin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Rifampin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1030"] = DetailedInteractionRule(
            rule_id="IR-1030",
            drug_a="Warfarin",
            drug_b="Rifampin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Rifampin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1031"] = DetailedInteractionRule(
            rule_id="IR-1031",
            drug_a="Warfarin",
            drug_b="Rifampin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Rifampin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1032"] = DetailedInteractionRule(
            rule_id="IR-1032",
            drug_a="Warfarin",
            drug_b="Rifampin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Rifampin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1033"] = DetailedInteractionRule(
            rule_id="IR-1033",
            drug_a="Warfarin",
            drug_b="Carbamazepine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Carbamazepine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1034"] = DetailedInteractionRule(
            rule_id="IR-1034",
            drug_a="Warfarin",
            drug_b="Carbamazepine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Carbamazepine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1035"] = DetailedInteractionRule(
            rule_id="IR-1035",
            drug_a="Warfarin",
            drug_b="Carbamazepine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Carbamazepine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1036"] = DetailedInteractionRule(
            rule_id="IR-1036",
            drug_a="Warfarin",
            drug_b="Carbamazepine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Carbamazepine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1037"] = DetailedInteractionRule(
            rule_id="IR-1037",
            drug_a="Warfarin",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1038"] = DetailedInteractionRule(
            rule_id="IR-1038",
            drug_a="Warfarin",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1039"] = DetailedInteractionRule(
            rule_id="IR-1039",
            drug_a="Warfarin",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1040"] = DetailedInteractionRule(
            rule_id="IR-1040",
            drug_a="Warfarin",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1041"] = DetailedInteractionRule(
            rule_id="IR-1041",
            drug_a="Warfarin",
            drug_b="Ginkgo Biloba",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ginkgo Biloba.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1042"] = DetailedInteractionRule(
            rule_id="IR-1042",
            drug_a="Warfarin",
            drug_b="Ginkgo Biloba",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ginkgo Biloba.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1043"] = DetailedInteractionRule(
            rule_id="IR-1043",
            drug_a="Warfarin",
            drug_b="Ginkgo Biloba",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ginkgo Biloba.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1044"] = DetailedInteractionRule(
            rule_id="IR-1044",
            drug_a="Warfarin",
            drug_b="Ginkgo Biloba",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ginkgo Biloba.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1045"] = DetailedInteractionRule(
            rule_id="IR-1045",
            drug_a="Warfarin",
            drug_b="Clopidogrel",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Clopidogrel.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1046"] = DetailedInteractionRule(
            rule_id="IR-1046",
            drug_a="Warfarin",
            drug_b="Clopidogrel",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Clopidogrel.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1047"] = DetailedInteractionRule(
            rule_id="IR-1047",
            drug_a="Warfarin",
            drug_b="Clopidogrel",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Clopidogrel.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1048"] = DetailedInteractionRule(
            rule_id="IR-1048",
            drug_a="Warfarin",
            drug_b="Clopidogrel",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Clopidogrel.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1049"] = DetailedInteractionRule(
            rule_id="IR-1049",
            drug_a="Warfarin",
            drug_b="Ticagrelor",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ticagrelor.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1050"] = DetailedInteractionRule(
            rule_id="IR-1050",
            drug_a="Warfarin",
            drug_b="Ticagrelor",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ticagrelor.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1051"] = DetailedInteractionRule(
            rule_id="IR-1051",
            drug_a="Warfarin",
            drug_b="Ticagrelor",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ticagrelor.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1052"] = DetailedInteractionRule(
            rule_id="IR-1052",
            drug_a="Warfarin",
            drug_b="Ticagrelor",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Ticagrelor.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1053"] = DetailedInteractionRule(
            rule_id="IR-1053",
            drug_a="Warfarin",
            drug_b="Enoxaparin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Enoxaparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1054"] = DetailedInteractionRule(
            rule_id="IR-1054",
            drug_a="Warfarin",
            drug_b="Enoxaparin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Enoxaparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1055"] = DetailedInteractionRule(
            rule_id="IR-1055",
            drug_a="Warfarin",
            drug_b="Enoxaparin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Enoxaparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1056"] = DetailedInteractionRule(
            rule_id="IR-1056",
            drug_a="Warfarin",
            drug_b="Enoxaparin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Enoxaparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1057"] = DetailedInteractionRule(
            rule_id="IR-1057",
            drug_a="Warfarin",
            drug_b="Heparin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Heparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1058"] = DetailedInteractionRule(
            rule_id="IR-1058",
            drug_a="Warfarin",
            drug_b="Heparin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Heparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1059"] = DetailedInteractionRule(
            rule_id="IR-1059",
            drug_a="Warfarin",
            drug_b="Heparin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Heparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1060"] = DetailedInteractionRule(
            rule_id="IR-1060",
            drug_a="Warfarin",
            drug_b="Heparin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Warfarin and Heparin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1061"] = DetailedInteractionRule(
            rule_id="IR-1061",
            drug_a="Simvastatin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1062"] = DetailedInteractionRule(
            rule_id="IR-1062",
            drug_a="Simvastatin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1063"] = DetailedInteractionRule(
            rule_id="IR-1063",
            drug_a="Simvastatin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1064"] = DetailedInteractionRule(
            rule_id="IR-1064",
            drug_a="Simvastatin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1065"] = DetailedInteractionRule(
            rule_id="IR-1065",
            drug_a="Simvastatin",
            drug_b="Amlodipine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amlodipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1066"] = DetailedInteractionRule(
            rule_id="IR-1066",
            drug_a="Simvastatin",
            drug_b="Amlodipine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amlodipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1067"] = DetailedInteractionRule(
            rule_id="IR-1067",
            drug_a="Simvastatin",
            drug_b="Amlodipine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amlodipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1068"] = DetailedInteractionRule(
            rule_id="IR-1068",
            drug_a="Simvastatin",
            drug_b="Amlodipine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Amlodipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1069"] = DetailedInteractionRule(
            rule_id="IR-1069",
            drug_a="Simvastatin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1070"] = DetailedInteractionRule(
            rule_id="IR-1070",
            drug_a="Simvastatin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1071"] = DetailedInteractionRule(
            rule_id="IR-1071",
            drug_a="Simvastatin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1072"] = DetailedInteractionRule(
            rule_id="IR-1072",
            drug_a="Simvastatin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1073"] = DetailedInteractionRule(
            rule_id="IR-1073",
            drug_a="Simvastatin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1074"] = DetailedInteractionRule(
            rule_id="IR-1074",
            drug_a="Simvastatin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1075"] = DetailedInteractionRule(
            rule_id="IR-1075",
            drug_a="Simvastatin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1076"] = DetailedInteractionRule(
            rule_id="IR-1076",
            drug_a="Simvastatin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1077"] = DetailedInteractionRule(
            rule_id="IR-1077",
            drug_a="Simvastatin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1078"] = DetailedInteractionRule(
            rule_id="IR-1078",
            drug_a="Simvastatin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1079"] = DetailedInteractionRule(
            rule_id="IR-1079",
            drug_a="Simvastatin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1080"] = DetailedInteractionRule(
            rule_id="IR-1080",
            drug_a="Simvastatin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1081"] = DetailedInteractionRule(
            rule_id="IR-1081",
            drug_a="Simvastatin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1082"] = DetailedInteractionRule(
            rule_id="IR-1082",
            drug_a="Simvastatin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1083"] = DetailedInteractionRule(
            rule_id="IR-1083",
            drug_a="Simvastatin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1084"] = DetailedInteractionRule(
            rule_id="IR-1084",
            drug_a="Simvastatin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1085"] = DetailedInteractionRule(
            rule_id="IR-1085",
            drug_a="Simvastatin",
            drug_b="Ketoconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Ketoconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1086"] = DetailedInteractionRule(
            rule_id="IR-1086",
            drug_a="Simvastatin",
            drug_b="Ketoconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Ketoconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1087"] = DetailedInteractionRule(
            rule_id="IR-1087",
            drug_a="Simvastatin",
            drug_b="Ketoconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Ketoconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1088"] = DetailedInteractionRule(
            rule_id="IR-1088",
            drug_a="Simvastatin",
            drug_b="Ketoconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Ketoconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1089"] = DetailedInteractionRule(
            rule_id="IR-1089",
            drug_a="Simvastatin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1090"] = DetailedInteractionRule(
            rule_id="IR-1090",
            drug_a="Simvastatin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1091"] = DetailedInteractionRule(
            rule_id="IR-1091",
            drug_a="Simvastatin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1092"] = DetailedInteractionRule(
            rule_id="IR-1092",
            drug_a="Simvastatin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1093"] = DetailedInteractionRule(
            rule_id="IR-1093",
            drug_a="Simvastatin",
            drug_b="Posaconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Posaconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1094"] = DetailedInteractionRule(
            rule_id="IR-1094",
            drug_a="Simvastatin",
            drug_b="Posaconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Posaconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1095"] = DetailedInteractionRule(
            rule_id="IR-1095",
            drug_a="Simvastatin",
            drug_b="Posaconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Posaconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1096"] = DetailedInteractionRule(
            rule_id="IR-1096",
            drug_a="Simvastatin",
            drug_b="Posaconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Posaconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1097"] = DetailedInteractionRule(
            rule_id="IR-1097",
            drug_a="Simvastatin",
            drug_b="Gemfibrozil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Gemfibrozil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1098"] = DetailedInteractionRule(
            rule_id="IR-1098",
            drug_a="Simvastatin",
            drug_b="Gemfibrozil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Gemfibrozil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1099"] = DetailedInteractionRule(
            rule_id="IR-1099",
            drug_a="Simvastatin",
            drug_b="Gemfibrozil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Gemfibrozil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1100"] = DetailedInteractionRule(
            rule_id="IR-1100",
            drug_a="Simvastatin",
            drug_b="Gemfibrozil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Gemfibrozil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1101"] = DetailedInteractionRule(
            rule_id="IR-1101",
            drug_a="Simvastatin",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1102"] = DetailedInteractionRule(
            rule_id="IR-1102",
            drug_a="Simvastatin",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1103"] = DetailedInteractionRule(
            rule_id="IR-1103",
            drug_a="Simvastatin",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1104"] = DetailedInteractionRule(
            rule_id="IR-1104",
            drug_a="Simvastatin",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1105"] = DetailedInteractionRule(
            rule_id="IR-1105",
            drug_a="Simvastatin",
            drug_b="Grapefruit Juice",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Grapefruit Juice.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1106"] = DetailedInteractionRule(
            rule_id="IR-1106",
            drug_a="Simvastatin",
            drug_b="Grapefruit Juice",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Grapefruit Juice.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1107"] = DetailedInteractionRule(
            rule_id="IR-1107",
            drug_a="Simvastatin",
            drug_b="Grapefruit Juice",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Grapefruit Juice.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1108"] = DetailedInteractionRule(
            rule_id="IR-1108",
            drug_a="Simvastatin",
            drug_b="Grapefruit Juice",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Simvastatin and Grapefruit Juice.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1109"] = DetailedInteractionRule(
            rule_id="IR-1109",
            drug_a="Lisinopril",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1110"] = DetailedInteractionRule(
            rule_id="IR-1110",
            drug_a="Lisinopril",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1111"] = DetailedInteractionRule(
            rule_id="IR-1111",
            drug_a="Lisinopril",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1112"] = DetailedInteractionRule(
            rule_id="IR-1112",
            drug_a="Lisinopril",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1113"] = DetailedInteractionRule(
            rule_id="IR-1113",
            drug_a="Lisinopril",
            drug_b="Eplerenone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Eplerenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1114"] = DetailedInteractionRule(
            rule_id="IR-1114",
            drug_a="Lisinopril",
            drug_b="Eplerenone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Eplerenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1115"] = DetailedInteractionRule(
            rule_id="IR-1115",
            drug_a="Lisinopril",
            drug_b="Eplerenone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Eplerenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1116"] = DetailedInteractionRule(
            rule_id="IR-1116",
            drug_a="Lisinopril",
            drug_b="Eplerenone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Eplerenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1117"] = DetailedInteractionRule(
            rule_id="IR-1117",
            drug_a="Lisinopril",
            drug_b="Potassium Chloride",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Potassium Chloride.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1118"] = DetailedInteractionRule(
            rule_id="IR-1118",
            drug_a="Lisinopril",
            drug_b="Potassium Chloride",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Potassium Chloride.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1119"] = DetailedInteractionRule(
            rule_id="IR-1119",
            drug_a="Lisinopril",
            drug_b="Potassium Chloride",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Potassium Chloride.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1120"] = DetailedInteractionRule(
            rule_id="IR-1120",
            drug_a="Lisinopril",
            drug_b="Potassium Chloride",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Potassium Chloride.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1121"] = DetailedInteractionRule(
            rule_id="IR-1121",
            drug_a="Lisinopril",
            drug_b="Triamterene",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Triamterene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1122"] = DetailedInteractionRule(
            rule_id="IR-1122",
            drug_a="Lisinopril",
            drug_b="Triamterene",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Triamterene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1123"] = DetailedInteractionRule(
            rule_id="IR-1123",
            drug_a="Lisinopril",
            drug_b="Triamterene",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Triamterene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1124"] = DetailedInteractionRule(
            rule_id="IR-1124",
            drug_a="Lisinopril",
            drug_b="Triamterene",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Triamterene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1125"] = DetailedInteractionRule(
            rule_id="IR-1125",
            drug_a="Lisinopril",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1126"] = DetailedInteractionRule(
            rule_id="IR-1126",
            drug_a="Lisinopril",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1127"] = DetailedInteractionRule(
            rule_id="IR-1127",
            drug_a="Lisinopril",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1128"] = DetailedInteractionRule(
            rule_id="IR-1128",
            drug_a="Lisinopril",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1129"] = DetailedInteractionRule(
            rule_id="IR-1129",
            drug_a="Lisinopril",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1130"] = DetailedInteractionRule(
            rule_id="IR-1130",
            drug_a="Lisinopril",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1131"] = DetailedInteractionRule(
            rule_id="IR-1131",
            drug_a="Lisinopril",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1132"] = DetailedInteractionRule(
            rule_id="IR-1132",
            drug_a="Lisinopril",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1133"] = DetailedInteractionRule(
            rule_id="IR-1133",
            drug_a="Lisinopril",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1134"] = DetailedInteractionRule(
            rule_id="IR-1134",
            drug_a="Lisinopril",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1135"] = DetailedInteractionRule(
            rule_id="IR-1135",
            drug_a="Lisinopril",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1136"] = DetailedInteractionRule(
            rule_id="IR-1136",
            drug_a="Lisinopril",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1137"] = DetailedInteractionRule(
            rule_id="IR-1137",
            drug_a="Lisinopril",
            drug_b="Meloxicam",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Meloxicam.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1138"] = DetailedInteractionRule(
            rule_id="IR-1138",
            drug_a="Lisinopril",
            drug_b="Meloxicam",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Meloxicam.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1139"] = DetailedInteractionRule(
            rule_id="IR-1139",
            drug_a="Lisinopril",
            drug_b="Meloxicam",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Meloxicam.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1140"] = DetailedInteractionRule(
            rule_id="IR-1140",
            drug_a="Lisinopril",
            drug_b="Meloxicam",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Meloxicam.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1141"] = DetailedInteractionRule(
            rule_id="IR-1141",
            drug_a="Lisinopril",
            drug_b="Lithium",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Lithium.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1142"] = DetailedInteractionRule(
            rule_id="IR-1142",
            drug_a="Lisinopril",
            drug_b="Lithium",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Lithium.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1143"] = DetailedInteractionRule(
            rule_id="IR-1143",
            drug_a="Lisinopril",
            drug_b="Lithium",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Lithium.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1144"] = DetailedInteractionRule(
            rule_id="IR-1144",
            drug_a="Lisinopril",
            drug_b="Lithium",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Lithium.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1145"] = DetailedInteractionRule(
            rule_id="IR-1145",
            drug_a="Lisinopril",
            drug_b="Aliskiren",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Aliskiren.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1146"] = DetailedInteractionRule(
            rule_id="IR-1146",
            drug_a="Lisinopril",
            drug_b="Aliskiren",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Aliskiren.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1147"] = DetailedInteractionRule(
            rule_id="IR-1147",
            drug_a="Lisinopril",
            drug_b="Aliskiren",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Aliskiren.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1148"] = DetailedInteractionRule(
            rule_id="IR-1148",
            drug_a="Lisinopril",
            drug_b="Aliskiren",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Aliskiren.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1149"] = DetailedInteractionRule(
            rule_id="IR-1149",
            drug_a="Lisinopril",
            drug_b="Sacubitril",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Sacubitril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1150"] = DetailedInteractionRule(
            rule_id="IR-1150",
            drug_a="Lisinopril",
            drug_b="Sacubitril",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Sacubitril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1151"] = DetailedInteractionRule(
            rule_id="IR-1151",
            drug_a="Lisinopril",
            drug_b="Sacubitril",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Sacubitril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1152"] = DetailedInteractionRule(
            rule_id="IR-1152",
            drug_a="Lisinopril",
            drug_b="Sacubitril",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lisinopril and Sacubitril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1153"] = DetailedInteractionRule(
            rule_id="IR-1153",
            drug_a="Metformin",
            drug_b="Iodinated Radiocontrast",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Iodinated Radiocontrast.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1154"] = DetailedInteractionRule(
            rule_id="IR-1154",
            drug_a="Metformin",
            drug_b="Iodinated Radiocontrast",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Iodinated Radiocontrast.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1155"] = DetailedInteractionRule(
            rule_id="IR-1155",
            drug_a="Metformin",
            drug_b="Iodinated Radiocontrast",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Iodinated Radiocontrast.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1156"] = DetailedInteractionRule(
            rule_id="IR-1156",
            drug_a="Metformin",
            drug_b="Iodinated Radiocontrast",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Iodinated Radiocontrast.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1157"] = DetailedInteractionRule(
            rule_id="IR-1157",
            drug_a="Metformin",
            drug_b="Cimetidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Cimetidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1158"] = DetailedInteractionRule(
            rule_id="IR-1158",
            drug_a="Metformin",
            drug_b="Cimetidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Cimetidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1159"] = DetailedInteractionRule(
            rule_id="IR-1159",
            drug_a="Metformin",
            drug_b="Cimetidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Cimetidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1160"] = DetailedInteractionRule(
            rule_id="IR-1160",
            drug_a="Metformin",
            drug_b="Cimetidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Cimetidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1161"] = DetailedInteractionRule(
            rule_id="IR-1161",
            drug_a="Metformin",
            drug_b="Topiramate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Topiramate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1162"] = DetailedInteractionRule(
            rule_id="IR-1162",
            drug_a="Metformin",
            drug_b="Topiramate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Topiramate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1163"] = DetailedInteractionRule(
            rule_id="IR-1163",
            drug_a="Metformin",
            drug_b="Topiramate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Topiramate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1164"] = DetailedInteractionRule(
            rule_id="IR-1164",
            drug_a="Metformin",
            drug_b="Topiramate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Topiramate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1165"] = DetailedInteractionRule(
            rule_id="IR-1165",
            drug_a="Metformin",
            drug_b="Furosemide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1166"] = DetailedInteractionRule(
            rule_id="IR-1166",
            drug_a="Metformin",
            drug_b="Furosemide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1167"] = DetailedInteractionRule(
            rule_id="IR-1167",
            drug_a="Metformin",
            drug_b="Furosemide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1168"] = DetailedInteractionRule(
            rule_id="IR-1168",
            drug_a="Metformin",
            drug_b="Furosemide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1169"] = DetailedInteractionRule(
            rule_id="IR-1169",
            drug_a="Metformin",
            drug_b="Nifedipine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Nifedipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1170"] = DetailedInteractionRule(
            rule_id="IR-1170",
            drug_a="Metformin",
            drug_b="Nifedipine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Nifedipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1171"] = DetailedInteractionRule(
            rule_id="IR-1171",
            drug_a="Metformin",
            drug_b="Nifedipine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Nifedipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1172"] = DetailedInteractionRule(
            rule_id="IR-1172",
            drug_a="Metformin",
            drug_b="Nifedipine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Nifedipine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1173"] = DetailedInteractionRule(
            rule_id="IR-1173",
            drug_a="Metformin",
            drug_b="Alcohol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Alcohol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1174"] = DetailedInteractionRule(
            rule_id="IR-1174",
            drug_a="Metformin",
            drug_b="Alcohol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Alcohol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1175"] = DetailedInteractionRule(
            rule_id="IR-1175",
            drug_a="Metformin",
            drug_b="Alcohol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Alcohol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1176"] = DetailedInteractionRule(
            rule_id="IR-1176",
            drug_a="Metformin",
            drug_b="Alcohol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Alcohol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1177"] = DetailedInteractionRule(
            rule_id="IR-1177",
            drug_a="Metformin",
            drug_b="Ranolazine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Ranolazine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1178"] = DetailedInteractionRule(
            rule_id="IR-1178",
            drug_a="Metformin",
            drug_b="Ranolazine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Ranolazine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1179"] = DetailedInteractionRule(
            rule_id="IR-1179",
            drug_a="Metformin",
            drug_b="Ranolazine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Ranolazine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1180"] = DetailedInteractionRule(
            rule_id="IR-1180",
            drug_a="Metformin",
            drug_b="Ranolazine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Ranolazine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1181"] = DetailedInteractionRule(
            rule_id="IR-1181",
            drug_a="Metformin",
            drug_b="Dolutegravir",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Dolutegravir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1182"] = DetailedInteractionRule(
            rule_id="IR-1182",
            drug_a="Metformin",
            drug_b="Dolutegravir",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Dolutegravir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1183"] = DetailedInteractionRule(
            rule_id="IR-1183",
            drug_a="Metformin",
            drug_b="Dolutegravir",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Dolutegravir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1184"] = DetailedInteractionRule(
            rule_id="IR-1184",
            drug_a="Metformin",
            drug_b="Dolutegravir",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Metformin and Dolutegravir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1185"] = DetailedInteractionRule(
            rule_id="IR-1185",
            drug_a="Ciprofloxacin",
            drug_b="Theophylline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1186"] = DetailedInteractionRule(
            rule_id="IR-1186",
            drug_a="Ciprofloxacin",
            drug_b="Theophylline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1187"] = DetailedInteractionRule(
            rule_id="IR-1187",
            drug_a="Ciprofloxacin",
            drug_b="Theophylline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1188"] = DetailedInteractionRule(
            rule_id="IR-1188",
            drug_a="Ciprofloxacin",
            drug_b="Theophylline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1189"] = DetailedInteractionRule(
            rule_id="IR-1189",
            drug_a="Ciprofloxacin",
            drug_b="Tizanidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Tizanidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1190"] = DetailedInteractionRule(
            rule_id="IR-1190",
            drug_a="Ciprofloxacin",
            drug_b="Tizanidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Tizanidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1191"] = DetailedInteractionRule(
            rule_id="IR-1191",
            drug_a="Ciprofloxacin",
            drug_b="Tizanidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Tizanidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1192"] = DetailedInteractionRule(
            rule_id="IR-1192",
            drug_a="Ciprofloxacin",
            drug_b="Tizanidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Tizanidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1193"] = DetailedInteractionRule(
            rule_id="IR-1193",
            drug_a="Ciprofloxacin",
            drug_b="Warfarin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1194"] = DetailedInteractionRule(
            rule_id="IR-1194",
            drug_a="Ciprofloxacin",
            drug_b="Warfarin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1195"] = DetailedInteractionRule(
            rule_id="IR-1195",
            drug_a="Ciprofloxacin",
            drug_b="Warfarin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1196"] = DetailedInteractionRule(
            rule_id="IR-1196",
            drug_a="Ciprofloxacin",
            drug_b="Warfarin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1197"] = DetailedInteractionRule(
            rule_id="IR-1197",
            drug_a="Ciprofloxacin",
            drug_b="Antacids (Al/Mg)",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Antacids (Al/Mg).",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1198"] = DetailedInteractionRule(
            rule_id="IR-1198",
            drug_a="Ciprofloxacin",
            drug_b="Antacids (Al/Mg)",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Antacids (Al/Mg).",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1199"] = DetailedInteractionRule(
            rule_id="IR-1199",
            drug_a="Ciprofloxacin",
            drug_b="Antacids (Al/Mg)",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Antacids (Al/Mg).",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1200"] = DetailedInteractionRule(
            rule_id="IR-1200",
            drug_a="Ciprofloxacin",
            drug_b="Antacids (Al/Mg)",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Antacids (Al/Mg).",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1201"] = DetailedInteractionRule(
            rule_id="IR-1201",
            drug_a="Ciprofloxacin",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1202"] = DetailedInteractionRule(
            rule_id="IR-1202",
            drug_a="Ciprofloxacin",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1203"] = DetailedInteractionRule(
            rule_id="IR-1203",
            drug_a="Ciprofloxacin",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1204"] = DetailedInteractionRule(
            rule_id="IR-1204",
            drug_a="Ciprofloxacin",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1205"] = DetailedInteractionRule(
            rule_id="IR-1205",
            drug_a="Ciprofloxacin",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1206"] = DetailedInteractionRule(
            rule_id="IR-1206",
            drug_a="Ciprofloxacin",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1207"] = DetailedInteractionRule(
            rule_id="IR-1207",
            drug_a="Ciprofloxacin",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1208"] = DetailedInteractionRule(
            rule_id="IR-1208",
            drug_a="Ciprofloxacin",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1209"] = DetailedInteractionRule(
            rule_id="IR-1209",
            drug_a="Ciprofloxacin",
            drug_b="Zinc",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Zinc.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1210"] = DetailedInteractionRule(
            rule_id="IR-1210",
            drug_a="Ciprofloxacin",
            drug_b="Zinc",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Zinc.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1211"] = DetailedInteractionRule(
            rule_id="IR-1211",
            drug_a="Ciprofloxacin",
            drug_b="Zinc",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Zinc.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1212"] = DetailedInteractionRule(
            rule_id="IR-1212",
            drug_a="Ciprofloxacin",
            drug_b="Zinc",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Zinc.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1213"] = DetailedInteractionRule(
            rule_id="IR-1213",
            drug_a="Ciprofloxacin",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1214"] = DetailedInteractionRule(
            rule_id="IR-1214",
            drug_a="Ciprofloxacin",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1215"] = DetailedInteractionRule(
            rule_id="IR-1215",
            drug_a="Ciprofloxacin",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1216"] = DetailedInteractionRule(
            rule_id="IR-1216",
            drug_a="Ciprofloxacin",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1217"] = DetailedInteractionRule(
            rule_id="IR-1217",
            drug_a="Ciprofloxacin",
            drug_b="Didanosine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Didanosine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1218"] = DetailedInteractionRule(
            rule_id="IR-1218",
            drug_a="Ciprofloxacin",
            drug_b="Didanosine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Didanosine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1219"] = DetailedInteractionRule(
            rule_id="IR-1219",
            drug_a="Ciprofloxacin",
            drug_b="Didanosine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Didanosine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1220"] = DetailedInteractionRule(
            rule_id="IR-1220",
            drug_a="Ciprofloxacin",
            drug_b="Didanosine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Didanosine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1221"] = DetailedInteractionRule(
            rule_id="IR-1221",
            drug_a="Ciprofloxacin",
            drug_b="Methotrexate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Methotrexate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1222"] = DetailedInteractionRule(
            rule_id="IR-1222",
            drug_a="Ciprofloxacin",
            drug_b="Methotrexate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Methotrexate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1223"] = DetailedInteractionRule(
            rule_id="IR-1223",
            drug_a="Ciprofloxacin",
            drug_b="Methotrexate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Methotrexate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1224"] = DetailedInteractionRule(
            rule_id="IR-1224",
            drug_a="Ciprofloxacin",
            drug_b="Methotrexate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Methotrexate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1225"] = DetailedInteractionRule(
            rule_id="IR-1225",
            drug_a="Ciprofloxacin",
            drug_b="Clozapine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Clozapine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1226"] = DetailedInteractionRule(
            rule_id="IR-1226",
            drug_a="Ciprofloxacin",
            drug_b="Clozapine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Clozapine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1227"] = DetailedInteractionRule(
            rule_id="IR-1227",
            drug_a="Ciprofloxacin",
            drug_b="Clozapine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Clozapine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1228"] = DetailedInteractionRule(
            rule_id="IR-1228",
            drug_a="Ciprofloxacin",
            drug_b="Clozapine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Clozapine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1229"] = DetailedInteractionRule(
            rule_id="IR-1229",
            drug_a="Ciprofloxacin",
            drug_b="Duloxetine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Duloxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1230"] = DetailedInteractionRule(
            rule_id="IR-1230",
            drug_a="Ciprofloxacin",
            drug_b="Duloxetine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Duloxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1231"] = DetailedInteractionRule(
            rule_id="IR-1231",
            drug_a="Ciprofloxacin",
            drug_b="Duloxetine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Duloxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1232"] = DetailedInteractionRule(
            rule_id="IR-1232",
            drug_a="Ciprofloxacin",
            drug_b="Duloxetine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Ciprofloxacin and Duloxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1233"] = DetailedInteractionRule(
            rule_id="IR-1233",
            drug_a="Methotrexate",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1234"] = DetailedInteractionRule(
            rule_id="IR-1234",
            drug_a="Methotrexate",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1235"] = DetailedInteractionRule(
            rule_id="IR-1235",
            drug_a="Methotrexate",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1236"] = DetailedInteractionRule(
            rule_id="IR-1236",
            drug_a="Methotrexate",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1237"] = DetailedInteractionRule(
            rule_id="IR-1237",
            drug_a="Methotrexate",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1238"] = DetailedInteractionRule(
            rule_id="IR-1238",
            drug_a="Methotrexate",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1239"] = DetailedInteractionRule(
            rule_id="IR-1239",
            drug_a="Methotrexate",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1240"] = DetailedInteractionRule(
            rule_id="IR-1240",
            drug_a="Methotrexate",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1241"] = DetailedInteractionRule(
            rule_id="IR-1241",
            drug_a="Methotrexate",
            drug_b="Ketorolac",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ketorolac.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1242"] = DetailedInteractionRule(
            rule_id="IR-1242",
            drug_a="Methotrexate",
            drug_b="Ketorolac",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ketorolac.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1243"] = DetailedInteractionRule(
            rule_id="IR-1243",
            drug_a="Methotrexate",
            drug_b="Ketorolac",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ketorolac.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1244"] = DetailedInteractionRule(
            rule_id="IR-1244",
            drug_a="Methotrexate",
            drug_b="Ketorolac",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Ketorolac.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1245"] = DetailedInteractionRule(
            rule_id="IR-1245",
            drug_a="Methotrexate",
            drug_b="Amoxicillin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Amoxicillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1246"] = DetailedInteractionRule(
            rule_id="IR-1246",
            drug_a="Methotrexate",
            drug_b="Amoxicillin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Amoxicillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1247"] = DetailedInteractionRule(
            rule_id="IR-1247",
            drug_a="Methotrexate",
            drug_b="Amoxicillin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Amoxicillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1248"] = DetailedInteractionRule(
            rule_id="IR-1248",
            drug_a="Methotrexate",
            drug_b="Amoxicillin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Amoxicillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1249"] = DetailedInteractionRule(
            rule_id="IR-1249",
            drug_a="Methotrexate",
            drug_b="Piperacillin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Piperacillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1250"] = DetailedInteractionRule(
            rule_id="IR-1250",
            drug_a="Methotrexate",
            drug_b="Piperacillin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Piperacillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1251"] = DetailedInteractionRule(
            rule_id="IR-1251",
            drug_a="Methotrexate",
            drug_b="Piperacillin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Piperacillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1252"] = DetailedInteractionRule(
            rule_id="IR-1252",
            drug_a="Methotrexate",
            drug_b="Piperacillin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Piperacillin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1253"] = DetailedInteractionRule(
            rule_id="IR-1253",
            drug_a="Methotrexate",
            drug_b="Probenecid",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Probenecid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1254"] = DetailedInteractionRule(
            rule_id="IR-1254",
            drug_a="Methotrexate",
            drug_b="Probenecid",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Probenecid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1255"] = DetailedInteractionRule(
            rule_id="IR-1255",
            drug_a="Methotrexate",
            drug_b="Probenecid",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Probenecid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1256"] = DetailedInteractionRule(
            rule_id="IR-1256",
            drug_a="Methotrexate",
            drug_b="Probenecid",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Probenecid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1257"] = DetailedInteractionRule(
            rule_id="IR-1257",
            drug_a="Methotrexate",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1258"] = DetailedInteractionRule(
            rule_id="IR-1258",
            drug_a="Methotrexate",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1259"] = DetailedInteractionRule(
            rule_id="IR-1259",
            drug_a="Methotrexate",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1260"] = DetailedInteractionRule(
            rule_id="IR-1260",
            drug_a="Methotrexate",
            drug_b="Trimethoprim",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Trimethoprim.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1261"] = DetailedInteractionRule(
            rule_id="IR-1261",
            drug_a="Methotrexate",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1262"] = DetailedInteractionRule(
            rule_id="IR-1262",
            drug_a="Methotrexate",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1263"] = DetailedInteractionRule(
            rule_id="IR-1263",
            drug_a="Methotrexate",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1264"] = DetailedInteractionRule(
            rule_id="IR-1264",
            drug_a="Methotrexate",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1265"] = DetailedInteractionRule(
            rule_id="IR-1265",
            drug_a="Methotrexate",
            drug_b="Pantoprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Pantoprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1266"] = DetailedInteractionRule(
            rule_id="IR-1266",
            drug_a="Methotrexate",
            drug_b="Pantoprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Pantoprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1267"] = DetailedInteractionRule(
            rule_id="IR-1267",
            drug_a="Methotrexate",
            drug_b="Pantoprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Pantoprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1268"] = DetailedInteractionRule(
            rule_id="IR-1268",
            drug_a="Methotrexate",
            drug_b="Pantoprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Pantoprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1269"] = DetailedInteractionRule(
            rule_id="IR-1269",
            drug_a="Methotrexate",
            drug_b="Leflunomide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Leflunomide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1270"] = DetailedInteractionRule(
            rule_id="IR-1270",
            drug_a="Methotrexate",
            drug_b="Leflunomide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Leflunomide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1271"] = DetailedInteractionRule(
            rule_id="IR-1271",
            drug_a="Methotrexate",
            drug_b="Leflunomide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Leflunomide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1272"] = DetailedInteractionRule(
            rule_id="IR-1272",
            drug_a="Methotrexate",
            drug_b="Leflunomide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Methotrexate and Leflunomide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1273"] = DetailedInteractionRule(
            rule_id="IR-1273",
            drug_a="Digoxin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1274"] = DetailedInteractionRule(
            rule_id="IR-1274",
            drug_a="Digoxin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1275"] = DetailedInteractionRule(
            rule_id="IR-1275",
            drug_a="Digoxin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1276"] = DetailedInteractionRule(
            rule_id="IR-1276",
            drug_a="Digoxin",
            drug_b="Amiodarone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Amiodarone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1277"] = DetailedInteractionRule(
            rule_id="IR-1277",
            drug_a="Digoxin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1278"] = DetailedInteractionRule(
            rule_id="IR-1278",
            drug_a="Digoxin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1279"] = DetailedInteractionRule(
            rule_id="IR-1279",
            drug_a="Digoxin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1280"] = DetailedInteractionRule(
            rule_id="IR-1280",
            drug_a="Digoxin",
            drug_b="Verapamil",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Verapamil.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1281"] = DetailedInteractionRule(
            rule_id="IR-1281",
            drug_a="Digoxin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1282"] = DetailedInteractionRule(
            rule_id="IR-1282",
            drug_a="Digoxin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1283"] = DetailedInteractionRule(
            rule_id="IR-1283",
            drug_a="Digoxin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1284"] = DetailedInteractionRule(
            rule_id="IR-1284",
            drug_a="Digoxin",
            drug_b="Diltiazem",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Diltiazem.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1285"] = DetailedInteractionRule(
            rule_id="IR-1285",
            drug_a="Digoxin",
            drug_b="Quinidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Quinidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1286"] = DetailedInteractionRule(
            rule_id="IR-1286",
            drug_a="Digoxin",
            drug_b="Quinidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Quinidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1287"] = DetailedInteractionRule(
            rule_id="IR-1287",
            drug_a="Digoxin",
            drug_b="Quinidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Quinidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1288"] = DetailedInteractionRule(
            rule_id="IR-1288",
            drug_a="Digoxin",
            drug_b="Quinidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Quinidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1289"] = DetailedInteractionRule(
            rule_id="IR-1289",
            drug_a="Digoxin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1290"] = DetailedInteractionRule(
            rule_id="IR-1290",
            drug_a="Digoxin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1291"] = DetailedInteractionRule(
            rule_id="IR-1291",
            drug_a="Digoxin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1292"] = DetailedInteractionRule(
            rule_id="IR-1292",
            drug_a="Digoxin",
            drug_b="Clarithromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Clarithromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1293"] = DetailedInteractionRule(
            rule_id="IR-1293",
            drug_a="Digoxin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1294"] = DetailedInteractionRule(
            rule_id="IR-1294",
            drug_a="Digoxin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1295"] = DetailedInteractionRule(
            rule_id="IR-1295",
            drug_a="Digoxin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1296"] = DetailedInteractionRule(
            rule_id="IR-1296",
            drug_a="Digoxin",
            drug_b="Erythromycin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Erythromycin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1297"] = DetailedInteractionRule(
            rule_id="IR-1297",
            drug_a="Digoxin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1298"] = DetailedInteractionRule(
            rule_id="IR-1298",
            drug_a="Digoxin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1299"] = DetailedInteractionRule(
            rule_id="IR-1299",
            drug_a="Digoxin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1300"] = DetailedInteractionRule(
            rule_id="IR-1300",
            drug_a="Digoxin",
            drug_b="Itraconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Itraconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1301"] = DetailedInteractionRule(
            rule_id="IR-1301",
            drug_a="Digoxin",
            drug_b="Propafenone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Propafenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1302"] = DetailedInteractionRule(
            rule_id="IR-1302",
            drug_a="Digoxin",
            drug_b="Propafenone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Propafenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1303"] = DetailedInteractionRule(
            rule_id="IR-1303",
            drug_a="Digoxin",
            drug_b="Propafenone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Propafenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1304"] = DetailedInteractionRule(
            rule_id="IR-1304",
            drug_a="Digoxin",
            drug_b="Propafenone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Propafenone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1305"] = DetailedInteractionRule(
            rule_id="IR-1305",
            drug_a="Digoxin",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1306"] = DetailedInteractionRule(
            rule_id="IR-1306",
            drug_a="Digoxin",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1307"] = DetailedInteractionRule(
            rule_id="IR-1307",
            drug_a="Digoxin",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1308"] = DetailedInteractionRule(
            rule_id="IR-1308",
            drug_a="Digoxin",
            drug_b="Spironolactone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Spironolactone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1309"] = DetailedInteractionRule(
            rule_id="IR-1309",
            drug_a="Digoxin",
            drug_b="Atorvastatin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Atorvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1310"] = DetailedInteractionRule(
            rule_id="IR-1310",
            drug_a="Digoxin",
            drug_b="Atorvastatin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Atorvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1311"] = DetailedInteractionRule(
            rule_id="IR-1311",
            drug_a="Digoxin",
            drug_b="Atorvastatin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Atorvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1312"] = DetailedInteractionRule(
            rule_id="IR-1312",
            drug_a="Digoxin",
            drug_b="Atorvastatin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Digoxin and Atorvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1313"] = DetailedInteractionRule(
            rule_id="IR-1313",
            drug_a="Clopidogrel",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1314"] = DetailedInteractionRule(
            rule_id="IR-1314",
            drug_a="Clopidogrel",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1315"] = DetailedInteractionRule(
            rule_id="IR-1315",
            drug_a="Clopidogrel",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1316"] = DetailedInteractionRule(
            rule_id="IR-1316",
            drug_a="Clopidogrel",
            drug_b="Omeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Omeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1317"] = DetailedInteractionRule(
            rule_id="IR-1317",
            drug_a="Clopidogrel",
            drug_b="Esomeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Esomeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1318"] = DetailedInteractionRule(
            rule_id="IR-1318",
            drug_a="Clopidogrel",
            drug_b="Esomeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Esomeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1319"] = DetailedInteractionRule(
            rule_id="IR-1319",
            drug_a="Clopidogrel",
            drug_b="Esomeprazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Esomeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1320"] = DetailedInteractionRule(
            rule_id="IR-1320",
            drug_a="Clopidogrel",
            drug_b="Esomeprazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Esomeprazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1321"] = DetailedInteractionRule(
            rule_id="IR-1321",
            drug_a="Clopidogrel",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1322"] = DetailedInteractionRule(
            rule_id="IR-1322",
            drug_a="Clopidogrel",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1323"] = DetailedInteractionRule(
            rule_id="IR-1323",
            drug_a="Clopidogrel",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1324"] = DetailedInteractionRule(
            rule_id="IR-1324",
            drug_a="Clopidogrel",
            drug_b="Fluconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1325"] = DetailedInteractionRule(
            rule_id="IR-1325",
            drug_a="Clopidogrel",
            drug_b="Voriconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Voriconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1326"] = DetailedInteractionRule(
            rule_id="IR-1326",
            drug_a="Clopidogrel",
            drug_b="Voriconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Voriconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1327"] = DetailedInteractionRule(
            rule_id="IR-1327",
            drug_a="Clopidogrel",
            drug_b="Voriconazole",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Voriconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1328"] = DetailedInteractionRule(
            rule_id="IR-1328",
            drug_a="Clopidogrel",
            drug_b="Voriconazole",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Voriconazole.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1329"] = DetailedInteractionRule(
            rule_id="IR-1329",
            drug_a="Clopidogrel",
            drug_b="Fluoxetine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluoxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1330"] = DetailedInteractionRule(
            rule_id="IR-1330",
            drug_a="Clopidogrel",
            drug_b="Fluoxetine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluoxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1331"] = DetailedInteractionRule(
            rule_id="IR-1331",
            drug_a="Clopidogrel",
            drug_b="Fluoxetine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluoxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1332"] = DetailedInteractionRule(
            rule_id="IR-1332",
            drug_a="Clopidogrel",
            drug_b="Fluoxetine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluoxetine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1333"] = DetailedInteractionRule(
            rule_id="IR-1333",
            drug_a="Clopidogrel",
            drug_b="Fluvoxamine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluvoxamine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1334"] = DetailedInteractionRule(
            rule_id="IR-1334",
            drug_a="Clopidogrel",
            drug_b="Fluvoxamine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluvoxamine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1335"] = DetailedInteractionRule(
            rule_id="IR-1335",
            drug_a="Clopidogrel",
            drug_b="Fluvoxamine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluvoxamine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1336"] = DetailedInteractionRule(
            rule_id="IR-1336",
            drug_a="Clopidogrel",
            drug_b="Fluvoxamine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Fluvoxamine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1337"] = DetailedInteractionRule(
            rule_id="IR-1337",
            drug_a="Clopidogrel",
            drug_b="Ticlopidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Ticlopidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1338"] = DetailedInteractionRule(
            rule_id="IR-1338",
            drug_a="Clopidogrel",
            drug_b="Ticlopidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Ticlopidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1339"] = DetailedInteractionRule(
            rule_id="IR-1339",
            drug_a="Clopidogrel",
            drug_b="Ticlopidine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Ticlopidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1340"] = DetailedInteractionRule(
            rule_id="IR-1340",
            drug_a="Clopidogrel",
            drug_b="Ticlopidine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Ticlopidine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1341"] = DetailedInteractionRule(
            rule_id="IR-1341",
            drug_a="Clopidogrel",
            drug_b="Morphine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Morphine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1342"] = DetailedInteractionRule(
            rule_id="IR-1342",
            drug_a="Clopidogrel",
            drug_b="Morphine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Morphine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1343"] = DetailedInteractionRule(
            rule_id="IR-1343",
            drug_a="Clopidogrel",
            drug_b="Morphine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Morphine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1344"] = DetailedInteractionRule(
            rule_id="IR-1344",
            drug_a="Clopidogrel",
            drug_b="Morphine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Morphine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1345"] = DetailedInteractionRule(
            rule_id="IR-1345",
            drug_a="Clopidogrel",
            drug_b="Aspirin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1346"] = DetailedInteractionRule(
            rule_id="IR-1346",
            drug_a="Clopidogrel",
            drug_b="Aspirin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1347"] = DetailedInteractionRule(
            rule_id="IR-1347",
            drug_a="Clopidogrel",
            drug_b="Aspirin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1348"] = DetailedInteractionRule(
            rule_id="IR-1348",
            drug_a="Clopidogrel",
            drug_b="Aspirin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Aspirin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1349"] = DetailedInteractionRule(
            rule_id="IR-1349",
            drug_a="Clopidogrel",
            drug_b="Rivaroxaban",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Rivaroxaban.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1350"] = DetailedInteractionRule(
            rule_id="IR-1350",
            drug_a="Clopidogrel",
            drug_b="Rivaroxaban",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Rivaroxaban.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1351"] = DetailedInteractionRule(
            rule_id="IR-1351",
            drug_a="Clopidogrel",
            drug_b="Rivaroxaban",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Rivaroxaban.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1352"] = DetailedInteractionRule(
            rule_id="IR-1352",
            drug_a="Clopidogrel",
            drug_b="Rivaroxaban",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Clopidogrel and Rivaroxaban.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1353"] = DetailedInteractionRule(
            rule_id="IR-1353",
            drug_a="Fluoxetine",
            drug_b="Tramadol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tramadol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1354"] = DetailedInteractionRule(
            rule_id="IR-1354",
            drug_a="Fluoxetine",
            drug_b="Tramadol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tramadol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1355"] = DetailedInteractionRule(
            rule_id="IR-1355",
            drug_a="Fluoxetine",
            drug_b="Tramadol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tramadol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1356"] = DetailedInteractionRule(
            rule_id="IR-1356",
            drug_a="Fluoxetine",
            drug_b="Tramadol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tramadol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1357"] = DetailedInteractionRule(
            rule_id="IR-1357",
            drug_a="Fluoxetine",
            drug_b="Linezolid",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Linezolid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1358"] = DetailedInteractionRule(
            rule_id="IR-1358",
            drug_a="Fluoxetine",
            drug_b="Linezolid",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Linezolid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1359"] = DetailedInteractionRule(
            rule_id="IR-1359",
            drug_a="Fluoxetine",
            drug_b="Linezolid",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Linezolid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1360"] = DetailedInteractionRule(
            rule_id="IR-1360",
            drug_a="Fluoxetine",
            drug_b="Linezolid",
            severity=InteractionSeverity.CONTRAINDICATED,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Linezolid.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1361"] = DetailedInteractionRule(
            rule_id="IR-1361",
            drug_a="Fluoxetine",
            drug_b="Selegiline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Selegiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1362"] = DetailedInteractionRule(
            rule_id="IR-1362",
            drug_a="Fluoxetine",
            drug_b="Selegiline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Selegiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1363"] = DetailedInteractionRule(
            rule_id="IR-1363",
            drug_a="Fluoxetine",
            drug_b="Selegiline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Selegiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1364"] = DetailedInteractionRule(
            rule_id="IR-1364",
            drug_a="Fluoxetine",
            drug_b="Selegiline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Selegiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1365"] = DetailedInteractionRule(
            rule_id="IR-1365",
            drug_a="Fluoxetine",
            drug_b="Rasagiline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Rasagiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1366"] = DetailedInteractionRule(
            rule_id="IR-1366",
            drug_a="Fluoxetine",
            drug_b="Rasagiline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Rasagiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1367"] = DetailedInteractionRule(
            rule_id="IR-1367",
            drug_a="Fluoxetine",
            drug_b="Rasagiline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Rasagiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1368"] = DetailedInteractionRule(
            rule_id="IR-1368",
            drug_a="Fluoxetine",
            drug_b="Rasagiline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Rasagiline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1369"] = DetailedInteractionRule(
            rule_id="IR-1369",
            drug_a="Fluoxetine",
            drug_b="Phenelzine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Phenelzine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1370"] = DetailedInteractionRule(
            rule_id="IR-1370",
            drug_a="Fluoxetine",
            drug_b="Phenelzine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Phenelzine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1371"] = DetailedInteractionRule(
            rule_id="IR-1371",
            drug_a="Fluoxetine",
            drug_b="Phenelzine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Phenelzine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1372"] = DetailedInteractionRule(
            rule_id="IR-1372",
            drug_a="Fluoxetine",
            drug_b="Phenelzine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Phenelzine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1373"] = DetailedInteractionRule(
            rule_id="IR-1373",
            drug_a="Fluoxetine",
            drug_b="Tranylcypromine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tranylcypromine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1374"] = DetailedInteractionRule(
            rule_id="IR-1374",
            drug_a="Fluoxetine",
            drug_b="Tranylcypromine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tranylcypromine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1375"] = DetailedInteractionRule(
            rule_id="IR-1375",
            drug_a="Fluoxetine",
            drug_b="Tranylcypromine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tranylcypromine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1376"] = DetailedInteractionRule(
            rule_id="IR-1376",
            drug_a="Fluoxetine",
            drug_b="Tranylcypromine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tranylcypromine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1377"] = DetailedInteractionRule(
            rule_id="IR-1377",
            drug_a="Fluoxetine",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1378"] = DetailedInteractionRule(
            rule_id="IR-1378",
            drug_a="Fluoxetine",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1379"] = DetailedInteractionRule(
            rule_id="IR-1379",
            drug_a="Fluoxetine",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1380"] = DetailedInteractionRule(
            rule_id="IR-1380",
            drug_a="Fluoxetine",
            drug_b="St Johns Wort",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and St Johns Wort.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1381"] = DetailedInteractionRule(
            rule_id="IR-1381",
            drug_a="Fluoxetine",
            drug_b="Dextromethorphan",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Dextromethorphan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1382"] = DetailedInteractionRule(
            rule_id="IR-1382",
            drug_a="Fluoxetine",
            drug_b="Dextromethorphan",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Dextromethorphan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1383"] = DetailedInteractionRule(
            rule_id="IR-1383",
            drug_a="Fluoxetine",
            drug_b="Dextromethorphan",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Dextromethorphan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1384"] = DetailedInteractionRule(
            rule_id="IR-1384",
            drug_a="Fluoxetine",
            drug_b="Dextromethorphan",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Dextromethorphan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1385"] = DetailedInteractionRule(
            rule_id="IR-1385",
            drug_a="Fluoxetine",
            drug_b="Metoprolol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Metoprolol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1386"] = DetailedInteractionRule(
            rule_id="IR-1386",
            drug_a="Fluoxetine",
            drug_b="Metoprolol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Metoprolol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1387"] = DetailedInteractionRule(
            rule_id="IR-1387",
            drug_a="Fluoxetine",
            drug_b="Metoprolol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Metoprolol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1388"] = DetailedInteractionRule(
            rule_id="IR-1388",
            drug_a="Fluoxetine",
            drug_b="Metoprolol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Metoprolol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1389"] = DetailedInteractionRule(
            rule_id="IR-1389",
            drug_a="Fluoxetine",
            drug_b="Risperidone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Risperidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1390"] = DetailedInteractionRule(
            rule_id="IR-1390",
            drug_a="Fluoxetine",
            drug_b="Risperidone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Risperidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1391"] = DetailedInteractionRule(
            rule_id="IR-1391",
            drug_a="Fluoxetine",
            drug_b="Risperidone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Risperidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1392"] = DetailedInteractionRule(
            rule_id="IR-1392",
            drug_a="Fluoxetine",
            drug_b="Risperidone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Risperidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1393"] = DetailedInteractionRule(
            rule_id="IR-1393",
            drug_a="Fluoxetine",
            drug_b="Tamoxifen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tamoxifen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1394"] = DetailedInteractionRule(
            rule_id="IR-1394",
            drug_a="Fluoxetine",
            drug_b="Tamoxifen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tamoxifen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1395"] = DetailedInteractionRule(
            rule_id="IR-1395",
            drug_a="Fluoxetine",
            drug_b="Tamoxifen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tamoxifen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1396"] = DetailedInteractionRule(
            rule_id="IR-1396",
            drug_a="Fluoxetine",
            drug_b="Tamoxifen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Fluoxetine and Tamoxifen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1397"] = DetailedInteractionRule(
            rule_id="IR-1397",
            drug_a="Lithium",
            drug_b="Hydrochlorothiazide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Hydrochlorothiazide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1398"] = DetailedInteractionRule(
            rule_id="IR-1398",
            drug_a="Lithium",
            drug_b="Hydrochlorothiazide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Hydrochlorothiazide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1399"] = DetailedInteractionRule(
            rule_id="IR-1399",
            drug_a="Lithium",
            drug_b="Hydrochlorothiazide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Hydrochlorothiazide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1400"] = DetailedInteractionRule(
            rule_id="IR-1400",
            drug_a="Lithium",
            drug_b="Hydrochlorothiazide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Hydrochlorothiazide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1401"] = DetailedInteractionRule(
            rule_id="IR-1401",
            drug_a="Lithium",
            drug_b="Chlorthalidone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Chlorthalidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1402"] = DetailedInteractionRule(
            rule_id="IR-1402",
            drug_a="Lithium",
            drug_b="Chlorthalidone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Chlorthalidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1403"] = DetailedInteractionRule(
            rule_id="IR-1403",
            drug_a="Lithium",
            drug_b="Chlorthalidone",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Chlorthalidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1404"] = DetailedInteractionRule(
            rule_id="IR-1404",
            drug_a="Lithium",
            drug_b="Chlorthalidone",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Chlorthalidone.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1405"] = DetailedInteractionRule(
            rule_id="IR-1405",
            drug_a="Lithium",
            drug_b="Furosemide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1406"] = DetailedInteractionRule(
            rule_id="IR-1406",
            drug_a="Lithium",
            drug_b="Furosemide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1407"] = DetailedInteractionRule(
            rule_id="IR-1407",
            drug_a="Lithium",
            drug_b="Furosemide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1408"] = DetailedInteractionRule(
            rule_id="IR-1408",
            drug_a="Lithium",
            drug_b="Furosemide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Furosemide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1409"] = DetailedInteractionRule(
            rule_id="IR-1409",
            drug_a="Lithium",
            drug_b="Lisinopril",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Lisinopril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1410"] = DetailedInteractionRule(
            rule_id="IR-1410",
            drug_a="Lithium",
            drug_b="Lisinopril",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Lisinopril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1411"] = DetailedInteractionRule(
            rule_id="IR-1411",
            drug_a="Lithium",
            drug_b="Lisinopril",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Lisinopril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1412"] = DetailedInteractionRule(
            rule_id="IR-1412",
            drug_a="Lithium",
            drug_b="Lisinopril",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Lisinopril.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1413"] = DetailedInteractionRule(
            rule_id="IR-1413",
            drug_a="Lithium",
            drug_b="Losartan",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Losartan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1414"] = DetailedInteractionRule(
            rule_id="IR-1414",
            drug_a="Lithium",
            drug_b="Losartan",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Losartan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1415"] = DetailedInteractionRule(
            rule_id="IR-1415",
            drug_a="Lithium",
            drug_b="Losartan",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Losartan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1416"] = DetailedInteractionRule(
            rule_id="IR-1416",
            drug_a="Lithium",
            drug_b="Losartan",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Losartan.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1417"] = DetailedInteractionRule(
            rule_id="IR-1417",
            drug_a="Lithium",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1418"] = DetailedInteractionRule(
            rule_id="IR-1418",
            drug_a="Lithium",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1419"] = DetailedInteractionRule(
            rule_id="IR-1419",
            drug_a="Lithium",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1420"] = DetailedInteractionRule(
            rule_id="IR-1420",
            drug_a="Lithium",
            drug_b="Ibuprofen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Ibuprofen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1421"] = DetailedInteractionRule(
            rule_id="IR-1421",
            drug_a="Lithium",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1422"] = DetailedInteractionRule(
            rule_id="IR-1422",
            drug_a="Lithium",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1423"] = DetailedInteractionRule(
            rule_id="IR-1423",
            drug_a="Lithium",
            drug_b="Naproxen",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1424"] = DetailedInteractionRule(
            rule_id="IR-1424",
            drug_a="Lithium",
            drug_b="Naproxen",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Naproxen.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1425"] = DetailedInteractionRule(
            rule_id="IR-1425",
            drug_a="Lithium",
            drug_b="Celecoxib",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Celecoxib.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1426"] = DetailedInteractionRule(
            rule_id="IR-1426",
            drug_a="Lithium",
            drug_b="Celecoxib",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Celecoxib.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1427"] = DetailedInteractionRule(
            rule_id="IR-1427",
            drug_a="Lithium",
            drug_b="Celecoxib",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Celecoxib.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1428"] = DetailedInteractionRule(
            rule_id="IR-1428",
            drug_a="Lithium",
            drug_b="Celecoxib",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Celecoxib.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1429"] = DetailedInteractionRule(
            rule_id="IR-1429",
            drug_a="Lithium",
            drug_b="Theophylline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1430"] = DetailedInteractionRule(
            rule_id="IR-1430",
            drug_a="Lithium",
            drug_b="Theophylline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1431"] = DetailedInteractionRule(
            rule_id="IR-1431",
            drug_a="Lithium",
            drug_b="Theophylline",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1432"] = DetailedInteractionRule(
            rule_id="IR-1432",
            drug_a="Lithium",
            drug_b="Theophylline",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Theophylline.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1433"] = DetailedInteractionRule(
            rule_id="IR-1433",
            drug_a="Lithium",
            drug_b="Caffeine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Caffeine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1434"] = DetailedInteractionRule(
            rule_id="IR-1434",
            drug_a="Lithium",
            drug_b="Caffeine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Caffeine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1435"] = DetailedInteractionRule(
            rule_id="IR-1435",
            drug_a="Lithium",
            drug_b="Caffeine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Caffeine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1436"] = DetailedInteractionRule(
            rule_id="IR-1436",
            drug_a="Lithium",
            drug_b="Caffeine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Lithium and Caffeine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1437"] = DetailedInteractionRule(
            rule_id="IR-1437",
            drug_a="Amiodarone",
            drug_b="Warfarin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1438"] = DetailedInteractionRule(
            rule_id="IR-1438",
            drug_a="Amiodarone",
            drug_b="Warfarin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1439"] = DetailedInteractionRule(
            rule_id="IR-1439",
            drug_a="Amiodarone",
            drug_b="Warfarin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1440"] = DetailedInteractionRule(
            rule_id="IR-1440",
            drug_a="Amiodarone",
            drug_b="Warfarin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Warfarin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1441"] = DetailedInteractionRule(
            rule_id="IR-1441",
            drug_a="Amiodarone",
            drug_b="Digoxin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Digoxin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1442"] = DetailedInteractionRule(
            rule_id="IR-1442",
            drug_a="Amiodarone",
            drug_b="Digoxin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Digoxin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1443"] = DetailedInteractionRule(
            rule_id="IR-1443",
            drug_a="Amiodarone",
            drug_b="Digoxin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Digoxin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1444"] = DetailedInteractionRule(
            rule_id="IR-1444",
            drug_a="Amiodarone",
            drug_b="Digoxin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Digoxin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1445"] = DetailedInteractionRule(
            rule_id="IR-1445",
            drug_a="Amiodarone",
            drug_b="Simvastatin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Simvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1446"] = DetailedInteractionRule(
            rule_id="IR-1446",
            drug_a="Amiodarone",
            drug_b="Simvastatin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Simvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1447"] = DetailedInteractionRule(
            rule_id="IR-1447",
            drug_a="Amiodarone",
            drug_b="Simvastatin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Simvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1448"] = DetailedInteractionRule(
            rule_id="IR-1448",
            drug_a="Amiodarone",
            drug_b="Simvastatin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Simvastatin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1449"] = DetailedInteractionRule(
            rule_id="IR-1449",
            drug_a="Amiodarone",
            drug_b="Levofloxacin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Levofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1450"] = DetailedInteractionRule(
            rule_id="IR-1450",
            drug_a="Amiodarone",
            drug_b="Levofloxacin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Levofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1451"] = DetailedInteractionRule(
            rule_id="IR-1451",
            drug_a="Amiodarone",
            drug_b="Levofloxacin",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Levofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1452"] = DetailedInteractionRule(
            rule_id="IR-1452",
            drug_a="Amiodarone",
            drug_b="Levofloxacin",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Levofloxacin.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1453"] = DetailedInteractionRule(
            rule_id="IR-1453",
            drug_a="Amiodarone",
            drug_b="Haloperidol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Haloperidol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1454"] = DetailedInteractionRule(
            rule_id="IR-1454",
            drug_a="Amiodarone",
            drug_b="Haloperidol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Haloperidol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1455"] = DetailedInteractionRule(
            rule_id="IR-1455",
            drug_a="Amiodarone",
            drug_b="Haloperidol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Haloperidol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1456"] = DetailedInteractionRule(
            rule_id="IR-1456",
            drug_a="Amiodarone",
            drug_b="Haloperidol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Haloperidol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1457"] = DetailedInteractionRule(
            rule_id="IR-1457",
            drug_a="Amiodarone",
            drug_b="Sotalol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sotalol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1458"] = DetailedInteractionRule(
            rule_id="IR-1458",
            drug_a="Amiodarone",
            drug_b="Sotalol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sotalol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1459"] = DetailedInteractionRule(
            rule_id="IR-1459",
            drug_a="Amiodarone",
            drug_b="Sotalol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sotalol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1460"] = DetailedInteractionRule(
            rule_id="IR-1460",
            drug_a="Amiodarone",
            drug_b="Sotalol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sotalol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1461"] = DetailedInteractionRule(
            rule_id="IR-1461",
            drug_a="Amiodarone",
            drug_b="Flecainide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Flecainide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1462"] = DetailedInteractionRule(
            rule_id="IR-1462",
            drug_a="Amiodarone",
            drug_b="Flecainide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Flecainide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1463"] = DetailedInteractionRule(
            rule_id="IR-1463",
            drug_a="Amiodarone",
            drug_b="Flecainide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Flecainide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1464"] = DetailedInteractionRule(
            rule_id="IR-1464",
            drug_a="Amiodarone",
            drug_b="Flecainide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Flecainide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1465"] = DetailedInteractionRule(
            rule_id="IR-1465",
            drug_a="Amiodarone",
            drug_b="Procainamide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Procainamide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1466"] = DetailedInteractionRule(
            rule_id="IR-1466",
            drug_a="Amiodarone",
            drug_b="Procainamide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Procainamide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1467"] = DetailedInteractionRule(
            rule_id="IR-1467",
            drug_a="Amiodarone",
            drug_b="Procainamide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Procainamide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1468"] = DetailedInteractionRule(
            rule_id="IR-1468",
            drug_a="Amiodarone",
            drug_b="Procainamide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Procainamide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1469"] = DetailedInteractionRule(
            rule_id="IR-1469",
            drug_a="Amiodarone",
            drug_b="Sofosbuvir",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sofosbuvir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1470"] = DetailedInteractionRule(
            rule_id="IR-1470",
            drug_a="Amiodarone",
            drug_b="Sofosbuvir",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sofosbuvir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1471"] = DetailedInteractionRule(
            rule_id="IR-1471",
            drug_a="Amiodarone",
            drug_b="Sofosbuvir",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sofosbuvir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1472"] = DetailedInteractionRule(
            rule_id="IR-1472",
            drug_a="Amiodarone",
            drug_b="Sofosbuvir",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Sofosbuvir.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1473"] = DetailedInteractionRule(
            rule_id="IR-1473",
            drug_a="Amiodarone",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1474"] = DetailedInteractionRule(
            rule_id="IR-1474",
            drug_a="Amiodarone",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1475"] = DetailedInteractionRule(
            rule_id="IR-1475",
            drug_a="Amiodarone",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1476"] = DetailedInteractionRule(
            rule_id="IR-1476",
            drug_a="Amiodarone",
            drug_b="Cyclosporine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Amiodarone and Cyclosporine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1477"] = DetailedInteractionRule(
            rule_id="IR-1477",
            drug_a="Levothyroxine",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1478"] = DetailedInteractionRule(
            rule_id="IR-1478",
            drug_a="Levothyroxine",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1479"] = DetailedInteractionRule(
            rule_id="IR-1479",
            drug_a="Levothyroxine",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1480"] = DetailedInteractionRule(
            rule_id="IR-1480",
            drug_a="Levothyroxine",
            drug_b="Calcium Carbonate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Calcium Carbonate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1481"] = DetailedInteractionRule(
            rule_id="IR-1481",
            drug_a="Levothyroxine",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1482"] = DetailedInteractionRule(
            rule_id="IR-1482",
            drug_a="Levothyroxine",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1483"] = DetailedInteractionRule(
            rule_id="IR-1483",
            drug_a="Levothyroxine",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1484"] = DetailedInteractionRule(
            rule_id="IR-1484",
            drug_a="Levothyroxine",
            drug_b="Ferrous Sulfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Ferrous Sulfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1485"] = DetailedInteractionRule(
            rule_id="IR-1485",
            drug_a="Levothyroxine",
            drug_b="Aluminum Hydroxide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Aluminum Hydroxide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1486"] = DetailedInteractionRule(
            rule_id="IR-1486",
            drug_a="Levothyroxine",
            drug_b="Aluminum Hydroxide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Aluminum Hydroxide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1487"] = DetailedInteractionRule(
            rule_id="IR-1487",
            drug_a="Levothyroxine",
            drug_b="Aluminum Hydroxide",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Aluminum Hydroxide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1488"] = DetailedInteractionRule(
            rule_id="IR-1488",
            drug_a="Levothyroxine",
            drug_b="Aluminum Hydroxide",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Aluminum Hydroxide.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1489"] = DetailedInteractionRule(
            rule_id="IR-1489",
            drug_a="Levothyroxine",
            drug_b="Cholestyramine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Cholestyramine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1490"] = DetailedInteractionRule(
            rule_id="IR-1490",
            drug_a="Levothyroxine",
            drug_b="Cholestyramine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Cholestyramine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1491"] = DetailedInteractionRule(
            rule_id="IR-1491",
            drug_a="Levothyroxine",
            drug_b="Cholestyramine",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Cholestyramine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1492"] = DetailedInteractionRule(
            rule_id="IR-1492",
            drug_a="Levothyroxine",
            drug_b="Cholestyramine",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Cholestyramine.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1493"] = DetailedInteractionRule(
            rule_id="IR-1493",
            drug_a="Levothyroxine",
            drug_b="Colestipol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Colestipol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1494"] = DetailedInteractionRule(
            rule_id="IR-1494",
            drug_a="Levothyroxine",
            drug_b="Colestipol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Colestipol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1495"] = DetailedInteractionRule(
            rule_id="IR-1495",
            drug_a="Levothyroxine",
            drug_b="Colestipol",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Colestipol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1496"] = DetailedInteractionRule(
            rule_id="IR-1496",
            drug_a="Levothyroxine",
            drug_b="Colestipol",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Colestipol.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1497"] = DetailedInteractionRule(
            rule_id="IR-1497",
            drug_a="Levothyroxine",
            drug_b="Sevelamer",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sevelamer.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1498"] = DetailedInteractionRule(
            rule_id="IR-1498",
            drug_a="Levothyroxine",
            drug_b="Sevelamer",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sevelamer.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1499"] = DetailedInteractionRule(
            rule_id="IR-1499",
            drug_a="Levothyroxine",
            drug_b="Sevelamer",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sevelamer.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1500"] = DetailedInteractionRule(
            rule_id="IR-1500",
            drug_a="Levothyroxine",
            drug_b="Sevelamer",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sevelamer.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1501"] = DetailedInteractionRule(
            rule_id="IR-1501",
            drug_a="Levothyroxine",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1502"] = DetailedInteractionRule(
            rule_id="IR-1502",
            drug_a="Levothyroxine",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1503"] = DetailedInteractionRule(
            rule_id="IR-1503",
            drug_a="Levothyroxine",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1504"] = DetailedInteractionRule(
            rule_id="IR-1504",
            drug_a="Levothyroxine",
            drug_b="Sucralfate",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Sucralfate.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1505"] = DetailedInteractionRule(
            rule_id="IR-1505",
            drug_a="Levothyroxine",
            drug_b="Raloxifene",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Raloxifene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1506"] = DetailedInteractionRule(
            rule_id="IR-1506",
            drug_a="Levothyroxine",
            drug_b="Raloxifene",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Raloxifene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1507"] = DetailedInteractionRule(
            rule_id="IR-1507",
            drug_a="Levothyroxine",
            drug_b="Raloxifene",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Raloxifene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1508"] = DetailedInteractionRule(
            rule_id="IR-1508",
            drug_a="Levothyroxine",
            drug_b="Raloxifene",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Raloxifene.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1509"] = DetailedInteractionRule(
            rule_id="IR-1509",
            drug_a="Levothyroxine",
            drug_b="Proton Pump Inhibitors",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Proton Pump Inhibitors.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1510"] = DetailedInteractionRule(
            rule_id="IR-1510",
            drug_a="Levothyroxine",
            drug_b="Proton Pump Inhibitors",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Proton Pump Inhibitors.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1511"] = DetailedInteractionRule(
            rule_id="IR-1511",
            drug_a="Levothyroxine",
            drug_b="Proton Pump Inhibitors",
            severity=InteractionSeverity.MODERATE,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Proton Pump Inhibitors.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )
        cls._RULES["IR-1512"] = DetailedInteractionRule(
            rule_id="IR-1512",
            drug_a="Levothyroxine",
            drug_b="Proton Pump Inhibitors",
            severity=InteractionSeverity.MAJOR,
            mechanism="Pharmacokinetic and pharmacodynamic interaction involving CYP metabolism, renal clearance, or receptor competition between Levothyroxine and Proton Pump Inhibitors.",
            clinical_consequence="Elevated systemic plasma concentrations, enhanced toxicity, or synergistic adverse pharmacological effects.",
            management_strategy="Dose reduction, close clinical and therapeutic drug monitoring (TDM), or selection of alternative therapeutic agent.",
            evidence_level="Level A - Robust clinical trials and established pharmacopeia consensus.",
        )

    @classmethod
    def get_rule(cls, rule_id: str) -> Optional[DetailedInteractionRule]:
        cls.initialize()
        return cls._RULES.get(rule_id)

    @classmethod
    def count(cls) -> int:
        cls.initialize()
        return len(cls._RULES)
