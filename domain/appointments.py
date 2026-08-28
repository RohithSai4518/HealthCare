"""
HealthSphere Appointment & Scheduling Domain Models
Doctor profiles, operational availability slots, and patient booking lifecycle.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional
from core.enums import AppointmentStatus, AppointmentType
from domain.models import BaseEntity, ContactInfo, current_timestamp_iso


@dataclass
class ScheduleSlot:
    """Discrete time slot allocated for consultation."""

    slot_id: str
    doctor_id: str
    start_time: str  # ISO 8601
    end_time: str  # ISO 8601
    is_booked: bool = False
    booked_appointment_id: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "slot_id": self.slot_id,
            "doctor_id": self.doctor_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "is_booked": self.is_booked,
            "booked_appointment_id": self.booked_appointment_id,
        }


@dataclass
class Doctor(BaseEntity):
    """Healthcare Practitioner / Physician Entity."""

    license_number: str = ""
    first_name: str = ""
    last_name: str = ""
    specialty: str = "General Medicine"
    department: str = "Outpatient"
    contact: Optional[ContactInfo] = None
    consultation_fee: float = 150.0
    schedule_slots: List[ScheduleSlot] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"Dr. {self.first_name} {self.last_name}".strip()

    def add_slot(self, slot: ScheduleSlot) -> None:
        self.schedule_slots.append(slot)
        self.mark_updated()

    def find_slot(self, slot_id: str) -> Optional[ScheduleSlot]:
        for slot in self.schedule_slots:
            if slot.slot_id == slot_id:
                return slot
        return None


@dataclass
class Appointment(BaseEntity):
    """Appointment booking aggregate root."""

    patient_id: str = ""
    doctor_id: str = ""
    slot_id: str = ""
    appointment_type: AppointmentType = AppointmentType.ROUTINE_CHECKUP
    status: AppointmentStatus = AppointmentStatus.SCHEDULED
    scheduled_start: str = ""
    scheduled_end: str = ""
    reason_for_visit: str = ""
    cancellation_reason: Optional[str] = None
    check_in_time: Optional[str] = None
    completed_time: Optional[str] = None
    encounter_id: Optional[str] = None

    def confirm(self) -> None:
        self.status = AppointmentStatus.CONFIRMED
        self.mark_updated()

    def check_in(self) -> None:
        self.status = AppointmentStatus.IN_PROGRESS
        self.check_in_time = current_timestamp_iso()
        self.mark_updated()

    def complete(self, encounter_id: Optional[str] = None) -> None:
        self.status = AppointmentStatus.COMPLETED
        self.completed_time = current_timestamp_iso()
        if encounter_id:
            self.encounter_id = encounter_id
        self.mark_updated()

    def cancel(self, reason: str) -> None:
        self.status = AppointmentStatus.CANCELLED
        self.cancellation_reason = reason
        self.mark_updated()

    def mark_no_show(self) -> None:
        self.status = AppointmentStatus.NO_SHOW
        self.mark_updated()
