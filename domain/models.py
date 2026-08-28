"""
HealthSphere Domain Foundation Models
Base entities, value objects, address structures, and common primitives.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Optional
import uuid


def generate_uuid() -> str:
    """Generate RFC 4122 compliant unique identifier."""
    return str(uuid.uuid4())


def current_timestamp_iso() -> str:
    """Get current UTC timestamp formatted as ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat()


@dataclass
class BaseEntity:
    """Base class for all identifiable domain models."""

    id: str = field(default_factory=generate_uuid)
    created_at: str = field(default_factory=current_timestamp_iso)
    updated_at: str = field(default_factory=current_timestamp_iso)
    is_active: bool = True

    def mark_updated(self) -> None:
        self.updated_at = current_timestamp_iso()

    def deactivate(self) -> None:
        self.is_active = False
        self.mark_updated()

    def to_dict(self) -> Dict[str, Any]:
        result = {}
        for key, value in self.__dict__.items():
            if hasattr(value, "to_dict"):
                result[key] = value.to_dict()
            elif hasattr(value, "value"):  # Enum
                result[key] = value.value
            elif isinstance(value, list):
                result[key] = [item.to_dict() if hasattr(item, "to_dict") else (item.value if hasattr(item, "value") else item) for item in value]
            elif isinstance(value, dict):
                result[key] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for k, v in value.items()}
            else:
                result[key] = value
        return result


@dataclass
class Address:
    """Standardized physical address value object."""

    street: str
    city: str
    state_or_province: str
    postal_code: str
    country: str = "US"
    apartment_or_suite: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "street": self.street,
            "apartment_or_suite": self.apartment_or_suite,
            "city": self.city,
            "state_or_province": self.state_or_province,
            "postal_code": self.postal_code,
            "country": self.country,
        }

    def formatted(self) -> str:
        apt = f", {self.apartment_or_suite}" if self.apartment_or_suite else ""
        return f"{self.street}{apt}, {self.city}, {self.state_or_province} {self.postal_code}, {self.country}"


@dataclass
class ContactInfo:
    """Contact details value object."""

    phone_primary: str
    phone_secondary: Optional[str] = None
    email: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "phone_primary": self.phone_primary,
            "phone_secondary": self.phone_secondary,
            "email": self.email,
        }


@dataclass
class InsurancePolicy:
    """Health insurance policy representation."""

    provider_name: str
    policy_number: str
    group_number: str
    subscriber_id: str
    co_pay_amount: float
    coverage_percentage: float  # e.g., 0.80 for 80% coverage
    deductible: float
    deductible_met: float = 0.0
    effective_start: str = "2024-01-01"
    effective_end: str = "2029-12-31"

    def calculate_patient_responsibility(self, total_charge: float) -> tuple[float, float]:
        """
        Calculates (patient_share, insurance_share).
        Respects deductible and co-pay parameters.
        """
        remaining_deductible = max(0.0, self.deductible - self.deductible_met)
        deductible_portion = min(total_charge, remaining_deductible)
        charge_after_deductible = max(0.0, total_charge - deductible_portion)

        insurance_covered = charge_after_deductible * self.coverage_percentage
        patient_coinsurance = charge_after_deductible * (1.0 - self.coverage_percentage)
        total_patient_share = deductible_portion + patient_coinsurance + self.co_pay_amount

        # Patient cannot pay more than total charge
        total_patient_share = min(total_charge, total_patient_share)
        total_insurance_share = max(0.0, total_charge - total_patient_share)

        return round(total_patient_share, 2), round(total_insurance_share, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "provider_name": self.provider_name,
            "policy_number": self.policy_number,
            "group_number": self.group_number,
            "subscriber_id": self.subscriber_id,
            "co_pay_amount": self.co_pay_amount,
            "coverage_percentage": self.coverage_percentage,
            "deductible": self.deductible,
            "deductible_met": self.deductible_met,
            "effective_start": self.effective_start,
            "effective_end": self.effective_end,
        }
