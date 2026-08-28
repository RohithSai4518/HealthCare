"""
HealthSphere Clinical EHR Domain Models
Vitals charting, SOAP clinical notes, ICD-10 diagnostic coding, immunizations, and clinical encounters.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.enums import AbnormalityFlag, EncounterStatus, EncounterType
from domain.models import BaseEntity, current_timestamp_iso


@dataclass
class Vitals:
    """Patient physiological measurements with clinical classification flags."""

    systolic_bp: int  # mmHg
    diastolic_bp: int  # mmHg
    heart_rate_bpm: int  # beats per min
    respiratory_rate: int  # breaths per min
    temperature_celsius: float  # Celsius
    spo2_percentage: float  # Oxygen saturation %
    height_cm: float
    weight_kg: float
    recorded_at: str = field(default_factory=current_timestamp_iso)
    recorded_by_staff_id: str = ""

    @property
    def bmi(self) -> float:
        if self.height_cm <= 0:
            return 0.0
        height_m = self.height_cm / 100.0
        return round(self.weight_kg / (height_m * height_m), 1)

    @property
    def bp_category(self) -> str:
        if self.systolic_bp < 90 or self.diastolic_bp < 60:
            return "HYPOTENSION"
        if self.systolic_bp < 120 and self.diastolic_bp < 80:
            return "NORMAL"
        if self.systolic_bp <= 129 and self.diastolic_bp < 80:
            return "ELEVATED"
        if self.systolic_bp <= 139 or self.diastolic_bp <= 89:
            return "STAGE_1_HYPERTENSION"
        return "STAGE_2_HYPERTENSION"

    @property
    def is_feverish(self) -> bool:
        return self.temperature_celsius >= 38.0

    @property
    def is_hypoxic(self) -> bool:
        return self.spo2_percentage < 95.0

    def to_dict(self) -> dict:
        return {
            "systolic_bp": self.systolic_bp,
            "diastolic_bp": self.diastolic_bp,
            "heart_rate_bpm": self.heart_rate_bpm,
            "respiratory_rate": self.respiratory_rate,
            "temperature_celsius": self.temperature_celsius,
            "spo2_percentage": self.spo2_percentage,
            "height_cm": self.height_cm,
            "weight_kg": self.weight_kg,
            "bmi": self.bmi,
            "bp_category": self.bp_category,
            "is_feverish": self.is_feverish,
            "is_hypoxic": self.is_hypoxic,
            "recorded_at": self.recorded_at,
            "recorded_by_staff_id": self.recorded_by_staff_id,
        }


@dataclass
class Diagnosis:
    """Clinical diagnosis classified with ICD-10 codification."""

    icd10_code: str
    description: str
    is_primary: bool = True
    clinical_status: str = "ACTIVE"  # ACTIVE, RESOLVED, RECURRENT
    verification_status: str = "CONFIRMED"  # PROVISIONAL, CONFIRMED, REFUTED
    diagnosed_date: str = field(default_factory=current_timestamp_iso)
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "icd10_code": self.icd10_code,
            "description": self.description,
            "is_primary": self.is_primary,
            "clinical_status": self.clinical_status,
            "verification_status": self.verification_status,
            "diagnosed_date": self.diagnosed_date,
            "notes": self.notes,
        }


@dataclass
class ClinicalNote:
    """Standardized SOAP (Subjective, Objective, Assessment, Plan) documentation."""

    subjective: str  # Chief complaint, history of present illness
    objective: str  # Physical examination findings
    assessment: str  # Clinical impression and differentials
    plan: str  # Diagnostic orders, treatment, therapies, education
    author_doctor_id: str
    author_doctor_name: str
    created_at: str = field(default_factory=current_timestamp_iso)

    def to_dict(self) -> dict:
        return {
            "subjective": self.subjective,
            "objective": self.objective,
            "assessment": self.assessment,
            "plan": self.plan,
            "author_doctor_id": self.author_doctor_id,
            "author_doctor_name": self.author_doctor_name,
            "created_at": self.created_at,
        }


@dataclass
class Immunization:
    """Vaccination record entry."""

    vaccine_code: str
    vaccine_name: str
    administered_date: str
    dose_sequence: int
    lot_number: str
    expiration_date: str
    administered_by_staff_id: str
    site: str = "Left Deltoid"  # Left Deltoid, Right Thigh, etc.

    def to_dict(self) -> dict:
        return {
            "vaccine_code": self.vaccine_code,
            "vaccine_name": self.vaccine_name,
            "administered_date": self.administered_date,
            "dose_sequence": self.dose_sequence,
            "lot_number": self.lot_number,
            "expiration_date": self.expiration_date,
            "administered_by_staff_id": self.administered_by_staff_id,
            "site": self.site,
        }


@dataclass
class Encounter(BaseEntity):
    """Clinical Encounter Aggregate Root linking patient, clinician, and care episode."""

    patient_id: str = ""
    attending_doctor_id: str = ""
    encounter_type: EncounterType = EncounterType.OUTPATIENT
    status: EncounterStatus = EncounterStatus.PLANNED
    start_time: str = field(default_factory=current_timestamp_iso)
    end_time: Optional[str] = None
    chief_complaint: str = ""
    vitals: Optional[Vitals] = None
    diagnoses: List[Diagnosis] = field(default_factory=list)
    clinical_note: Optional[ClinicalNote] = None
    immunizations: List[Immunization] = field(default_factory=list)
    prescription_ids: List[str] = field(default_factory=list)
    lab_order_ids: List[str] = field(default_factory=list)
    discharge_summary: Optional[str] = None

    def start_encounter(self) -> None:
        self.status = EncounterStatus.IN_PROGRESS
        self.start_time = current_timestamp_iso()
        self.mark_updated()

    def complete_encounter(self, discharge_summary: str = "") -> None:
        self.status = EncounterStatus.DISCHARGED
        self.end_time = current_timestamp_iso()
        self.discharge_summary = discharge_summary
        self.mark_updated()

    def attach_vitals(self, vitals: Vitals) -> None:
        self.vitals = vitals
        self.mark_updated()

    def add_diagnosis(self, diagnosis: Diagnosis) -> None:
        if diagnosis.is_primary:
            for d in self.diagnoses:
                d.is_primary = False
        self.diagnoses.append(diagnosis)
        self.mark_updated()

    def set_soap_note(self, note: ClinicalNote) -> None:
        self.clinical_note = note
        self.mark_updated()
