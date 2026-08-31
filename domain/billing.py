"""
HealthSphere Billing & Financial Domain Models
Fee schedules, invoices, payments, and insurance claim adjudication state machines.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.enums import ClaimStatus, InvoiceStatus, PaymentMethod
from domain.models import BaseEntity, current_timestamp_iso


@dataclass
class InvoiceItem:
    """Line item in a healthcare billing invoice."""

    item_code: str  # CPT code, NDC, or service code
    description: str
    quantity: int
    unit_price: float
    discount_amount: float = 0.0

    @property
    def total_price(self) -> float:
        gross = self.quantity * self.unit_price
        return max(0.0, gross - self.discount_amount)

    def to_dict(self) -> dict:
        return {
            "item_code": self.item_code,
            "description": self.description,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "discount_amount": self.discount_amount,
            "total_price": self.total_price,
        }


@dataclass
class Payment(BaseEntity):
    """Financial transaction recording payment receipt."""

    invoice_id: str = ""
    patient_id: str = ""
    amount_paid: float = 0.0
    payment_method: PaymentMethod = PaymentMethod.CASH
    transaction_reference: str = ""
    payment_date: str = field(default_factory=current_timestamp_iso)
    notes: Optional[str] = None


@dataclass
class Invoice(BaseEntity):
    """Patient billing invoice aggregate root."""

    invoice_number: str = ""
    patient_id: str = ""
    encounter_id: Optional[str] = None
    status: InvoiceStatus = InvoiceStatus.DRAFT
    issue_date: str = field(default_factory=current_timestamp_iso)
    due_date: str = ""
    items: List[InvoiceItem] = field(default_factory=list)
    payments: List[Payment] = field(default_factory=list)
    insurance_claim_id: Optional[str] = None
    patient_responsibility: float = 0.0
    insurance_responsibility: float = 0.0
    tax_amount: float = 0.0

    @property
    def gross_total(self) -> float:
        return sum(item.total_price for item in self.items)

    @property
    def net_total(self) -> float:
        return round(self.gross_total + self.tax_amount, 2)

    @property
    def total_paid(self) -> float:
        return sum(payment.amount_paid for payment in self.payments)

    @property
    def balance_due(self) -> float:
        return max(0.0, round(self.patient_responsibility - self.total_paid, 2))

    def add_item(self, item: InvoiceItem) -> None:
        self.items.append(item)
        self.patient_responsibility = self.net_total
        self.mark_updated()

    def record_payment(self, payment: Payment) -> None:
        self.payments.append(payment)
        if self.balance_due <= 0.01:
            self.status = InvoiceStatus.PAID
        else:
            self.status = InvoiceStatus.PARTIALLY_PAID
        self.mark_updated()


@dataclass
class InsuranceClaim(BaseEntity):
    """Health insurance reimbursement claim filing."""

    claim_number: str = ""
    invoice_id: str = ""
    patient_id: str = ""
    provider_id: str = ""
    insurance_policy_number: str = ""
    status: ClaimStatus = ClaimStatus.SUBMITTED
    total_claim_amount: float = 0.0
    approved_amount: float = 0.0
    adjudication_date: Optional[str] = None
    denial_reason: Optional[str] = None
    payer_notes: Optional[str] = None

    def approve(self, amount: float, notes: Optional[str] = None) -> None:
        self.status = ClaimStatus.APPROVED if amount >= self.total_claim_amount else ClaimStatus.PARTIALLY_APPROVED
        self.approved_amount = round(amount, 2)
        self.adjudication_date = current_timestamp_iso()
        self.payer_notes = notes
        self.mark_updated()

    def deny(self, reason: str) -> None:
        self.status = ClaimStatus.DENIED
        self.approved_amount = 0.0
        self.denial_reason = reason
        self.adjudication_date = current_timestamp_iso()
        self.mark_updated()
