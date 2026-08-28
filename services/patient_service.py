"""
HealthSphere Patient Service
Manages patient registration, demographic updates, allergy documentation, and medical history.
"""

import time
from typing import List, Optional
from core.audit import audit_service
from core.enums import AuditAction, BloodGroup, Gender, MaritalStatus, UserRole
from core.exceptions import EntityNotFoundError, ValidationError
from core.security import RBACManager, UserContext
from domain.models import Address, ContactInfo, InsurancePolicy
from domain.patient import Allergy, EmergencyContact, MedicalHistoryRecord, Patient
from repositories.memory_repo import PatientRepository


class PatientService:
    """Orchestrates patient lifecycle and clinical profile management."""

    def __init__(self, patient_repo: PatientRepository):
        self.patient_repo = patient_repo

    def _generate_mrn(self) -> str:
        """Generate unique Medical Record Number."""
        count = self.patient_repo.count() + 1
        timestamp_part = str(int(time.time()))[-4:]
        return f"MRN-{timestamp_part}-{count:05d}"

    def register_patient(
        self,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        gender: Gender,
        blood_group: BloodGroup = BloodGroup.UNKNOWN,
        marital_status: MaritalStatus = MaritalStatus.SINGLE,
        primary_language: str = "English",
        address: Optional[Address] = None,
        contact: Optional[ContactInfo] = None,
        insurance: Optional[InsurancePolicy] = None,
        context: Optional[UserContext] = None,
    ) -> Patient:
        """Register a new patient into the system."""
        if context:
            RBACManager.check_permission(context, "patient:write")

        if not first_name.strip() or not last_name.strip():
            raise ValidationError("Patient first and last names are mandatory.", "name")
        if not date_of_birth.strip():
            raise ValidationError("Patient date of birth is mandatory.", "date_of_birth")

        mrn = self._generate_mrn()
        patient = Patient(
            mrn=mrn,
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            date_of_birth=date_of_birth.strip(),
            gender=gender,
            blood_group=blood_group,
            marital_status=marital_status,
            primary_language=primary_language,
            address=address,
            contact=contact,
            insurance=insurance,
        )

        saved_patient = self.patient_repo.save(patient)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="Patient",
            resource_id=saved_patient.id,
            details={"mrn": mrn, "patient_name": saved_patient.full_name},
        )

        return saved_patient

    def get_patient_by_id(self, patient_id: str, context: Optional[UserContext] = None) -> Patient:
        if context:
            if context.role == UserRole.PATIENT and context.linked_entity_id != patient_id:
                RBACManager.check_permission(context, "patient:read")
            elif context.role != UserRole.PATIENT:
                RBACManager.check_permission(context, "patient:read")

        patient = self.patient_repo.get_by_id(patient_id)
        if not patient:
            raise EntityNotFoundError("Patient", patient_id)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.READ,
            resource_type="Patient",
            resource_id=patient.id,
        )
        return patient

    def get_patient_by_mrn(self, mrn: str, context: Optional[UserContext] = None) -> Patient:
        if context:
            RBACManager.check_permission(context, "patient:read")
        patient = self.patient_repo.get_by_mrn(mrn)
        if not patient:
            raise EntityNotFoundError("Patient", mrn)
        return patient

    def search_patients(self, query: str, context: Optional[UserContext] = None) -> List[Patient]:
        if context:
            RBACManager.check_permission(context, "patient:read")
        return self.patient_repo.search_by_name(query)

    def add_patient_allergy(
        self,
        patient_id: str,
        allergy: Allergy,
        context: Optional[UserContext] = None,
    ) -> Patient:
        if context:
            RBACManager.check_permission(context, "patient:write")
        patient = self.get_patient_by_id(patient_id, context)
        patient.add_allergy(allergy)
        self.patient_repo.save(patient)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.UPDATE,
            resource_type="Patient",
            resource_id=patient_id,
            details={"allergen": allergy.allergen, "severity": allergy.severity.value},
        )
        return patient

    def add_medical_history(
        self,
        patient_id: str,
        history: MedicalHistoryRecord,
        context: Optional[UserContext] = None,
    ) -> Patient:
        if context:
            RBACManager.check_permission(context, "patient:write")
        patient = self.get_patient_by_id(patient_id, context)
        patient.add_history(history)
        self.patient_repo.save(patient)
        return patient

    def update_insurance_policy(
        self,
        patient_id: str,
        insurance: InsurancePolicy,
        context: Optional[UserContext] = None,
    ) -> Patient:
        if context:
            RBACManager.check_permission(context, "patient:write")
        patient = self.get_patient_by_id(patient_id, context)
        patient.insurance = insurance
        self.patient_repo.save(patient)
        return patient
