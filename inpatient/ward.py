"""
Hospital Ward, Room, and Bed Allocation Management
Tracks real-time hospital bed occupancy, isolation requirements, and nursing ward units.
"""

from dataclasses import dataclass, field
from enum import Enum, unique
from typing import Dict, List, Optional
from domain.models import BaseEntity


@unique
class BedStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    OCCUPIED = "OCCUPIED"
    CLEANING = "CLEANING"
    MAINTENANCE = "MAINTENANCE"
    ISOLATION = "ISOLATION"


@dataclass
class Bed:
    bed_id: str
    room_number: str
    ward_name: str
    bed_type: str  # ICU, Med-Surg, Step-Down, Telemetry, Pediatric
    status: BedStatus = BedStatus.AVAILABLE
    current_patient_id: Optional[str] = None
    assigned_nurse_id: Optional[str] = None


@dataclass
class Ward:
    name: str
    department: str
    total_capacity: int
    beds: List[Bed] = field(default_factory=list)

    @property
    def occupied_count(self) -> int:
        return sum(1 for b in self.beds if b.status == BedStatus.OCCUPIED)

    @property
    def occupancy_rate(self) -> float:
        if self.total_capacity == 0:
            return 0.0
        return round((self.occupied_count / self.total_capacity) * 100.0, 1)


class WardManager:
    """Manages hospital inpatient units and bed assignments."""

    def __init__(self):
        self._wards: Dict[str, Ward] = {}
        self._initialize_hospital_wards()

    def _initialize_hospital_wards(self):
        icu_beds = [Bed(bed_id=f"ICU-B{i:02d}", room_number=f"ICU-10{i}", ward_name="Intensive Care Unit", bed_type="ICU") for i in range(1, 11)]
        medsurg_beds = [Bed(bed_id=f"MS-B{i:02d}", room_number=f"MS-20{i}", ward_name="General Med-Surg", bed_type="Med-Surg") for i in range(1, 21)]
        
        self._wards["ICU"] = Ward(name="Intensive Care Unit", department="Critical Care", total_capacity=10, beds=icu_beds)
        self._wards["MEDSURG"] = Ward(name="General Med-Surg", department="Internal Medicine", total_capacity=20, beds=medsurg_beds)

    def assign_patient_to_bed(self, ward_key: str, bed_id: str, patient_id: str, nurse_id: Optional[str] = None) -> bool:
        ward = self._wards.get(ward_key)
        if not ward:
            return False
        for bed in ward.beds:
            if bed.bed_id == bed_id and bed.status == BedStatus.AVAILABLE:
                bed.status = BedStatus.OCCUPIED
                bed.current_patient_id = patient_id
                bed.assigned_nurse_id = nurse_id
                return True
        return False

    def discharge_bed(self, ward_key: str, bed_id: str) -> bool:
        ward = self._wards.get(ward_key)
        if not ward:
            return False
        for bed in ward.beds:
            if bed.bed_id == bed_id:
                bed.status = BedStatus.CLEANING
                bed.current_patient_id = None
                return True
        return False

    def get_ward(self, ward_key: str) -> Optional[Ward]:
        return self._wards.get(ward_key)
