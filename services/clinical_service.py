"""
HealthSphere Clinical EHR Service
Clinical encounters, physiological vitals monitoring, SOAP charting, and ICD-10 diagnostic tagging.
"""

from typing import List, Optional
from core.audit import audit_service
from core.enums import AuditAction, EncounterStatus, EncounterType
from core.exceptions import ConflictError, EntityNotFoundError, ValidationError
from core.security import RBACManager, UserContext
from domain.clinical import ClinicalNote, Diagnosis, Encounter, Immunization, Vitals
from repositories.memory_repo import (
    AppointmentRepository,
    DoctorRepository,
    EncounterRepository,
    PatientRepository,
)


class ClinicalService:
    """Manages patient clinical encounters, medical documentation, and vital metrics."""

    def __init__(
        self,
        encounter_repo: EncounterRepository,
        patient_repo: PatientRepository,
        doctor_repo: DoctorRepository,
        appointment_repo: Optional[AppointmentRepository] = None,
    ):
        self.encounter_repo = encounter_repo
        self.patient_repo = patient_repo
        self.doctor_repo = doctor_repo
        self.appointment_repo = appointment_repo

    def start_encounter(
        self,
        patient_id: str,
        attending_doctor_id: str,
        encounter_type: EncounterType = EncounterType.OUTPATIENT,
        chief_complaint: str = "",
        appointment_id: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> Encounter:
        """Initiates a clinical care encounter."""
        if context:
            RBACManager.check_permission(context, "clinical:write")

        self.patient_repo.get_by_id_or_raise(patient_id)
        self.doctor_repo.get_by_id_or_raise(attending_doctor_id)

        encounter = Encounter(
            patient_id=patient_id,
            attending_doctor_id=attending_doctor_id,
            encounter_type=encounter_type,
            status=EncounterStatus.IN_PROGRESS,
            chief_complaint=chief_complaint,
        )
        saved_encounter = self.encounter_repo.save(encounter)

        if appointment_id and self.appointment_repo:
            appointment = self.appointment_repo.get_by_id(appointment_id)
            if appointment:
                appointment.complete(saved_encounter.id)
                self.appointment_repo.save(appointment)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="Encounter",
            resource_id=saved_encounter.id,
            details={"patient_id": patient_id, "doctor_id": attending_doctor_id},
        )

        return saved_encounter

    def record_vitals(
        self,
        encounter_id: str,
        systolic_bp: int,
        diastolic_bp: int,
        heart_rate_bpm: int,
        respiratory_rate: int,
        temperature_celsius: float,
        spo2_percentage: float,
        height_cm: float,
        weight_kg: float,
        recorded_by_staff_id: str = "",
        context: Optional[UserContext] = None,
    ) -> Vitals:
        """Record patient vitals and attach to active encounter."""
        if context:
            RBACManager.check_permission(context, "clinical:vitals")

        encounter = self.encounter_repo.get_by_id_or_raise(encounter_id)
        if encounter.status == EncounterStatus.DISCHARGED:
            raise ConflictError("Cannot record vitals on a discharged encounter.")

        if systolic_bp <= 0 or diastolic_bp <= 0:
            raise ValidationError("Blood pressure values must be positive integers.")
        if heart_rate_bpm <= 0:
            raise ValidationError("Heart rate must be positive integer.")

        vitals = Vitals(
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            heart_rate_bpm=heart_rate_bpm,
            respiratory_rate=respiratory_rate,
            temperature_celsius=round(temperature_celsius, 1),
            spo2_percentage=round(spo2_percentage, 1),
            height_cm=round(height_cm, 1),
            weight_kg=round(weight_kg, 1),
            recorded_by_staff_id=recorded_by_staff_id,
        )

        encounter.attach_vitals(vitals)
        self.encounter_repo.save(encounter)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.UPDATE,
            resource_type="Encounter",
            resource_id=encounter_id,
            details={"action": "RECORD_VITALS", "bp": f"{systolic_bp}/{diastolic_bp}", "bmi": str(vitals.bmi)},
        )

        return vitals

    def document_soap_note(
        self,
        encounter_id: str,
        subjective: str,
        objective: str,
        assessment: str,
        plan: str,
        author_doctor_id: str,
        context: Optional[UserContext] = None,
    ) -> ClinicalNote:
        """Document official clinical SOAP notes."""
        if context:
            RBACManager.check_permission(context, "clinical:write")

        encounter = self.encounter_repo.get_by_id_or_raise(encounter_id)
        doctor = self.doctor_repo.get_by_id_or_raise(author_doctor_id)

        note = ClinicalNote(
            subjective=subjective,
            objective=objective,
            assessment=assessment,
            plan=plan,
            author_doctor_id=author_doctor_id,
            author_doctor_name=doctor.full_name,
        )

        encounter.set_soap_note(note)
        self.encounter_repo.save(encounter)
        return note

    def add_diagnosis(
        self,
        encounter_id: str,
        icd10_code: str,
        description: str,
        is_primary: bool = True,
        notes: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> Diagnosis:
        """Add an ICD-10 coded clinical diagnosis to the encounter."""
        if context:
            RBACManager.check_permission(context, "clinical:write")

        encounter = self.encounter_repo.get_by_id_or_raise(encounter_id)
        diagnosis = Diagnosis(
            icd10_code=icd10_code.upper().strip(),
            description=description.strip(),
            is_primary=is_primary,
            notes=notes,
        )
        encounter.add_diagnosis(diagnosis)
        self.encounter_repo.save(encounter)
        return diagnosis

    def complete_encounter(
        self,
        encounter_id: str,
        discharge_summary: str,
        context: Optional[UserContext] = None,
    ) -> Encounter:
        """Finalize and close clinical encounter."""
        if context:
            RBACManager.check_permission(context, "clinical:write")

        encounter = self.encounter_repo.get_by_id_or_raise(encounter_id)
        encounter.complete_encounter(discharge_summary)
        return self.encounter_repo.save(encounter)
