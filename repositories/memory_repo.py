"""
HealthSphere Thread-Safe In-Memory Repository Implementations
Production-grade, zero-dependency persistence layer with indexing and lock synchronization.
"""

from dataclasses import dataclass
import threading
from typing import Callable, Dict, Generic, List, Optional, TypeVar
from core.enums import UserRole
from core.exceptions import EntityNotFoundError
from domain.appointments import Appointment, Doctor
from domain.billing import InsuranceClaim, Invoice
from domain.clinical import Encounter
from domain.laboratory import LabOrder, LabTestType
from domain.models import BaseEntity
from domain.patient import Patient
from domain.pharmacy import Medication, PharmacyInventoryItem, Prescription
from repositories.base import IRepository

T = TypeVar("T", bound=BaseEntity)


class ThreadSafeMemoryRepository(IRepository[T], Generic[T]):
    """Generic thread-safe in-memory store."""

    def __init__(self, entity_name: str = "Entity"):
        self._storage: Dict[str, T] = {}
        self._lock = threading.RLock()
        self._entity_name = entity_name

    def save(self, entity: T) -> T:
        with self._lock:
            entity.mark_updated()
            self._storage[entity.id] = entity
            return entity

    def get_by_id(self, entity_id: str) -> Optional[T]:
        with self._lock:
            entity = self._storage.get(entity_id)
            if entity and entity.is_active:
                return entity
            return None

    def get_by_id_or_raise(self, entity_id: str) -> T:
        entity = self.get_by_id(entity_id)
        if not entity:
            raise EntityNotFoundError(self._entity_name, entity_id)
        return entity

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        with self._lock:
            active_items = [e for e in self._storage.values() if e.is_active]
            return active_items[skip : skip + limit]

    def find(self, predicate: Callable[[T], bool], skip: int = 0, limit: int = 100) -> List[T]:
        with self._lock:
            matched = [e for e in self._storage.values() if e.is_active and predicate(e)]
            return matched[skip : skip + limit]

    def delete(self, entity_id: str, hard_delete: bool = False) -> bool:
        with self._lock:
            if entity_id not in self._storage:
                return False
            if hard_delete:
                del self._storage[entity_id]
            else:
                self._storage[entity_id].deactivate()
            return True

    def count(self, predicate: Optional[Callable[[T], bool]] = None) -> int:
        with self._lock:
            if predicate is None:
                return sum(1 for e in self._storage.values() if e.is_active)
            return sum(1 for e in self._storage.values() if e.is_active and predicate(e))

    def clear(self) -> None:
        with self._lock:
            self._storage.clear()


class PatientRepository(ThreadSafeMemoryRepository[Patient]):
    """Patient persistence with MRN and name indexing."""

    def __init__(self):
        super().__init__("Patient")

    def get_by_mrn(self, mrn: str) -> Optional[Patient]:
        results = self.find(lambda p: p.mrn.upper() == mrn.strip().upper(), limit=1)
        return results[0] if results else None

    def search_by_name(self, query: str, limit: int = 50) -> List[Patient]:
        q = query.strip().lower()
        return self.find(
            lambda p: q in p.first_name.lower() or q in p.last_name.lower() or q in p.mrn.lower(),
            limit=limit,
        )


class DoctorRepository(ThreadSafeMemoryRepository[Doctor]):
    """Doctor repository with license and specialty queries."""

    def __init__(self):
        super().__init__("Doctor")

    def get_by_license(self, license_number: str) -> Optional[Doctor]:
        results = self.find(lambda d: d.license_number == license_number, limit=1)
        return results[0] if results else None

    def get_by_specialty(self, specialty: str) -> List[Doctor]:
        s = specialty.strip().lower()
        return self.find(lambda d: s in d.specialty.lower())


class AppointmentRepository(ThreadSafeMemoryRepository[Appointment]):
    """Appointment repository with doctor, patient, and date queries."""

    def __init__(self):
        super().__init__("Appointment")

    def get_by_patient(self, patient_id: str) -> List[Appointment]:
        return self.find(lambda a: a.patient_id == patient_id)

    def get_by_doctor(self, doctor_id: str) -> List[Appointment]:
        return self.find(lambda a: a.doctor_id == doctor_id)

    def get_by_slot(self, slot_id: str) -> Optional[Appointment]:
        results = self.find(lambda a: a.slot_id == slot_id, limit=1)
        return results[0] if results else None


