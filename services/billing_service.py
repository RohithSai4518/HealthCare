"""
HealthSphere Billing & Financial Operations Service
Invoice aggregation, insurance coverage calculations, payment transactions, and claim adjudication.
"""

import time
from typing import List, Optional
from core.audit import audit_service
from core.enums import AuditAction, ClaimStatus, InvoiceStatus, PaymentMethod
from core.exceptions import ClaimAdjudicationError, ConflictError, EntityNotFoundError, ValidationError
from core.security import RBACManager, UserContext
from domain.billing import InsuranceClaim, Invoice, InvoiceItem, Payment
from domain.models import current_timestamp_iso
from repositories.memory_repo import (
    ClaimRepository,
    EncounterRepository,
    InvoiceRepository,
    PatientRepository,
)


class BillingService:
    """Manages healthcare billing cycles, insurance adjudication, and payment processing."""

    def __init__(
        self,
        invoice_repo: InvoiceRepository,
        claim_repo: ClaimRepository,
        patient_repo: PatientRepository,
        encounter_repo: Optional[EncounterRepository] = None,
    ):
        self.invoice_repo = invoice_repo
        self.claim_repo = claim_repo
        self.patient_repo = patient_repo
        self.encounter_repo = encounter_repo

    def _generate_invoice_number(self) -> str:
        count = self.invoice_repo.count() + 1
        return f"INV-{int(time.time())}-{count:04d}"

    def create_invoice(
        self,
        patient_id: str,
        items_data: List[dict],  # list of {"item_code": str, "description": str, "quantity": int, "unit_price": float}
        encounter_id: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> Invoice:
        """Generates patient invoice and automatically splits liability if insurance policy exists."""
        if context:
            RBACManager.check_permission(context, "billing:write")

        patient = self.patient_repo.get_by_id_or_raise(patient_id)
        if not items_data:
            raise ValidationError("Invoice must contain at least one line item.")

        invoice_items: List[InvoiceItem] = []
        for item in items_data:
            invoice_items.append(
                InvoiceItem(
                    item_code=item["item_code"],
                    description=item["description"],
                    quantity=int(item["quantity"]),
                    unit_price=float(item["unit_price"]),
                    discount_amount=float(item.get("discount_amount", 0.0)),
                )
            )

        invoice_num = self._generate_invoice_number()
        invoice = Invoice(
            invoice_number=invoice_num,
            patient_id=patient_id,
            encounter_id=encounter_id,
            status=InvoiceStatus.ISSUED,
            items=invoice_items,
        )

        gross = invoice.gross_total
        if patient.insurance:
            patient_share, ins_share = patient.insurance.calculate_patient_responsibility(gross)
            invoice.patient_responsibility = patient_share
            invoice.insurance_responsibility = ins_share
        else:
            invoice.patient_responsibility = gross
            invoice.insurance_responsibility = 0.0

        saved_invoice = self.invoice_repo.save(invoice)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="Invoice",
            resource_id=saved_invoice.id,
            details={"invoice_number": invoice_num, "total": str(invoice.net_total)},
        )

        return saved_invoice

    def record_payment(
        self,
        invoice_id: str,
        amount: float,
        method: PaymentMethod = PaymentMethod.CREDIT_CARD,
        transaction_ref: Optional[str] = None,
        notes: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> Payment:
        """Processes and applies payment against an issued invoice."""
        if context:
            RBACManager.check_permission(context, "billing:payment")

        invoice = self.invoice_repo.get_by_id_or_raise(invoice_id)
        if invoice.status == InvoiceStatus.PAID:
            raise ConflictError("Invoice is already fully settled.")

        if amount <= 0:
            raise ValidationError("Payment amount must be greater than zero.")

        ref = transaction_ref or f"TXN-{int(time.time()*1000)}"
        payment = Payment(
            invoice_id=invoice_id,
            patient_id=invoice.patient_id,
            amount_paid=round(amount, 2),
            payment_method=method,
            transaction_reference=ref,
            notes=notes,
        )

        invoice.record_payment(payment)
        self.invoice_repo.save(invoice)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.UPDATE,
            resource_type="Invoice",
            resource_id=invoice_id,
            details={"action": "PAYMENT_RECORDED", "amount": str(amount), "status": invoice.status.value},
        )

        return payment

    def submit_insurance_claim(
        self,
        invoice_id: str,
        context: Optional[UserContext] = None,
    ) -> InsuranceClaim:
        """Files an insurance claim for the portion covered by patient policy."""
        if context:
            RBACManager.check_permission(context, "billing:write")

        invoice = self.invoice_repo.get_by_id_or_raise(invoice_id)
        patient = self.patient_repo.get_by_id_or_raise(invoice.patient_id)

        if not patient.insurance:
            raise ValidationError("Patient does not have an active insurance policy on file.")

        if invoice.insurance_responsibility <= 0:
            raise ValidationError("Invoice has no insurance covered portion to file.")

        existing_claim = self.claim_repo.get_by_invoice(invoice_id)
        if existing_claim:
            raise ConflictError(f"Claim already filed for invoice {invoice_id} (Claim #{existing_claim.claim_number})")

        claim_num = f"CLM-{int(time.time())}-{patient.insurance.policy_number[-4:]}"
        claim = InsuranceClaim(
            claim_number=claim_num,
            invoice_id=invoice_id,
            patient_id=patient.id,
            provider_id="HEALTHSPHERE_CLINIC",
            insurance_policy_number=patient.insurance.policy_number,
            status=ClaimStatus.SUBMITTED,
            total_claim_amount=invoice.insurance_responsibility,
        )

        saved_claim = self.claim_repo.save(claim)
        invoice.insurance_claim_id = saved_claim.id
        self.invoice_repo.save(invoice)

        return saved_claim

    def adjudicate_claim(
        self,
        claim_id: str,
        approved_amount: float,
        is_approved: bool,
        notes: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> InsuranceClaim:
        """Payer adjudication state machine processing."""
        if context:
            RBACManager.check_permission(context, "billing:adjudicate")

        claim = self.claim_repo.get_by_id_or_raise(claim_id)
        if claim.status in (ClaimStatus.APPROVED, ClaimStatus.DENIED):
            raise ConflictError(f"Claim is already adjudicated with status {claim.status.value}")

        if is_approved:
            claim.approve(approved_amount, notes)
        else:
            claim.deny(notes or "Claim rejected by payer rules.")

        self.claim_repo.save(claim)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.ADJUDICATE,
            resource_type="InsuranceClaim",
            resource_id=claim_id,
            details={"status": claim.status.value, "approved_amount": str(claim.approved_amount)},
        )

        return claim
