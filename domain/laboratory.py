"""
HealthSphere Laboratory Information System (LIS) Domain Models
Diagnostic test catalog, specimen tracking, reference ranges, and laboratory order lifecycle.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.enums import AbnormalityFlag, LabOrderStatus, LabTestCategory
from domain.models import BaseEntity, current_timestamp_iso


@dataclass
class ReferenceRange:
    """Standard biological reference intervals for laboratory assays."""

    low_value: float
    high_value: float
    unit_of_measure: str
    critical_low: Optional[float] = None
    critical_high: Optional[float] = None

    def evaluate(self, measured_value: float) -> AbnormalityFlag:
        if self.critical_low is not None and measured_value <= self.critical_low:
            return AbnormalityFlag.CRITICAL_LOW
        if self.critical_high is not None and measured_value >= self.critical_high:
            return AbnormalityFlag.CRITICAL_HIGH
        if measured_value < self.low_value:
            return AbnormalityFlag.LOW
        if measured_value > self.high_value:
            return AbnormalityFlag.HIGH
        return AbnormalityFlag.NORMAL

    def to_dict(self) -> dict:
        return {
            "low_value": self.low_value,
            "high_value": self.high_value,
            "unit_of_measure": self.unit_of_measure,
            "critical_low": self.critical_low,
            "critical_high": self.critical_high,
        }


@dataclass
class LabTestType(BaseEntity):
    """Laboratory test definition aligned with standard LOINC / CPT codification."""

    code: str = ""  # e.g., LOINC 718-7 or CPT 85025
    name: str = ""  # e.g., "Complete Blood Count (CBC)"
    category: LabTestCategory = LabTestCategory.HEMATOLOGY
    sample_type_required: str = "Whole Blood (EDTA)"
    standard_price: float = 45.0
    turnaround_time_hours: int = 4
    reference_range: Optional[ReferenceRange] = None


@dataclass
class LabResultItem:
    """Individual quantitative or qualitative parameter result."""

    parameter_name: str
    measured_value: float
    unit_of_measure: str
    reference_range_display: str
    flag: AbnormalityFlag = AbnormalityFlag.NORMAL
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "parameter_name": self.parameter_name,
            "measured_value": self.measured_value,
            "unit_of_measure": self.unit_of_measure,
            "reference_range_display": self.reference_range_display,
            "flag": self.flag.value if isinstance(self.flag, AbnormalityFlag) else self.flag,
            "notes": self.notes,
        }


@dataclass
class LabOrder(BaseEntity):
    """Diagnostic laboratory order aggregate root."""

    patient_id: str = ""
    ordering_doctor_id: str = ""
    encounter_id: Optional[str] = None
    test_type_ids: List[str] = field(default_factory=list)
    status: LabOrderStatus = LabOrderStatus.ORDERED
    clinical_indication: str = ""
    specimen_barcode: Optional[str] = None
    collected_at: Optional[str] = None
    collected_by_technician_id: Optional[str] = None
    processed_at: Optional[str] = None
    completed_at: Optional[str] = None
    results: List[LabResultItem] = field(default_factory=list)
    technician_notes: Optional[str] = None

    @property
    def has_critical_values(self) -> bool:
        for r in self.results:
            if r.flag in (AbnormalityFlag.CRITICAL_HIGH, AbnormalityFlag.CRITICAL_LOW):
                return True
        return False

    def collect_sample(self, barcode: str, tech_id: str) -> None:
        self.specimen_barcode = barcode
        self.collected_by_technician_id = tech_id
        self.collected_at = current_timestamp_iso()
        self.status = LabOrderStatus.SAMPLE_COLLECTED
        self.mark_updated()

    def process_sample(self) -> None:
        self.processed_at = current_timestamp_iso()
        self.status = LabOrderStatus.PROCESSING
        self.mark_updated()

    def submit_results(self, results: List[LabResultItem], notes: Optional[str] = None) -> None:
        self.results = results
        self.technician_notes = notes
        self.completed_at = current_timestamp_iso()
        self.status = LabOrderStatus.COMPLETED
        self.mark_updated()
