"""
HealthSphere Core Enumerations
Defines standardized domain status codes, clinical types, roles, and action classifications.
"""

from enum import Enum, unique


@unique
class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


@unique
class BloodGroup(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    UNKNOWN = "UNKNOWN"


@unique
class MaritalStatus(str, Enum):
    SINGLE = "SINGLE"
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"
    WIDOWED = "WIDOWED"
    SEPARATED = "SEPARATED"


@unique
class AppointmentStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"


@unique
class AppointmentType(str, Enum):
    ROUTINE_CHECKUP = "ROUTINE_CHECKUP"
    FOLLOW_UP = "FOLLOW_UP"
    EMERGENCY = "EMERGENCY"
    SPECIALIST_CONSULTATION = "SPECIALIST_CONSULTATION"
    TELEMEDICINE = "TELEMEDICINE"


@unique
class EncounterType(str, Enum):
    OUTPATIENT = "OUTPATIENT"
    INPATIENT = "INPATIENT"
    EMERGENCY = "EMERGENCY"
    TELEHEALTH = "TELEHEALTH"
    HOME_HEALTH = "HOME_HEALTH"


@unique
class EncounterStatus(str, Enum):
    PLANNED = "PLANNED"
    ARRIVED = "ARRIVED"
    TRIAGED = "TRIAGED"
    IN_PROGRESS = "IN_PROGRESS"
    ON_HOLD = "ON_HOLD"
    DISCHARGED = "DISCHARGED"
    CANCELLED = "CANCELLED"


@unique
class AllergySeverity(str, Enum):
    MILD = "MILD"
    MODERATE = "MODERATE"
    SEVERE = "SEVERE"
    LIFE_THREATENING = "LIFE_THREATENING"


@unique
class AllergyCategory(str, Enum):
    FOOD = "FOOD"
    MEDICATION = "MEDICATION"
    ENVIRONMENTAL = "ENVIRONMENTAL"
    BIOLOGICAL = "BIOLOGICAL"
    OTHER = "OTHER"


@unique
class PrescriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISPENSED = "DISPENSED"
    PARTIALLY_DISPENSED = "PARTIALLY_DISPENSED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"


@unique
class DrugForm(str, Enum):
    TABLET = "TABLET"
    CAPSULE = "CAPSULE"
    SYRUP = "SYRUP"
    INJECTION = "INJECTION"
    OINTMENT = "OINTMENT"
    DROPS = "DROPS"
    INHALER = "INHALER"
    PATCH = "PATCH"


@unique
class InteractionSeverity(str, Enum):
    MINOR = "MINOR"
    MODERATE = "MODERATE"
    MAJOR = "MAJOR"
    CONTRAINDICATED = "CONTRAINDICATED"


@unique
class LabTestCategory(str, Enum):
    HEMATOLOGY = "HEMATOLOGY"
    BIOCHEMISTRY = "BIOCHEMISTRY"
    MICROBIOLOGY = "MICROBIOLOGY"
    IMMUNOLOGY = "IMMUNOLOGY"
    PATHOLOGY = "PATHOLOGY"
    RADIOLOGY = "RADIOLOGY"
    URINALYSIS = "URINALYSIS"


@unique
class LabOrderStatus(str, Enum):
    ORDERED = "ORDERED"
    SAMPLE_COLLECTED = "SAMPLE_COLLECTED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


@unique
class AbnormalityFlag(str, Enum):
    NORMAL = "NORMAL"
    LOW = "LOW"
    HIGH = "HIGH"
    CRITICAL_LOW = "CRITICAL_LOW"
    CRITICAL_HIGH = "CRITICAL_HIGH"
    ABNORMAL = "ABNORMAL"


@unique
class InvoiceStatus(str, Enum):
    DRAFT = "DRAFT"
    ISSUED = "ISSUED"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
    REFUNDED = "REFUNDED"


@unique
class PaymentMethod(str, Enum):
    CASH = "CASH"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    INSURANCE = "INSURANCE"
    BANK_TRANSFER = "BANK_TRANSFER"
    ONLINE_PORTAL = "ONLINE_PORTAL"


@unique
class ClaimStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    PARTIALLY_APPROVED = "PARTIALLY_APPROVED"
    DENIED = "DENIED"
    APPEALED = "APPEALED"


@unique
class UserRole(str, Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"
    PHARMACIST = "PHARMACIST"
    LAB_TECHNICIAN = "LAB_TECHNICIAN"
    BILLING_OFFICER = "BILLING_OFFICER"
    RECEPTIONIST = "RECEPTIONIST"
    PATIENT = "PATIENT"


@unique
class AuditAction(str, Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    DISPENSE = "DISPENSE"
    ADJUDICATE = "ADJUDICATE"
    EXPORT = "EXPORT"
