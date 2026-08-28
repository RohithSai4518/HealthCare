"""
HealthSphere Patient Domain Models
Comprehensive patient demographics, emergency contacts, allergy profiles, and medical history.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.enums import AllergyCategory, AllergySeverity, BloodGroup, Gender, MaritalStatus
from domain.models import Address, BaseEntity, ContactInfo, InsurancePolicy


@dataclass
class EmergencyContact:
    """Designated emergency contact details."""

    full_name: str
    relationship: str  # e.g., Spouse, Parent, Sibling
    phone_number: str
    email: Optional[str] = None
    is_primary: bool = True

    def to_dict(self) -> dict:
        return {
            "full_name": self.full_name,
            "relationship": self.relationship,
            "phone_number": self.phone_number,
            "email": self.email,
            "is_primary": self.is_primary,
        }


@dataclass
class Allergy:
    """Documented adverse drug reaction or allergy."""

    allergen: str
    category: AllergyCategory
    severity: AllergySeverity
    reaction_symptoms: str
    onset_date: Optional[str] = None
    is_active: bool = True
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "allergen": self.allergen,
            "category": self.category.value if isinstance(self.category, AllergyCategory) else self.category,
            "severity": self.severity.value if isinstance(self.severity, AllergySeverity) else self.severity,
            "reaction_symptoms": self.reaction_symptoms,
            "onset_date": self.onset_date,
            "is_active": self.is_active,
            "notes": self.notes,
        }


@dataclass
class MedicalHistoryRecord:
    """Historical condition or surgical record."""

    condition_or_procedure: str
    diagnosed_or_performed_date: str
    resolved_date: Optional[str] = None
    icd10_code: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "condition_or_procedure": self.condition_or_procedure,
            "diagnosed_or_performed_date": self.diagnosed_or_performed_date,
            "resolved_date": self.resolved_date,
            "icd10_code": self.icd10_code,
            "notes": self.notes,
        }


@dataclass
class Patient(BaseEntity):
    """Patient Aggregate Root representing medical record number and profile."""

    mrn: str = ""  # Medical Record Number
    first_name: str = ""
    last_name: str = ""
    date_of_birth: str = ""  # YYYY-MM-DD
    gender: Gender = Gender.UNKNOWN
    blood_group: BloodGroup = BloodGroup.UNKNOWN
    marital_status: MaritalStatus = MaritalStatus.SINGLE
    primary_language: str = "English"
    address: Optional[Address] = None
    contact: Optional[ContactInfo] = None
    emergency_contacts: List[EmergencyContact] = field(default_factory=list)
    allergies: List[Allergy] = field(default_factory=list)
    medical_history: List[MedicalHistoryRecord] = field(default_factory=list)
    insurance: Optional[InsurancePolicy] = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def add_allergy(self, allergy: Allergy) -> None:
        # Avoid duplicate allergens
        for existing in self.allergies:
            if existing.allergen.lower() == allergy.allergen.lower() and existing.is_active:
                existing.severity = allergy.severity
                existing.reaction_symptoms = allergy.reaction_symptoms
                existing.notes = allergy.notes
                self.mark_updated()
                return
        self.allergies.append(allergy)
        self.mark_updated()

    def add_history(self, history: MedicalHistoryRecord) -> None:
        self.medical_history.append(history)
        self.mark_updated()

    def add_emergency_contact(self, contact: EmergencyContact) -> None:
        if contact.is_primary:
            for c in self.emergency_contacts:
                c.is_primary = False
        self.emergency_contacts.append(contact)
        self.mark_updated()