class EncounterRepository(ThreadSafeMemoryRepository[Encounter]):
    """Clinical encounter repository."""

    def __init__(self):
        super().__init__("Encounter")

    def get_by_patient(self, patient_id: str) -> List[Encounter]:
        return self.find(lambda e: e.patient_id == patient_id)

    def get_by_doctor(self, doctor_id: str) -> List[Encounter]:
        return self.find(lambda e: e.attending_doctor_id == doctor_id)


class MedicationRepository(ThreadSafeMemoryRepository[Medication]):
    """Medication formulary repository."""

    def __init__(self):
        super().__init__("Medication")

    def get_by_ndc(self, ndc: str) -> Optional[Medication]:
        results = self.find(lambda m: m.ndc_code == ndc, limit=1)
        return results[0] if results else None

    def search_medications(self, query: str) -> List[Medication]:
        q = query.strip().lower()
        return self.find(lambda m: q in m.generic_name.lower() or q in m.brand_name.lower())


class PrescriptionRepository(ThreadSafeMemoryRepository[Prescription]):
    """Prescription records repository."""

    def __init__(self):
        super().__init__("Prescription")

    def get_by_patient(self, patient_id: str) -> List[Prescription]:
        return self.find(lambda p: p.patient_id == patient_id)


class InventoryRepository(ThreadSafeMemoryRepository[PharmacyInventoryItem]):
    """Pharmacy stock inventory repository."""

    def __init__(self):
        super().__init__("PharmacyInventoryItem")

    def get_by_medication(self, medication_id: str) -> List[PharmacyInventoryItem]:
        return self.find(lambda item: item.medication_id == medication_id)

    def get_total_stock(self, medication_id: str) -> int:
        batches = self.get_by_medication(medication_id)
        return sum(b.quantity_on_hand for b in batches)


class LabTestTypeRepository(ThreadSafeMemoryRepository[LabTestType]):
    """Laboratory test definition repository."""

    def __init__(self):
        super().__init__("LabTestType")

    def get_by_code(self, code: str) -> Optional[LabTestType]:
        results = self.find(lambda t: t.code.upper() == code.strip().upper(), limit=1)
        return results[0] if results else None


class LabOrderRepository(ThreadSafeMemoryRepository[LabOrder]):
    """Laboratory orders repository."""

    def __init__(self):
        super().__init__("LabOrder")

    def get_by_patient(self, patient_id: str) -> List[LabOrder]:
        return self.find(lambda o: o.patient_id == patient_id)

    def get_by_barcode(self, barcode: str) -> Optional[LabOrder]:
        results = self.find(lambda o: o.specimen_barcode == barcode, limit=1)
        return results[0] if results else None


class InvoiceRepository(ThreadSafeMemoryRepository[Invoice]):
    """Billing invoices repository."""

    def __init__(self):
        super().__init__("Invoice")

    def get_by_patient(self, patient_id: str) -> List[Invoice]:
        return self.find(lambda inv: inv.patient_id == patient_id)

    def get_by_number(self, invoice_number: str) -> Optional[Invoice]:
        results = self.find(lambda inv: inv.invoice_number == invoice_number, limit=1)
        return results[0] if results else None


class ClaimRepository(ThreadSafeMemoryRepository[InsuranceClaim]):
    """Insurance claims repository."""

    def __init__(self):
        super().__init__("InsuranceClaim")

    def get_by_patient(self, patient_id: str) -> List[InsuranceClaim]:
        return self.find(lambda c: c.patient_id == patient_id)

    def get_by_invoice(self, invoice_id: str) -> Optional[InsuranceClaim]:
        results = self.find(lambda c: c.invoice_id == invoice_id, limit=1)
        return results[0] if results else None


@dataclass
class UserAccount(BaseEntity):
    """User account entity for authentication."""

    username: str = ""
    password_hash: str = ""
    role: UserRole = UserRole.PATIENT
    linked_entity_id: Optional[str] = None  # doctor_id or patient_id


class UserRepository(ThreadSafeMemoryRepository[UserAccount]):
    """User authentication store."""

    def __init__(self):
        super().__init__("UserAccount")

    def get_by_username(self, username: str) -> Optional[UserAccount]:
        results = self.find(lambda u: u.username.lower() == username.strip().lower(), limit=1)
        return results[0] if results else None
