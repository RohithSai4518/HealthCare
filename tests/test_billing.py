"""
Unit Tests for HealthSphere Billing & Insurance Claims Subsystem
"""

import unittest
from core.enums import ClaimStatus, Gender, InvoiceStatus, PaymentMethod
from domain.models import InsurancePolicy
from repositories.memory_repo import ClaimRepository, InvoiceRepository, PatientRepository
from services.billing_service import BillingService
from services.patient_service import PatientService


class TestBillingService(unittest.TestCase):

    def setUp(self):
        self.invoice_repo = InvoiceRepository()
        self.claim_repo = ClaimRepository()
        self.patient_repo = PatientRepository()

        self.patient_service = PatientService(self.patient_repo)
        self.billing_service = BillingService(
            self.invoice_repo, self.claim_repo, self.patient_repo
        )

        insurance = InsurancePolicy(
            provider_name="HealthGuard Plus",
            policy_number="POL-998877",
            group_number="GRP-12",
            subscriber_id="SUB-44",
            co_pay_amount=25.0,
            coverage_percentage=0.80,  # 80% coverage
            deductible=100.0,
            deductible_met=100.0,  # deductible satisfied
        )

        self.insured_patient = self.patient_service.register_patient(
            first_name="Diana",
            last_name="Prince",
            date_of_birth="1984-03-22",
            gender=Gender.FEMALE,
            insurance=insurance,
        )

    def test_invoice_creation_with_insurance_split(self):
        # Gross total = $200
        # Patient share: 20% coinsurance ($40) + $25 copay = $65
        # Insurance share: $135
        invoice = self.billing_service.create_invoice(
            patient_id=self.insured_patient.id,
            items_data=[
                {"item_code": "CPT-99214", "description": "Complex Office Visit", "quantity": 1, "unit_price": 200.0}
            ],
        )
        self.assertEqual(invoice.status, InvoiceStatus.ISSUED)
        self.assertEqual(invoice.gross_total, 200.0)
        self.assertEqual(invoice.patient_responsibility, 65.0)
        self.assertEqual(invoice.insurance_responsibility, 135.0)

    def test_payment_and_claim_adjudication(self):
        invoice = self.billing_service.create_invoice(
            patient_id=self.insured_patient.id,
            items_data=[
                {"item_code": "CPT-99214", "description": "Complex Office Visit", "quantity": 1, "unit_price": 200.0}
            ],
        )

        # 1. Patient pays their portion
        payment = self.billing_service.record_payment(
            invoice_id=invoice.id,
            amount=65.0,
            method=PaymentMethod.CREDIT_CARD,
        )
        self.assertEqual(payment.amount_paid, 65.0)

        # 2. File insurance claim for covered portion
        claim = self.billing_service.submit_insurance_claim(invoice_id=invoice.id)
        self.assertEqual(claim.status, ClaimStatus.SUBMITTED)
        self.assertEqual(claim.total_claim_amount, 135.0)

        # 3. Adjudicate claim
        adjudicated = self.billing_service.adjudicate_claim(
            claim_id=claim.id,
            approved_amount=135.0,
            is_approved=True,
            notes="Claim processed and fully approved.",
        )
        self.assertEqual(adjudicated.status, ClaimStatus.APPROVED)
        self.assertEqual(adjudicated.approved_amount, 135.0)


if __name__ == "__main__":
    unittest.main()
