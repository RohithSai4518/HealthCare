"""
HealthSphere Pharmacy Domain Models
Medications, Drug Interaction Matrix, Prescriptions, Dispensation, and Inventory Management.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.enums import DrugForm, InteractionSeverity, PrescriptionStatus
from domain.models import BaseEntity, current_timestamp_iso


@dataclass
class Medication(BaseEntity):
    """Pharmaceutical product / drug definition."""

    ndc_code: str = ""  # National Drug Code
    generic_name: str = ""
    brand_name: str = ""
    form: DrugForm = DrugForm.TABLET
    strength: str = "500mg"
    unit_price: float = 10.0
    requires_prescription: bool = True
    storage_conditions: str = "Store at room temperature 15-25°C"
    active_ingredients: List[str] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        return f"{self.brand_name} ({self.generic_name}) {self.strength} {self.form.value}"


@dataclass
class DrugInteraction:
    """Pairwise drug-to-drug interaction rule."""

    drug_name_a: str
    drug_name_b: str
    severity: InteractionSeverity
    clinical_effect: str
    management_recommendation: str

    def matches(self, drug_1: str, drug_2: str) -> bool:
        d1, d2 = drug_1.strip().lower(), drug_2.strip().lower()
        a, b = self.drug_name_a.lower(), self.drug_name_b.lower()
        return (d1 == a and d2 == b) or (d1 == b and d2 == a)

    def to_dict(self) -> dict:
        return {
            "drug_name_a": self.drug_name_a,
            "drug_name_b": self.drug_name_b,
            "severity": self.severity.value if isinstance(self.severity, InteractionSeverity) else self.severity,
            "clinical_effect": self.clinical_effect,
            "management_recommendation": self.management_recommendation,
        }


@dataclass
class PrescriptionItem:
    """Line item in a clinical prescription."""

    medication_id: str
    medication_name: str
    dosage_instruction: str  # e.g., "1 tablet after meals"
    frequency_per_day: int  # e.g., 2
    duration_days: int  # e.g., 7
    total_quantity: int  # e.g., 14
    refills_authorized: int = 0
    refills_remaining: int = 0
    is_dispensed: bool = False
    dispensed_quantity: int = 0

    def to_dict(self) -> dict:
        return {
            "medication_id": self.medication_id,
            "medication_name": self.medication_name,
            "dosage_instruction": self.dosage_instruction,
            "frequency_per_day": self.frequency_per_day,
            "duration_days": self.duration_days,
            "total_quantity": self.total_quantity,
            "refills_authorized": self.refills_authorized,
            "refills_remaining": self.refills_remaining,
            "is_dispensed": self.is_dispensed,
            "dispensed_quantity": self.dispensed_quantity,
        }


@dataclass
class Prescription(BaseEntity):
    """Clinical Prescription Aggregate Root."""

    patient_id: str = ""
    prescribing_doctor_id: str = ""
    encounter_id: Optional[str] = None
    status: PrescriptionStatus = PrescriptionStatus.ACTIVE
    items: List[PrescriptionItem] = field(default_factory=list)
    issued_date: str = field(default_factory=current_timestamp_iso)
    expiry_date: str = ""
    clinical_rationale: Optional[str] = None
    dispensed_by_pharmacist_id: Optional[str] = None
    dispensed_timestamp: Optional[str] = None

    def add_item(self, item: PrescriptionItem) -> None:
        self.items.append(item)
        self.mark_updated()

    def mark_dispensed(self, pharmacist_id: str) -> None:
        for item in self.items:
            item.is_dispensed = True
            item.dispensed_quantity = item.total_quantity
        self.status = PrescriptionStatus.DISPENSED
        self.dispensed_by_pharmacist_id = pharmacist_id
        self.dispensed_timestamp = current_timestamp_iso()
        self.mark_updated()


@dataclass
class PharmacyInventoryItem(BaseEntity):
    """Stock tracking for physical medication batches."""

    medication_id: str = ""
    batch_number: str = ""
    quantity_on_hand: int = 0
    reorder_threshold: int = 50
    unit_cost: float = 5.0
    expiry_date: str = "2027-12-31"

    @property
    def is_low_stock(self) -> bool:
        return self.quantity_on_hand <= self.reorder_threshold

    def deduct(self, amount: int) -> None:
        if amount > self.quantity_on_hand:
            raise ValueError(f"Cannot deduct {amount} items from stock of {self.quantity_on_hand}")
        self.quantity_on_hand -= amount
        self.mark_updated()

    def restock(self, amount: int) -> None:
        self.quantity_on_hand += amount
        self.mark_updated()
