"""
HealthSphere Appointment & Scheduling Service
Slot generation, booking conflict avoidance, rescheduling, and status management.
"""

from datetime import datetime, timedelta
from typing import List, Optional
from core.audit import audit_service
from core.enums import AppointmentStatus, AppointmentType, AuditAction
from core.exceptions import ConflictError, EntityNotFoundError, ValidationError
from core.security import RBACManager, UserContext
from domain.appointments import Appointment, Doctor, ScheduleSlot
from repositories.memory_repo import AppointmentRepository, DoctorRepository, PatientRepository


class AppointmentService:
    """Manages physician schedules, consultation booking, and workflow state changes."""

    def __init__(
        self,
        appointment_repo: AppointmentRepository,
        doctor_repo: DoctorRepository,
        patient_repo: PatientRepository,
    ):
        self.appointment_repo = appointment_repo
        self.doctor_repo = doctor_repo
        self.patient_repo = patient_repo

    def register_doctor(
        self,
        license_number: str,
        first_name: str,
        last_name: str,
        specialty: str = "General Medicine",
        department: str = "Outpatient",
        consultation_fee: float = 150.0,
        context: Optional[UserContext] = None,
    ) -> Doctor:
        if context:
            RBACManager.check_permission(context, "system:admin")

        if not license_number.strip():
            raise ValidationError("Doctor license number is required.")

        doctor = Doctor(
            license_number=license_number.strip(),
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            specialty=specialty,
            department=department,
            consultation_fee=consultation_fee,
        )
        return self.doctor_repo.save(doctor)

    def generate_daily_slots(
        self,
        doctor_id: str,
        date_str: str,  # YYYY-MM-DD
        start_hour: int = 9,
        end_hour: int = 17,
        slot_duration_minutes: int = 30,
        context: Optional[UserContext] = None,
    ) -> List[ScheduleSlot]:
        """Generate open consultation slots for a doctor on a given day."""
        if context:
            RBACManager.check_permission(context, "appointment:write")

        doctor = self.doctor_repo.get_by_id_or_raise(doctor_id)
        base_date = datetime.strptime(date_str, "%Y-%m-%d")

        slots: List[ScheduleSlot] = []
        current_time = base_date.replace(hour=start_hour, minute=0, second=0)
        end_time_boundary = base_date.replace(hour=end_hour, minute=0, second=0)

        while current_time + timedelta(minutes=slot_duration_minutes) <= end_time_boundary:
            slot_end = current_time + timedelta(minutes=slot_duration_minutes)
            slot_id = f"SLOT-{doctor_id[:6]}-{current_time.strftime('%Y%m%d%H%M')}"

            # Check if already exists
            existing = doctor.find_slot(slot_id)
            if not existing:
                slot = ScheduleSlot(
                    slot_id=slot_id,
                    doctor_id=doctor_id,
                    start_time=current_time.isoformat(),
                    end_time=slot_end.isoformat(),
                    is_booked=False,
                )
                doctor.add_slot(slot)
                slots.append(slot)
            else:
                slots.append(existing)

            current_time = slot_end

        self.doctor_repo.save(doctor)
        return slots

    def book_appointment(
        self,
        patient_id: str,
        doctor_id: str,
        slot_id: str,
        reason_for_visit: str,
        appointment_type: AppointmentType = AppointmentType.ROUTINE_CHECKUP,
        context: Optional[UserContext] = None,
    ) -> Appointment:
        """Book a doctor slot for a patient with double-booking prevention."""
        if context:
            RBACManager.check_permission(context, "appointment:write")

        # Verify patient and doctor exist
        self.patient_repo.get_by_id_or_raise(patient_id)
        doctor = self.doctor_repo.get_by_id_or_raise(doctor_id)

        slot = doctor.find_slot(slot_id)
        if not slot:
            raise EntityNotFoundError("ScheduleSlot", slot_id)

        if slot.is_booked:
            raise ConflictError(f"Slot '{slot_id}' is already booked by another patient.")

        # Create appointment
        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            slot_id=slot_id,
            appointment_type=appointment_type,
            status=AppointmentStatus.SCHEDULED,
            scheduled_start=slot.start_time,
            scheduled_end=slot.end_time,
            reason_for_visit=reason_for_visit,
        )
        saved_appointment = self.appointment_repo.save(appointment)

        # Mark slot as booked
        slot.is_booked = True
        slot.booked_appointment_id = saved_appointment.id
        self.doctor_repo.save(doctor)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="Appointment",
            resource_id=saved_appointment.id,
            details={"patient_id": patient_id, "doctor_id": doctor_id, "slot_id": slot_id},
        )

        return saved_appointment

    def cancel_appointment(
        self,
        appointment_id: str,
        reason: str,
        context: Optional[UserContext] = None,
    ) -> Appointment:
        if context:
            RBACManager.check_permission(context, "appointment:cancel")

        appointment = self.appointment_repo.get_by_id_or_raise(appointment_id)
        if appointment.status in (AppointmentStatus.CANCELLED, AppointmentStatus.COMPLETED):
            raise ConflictError(f"Cannot cancel appointment with status {appointment.status.value}")

        appointment.cancel(reason)
        self.appointment_repo.save(appointment)

        # Free up doctor slot
        doctor = self.doctor_repo.get_by_id(appointment.doctor_id)
        if doctor:
            slot = doctor.find_slot(appointment.slot_id)
            if slot:
                slot.is_booked = False
                slot.booked_appointment_id = None
                self.doctor_repo.save(doctor)

        return appointment

    def check_in_patient(
        self,
        appointment_id: str,
        context: Optional[UserContext] = None,
    ) -> Appointment:
        if context:
            RBACManager.check_permission(context, "appointment:write")

        appointment = self.appointment_repo.get_by_id_or_raise(appointment_id)
        appointment.check_in()
        return self.appointment_repo.save(appointment)
