"""
Unit Tests for EDI X12 837P and 835 Subsystems
"""

import unittest
from domain.billing import InsuranceClaim, Invoice, InvoiceItem
from domain.models import InsurancePolicy
from domain.patient import Patient
from edi_x12.x12_835 import X12_835_Parser
from edi_x12.x12_837p import X12_837P_Builder


class TestEDIX12(unittest.TestCase):

    def test_837p_claim_construction(self):
        ins = InsurancePolicy(
            provider_name="Medicare Part B",
            policy_number="MED-1234",
            group_number="GRP-01",
            subscriber_id="SUB-99",
            co_pay_amount=20.0,
            coverage_percentage=0.8,
            deductible=100.0,
        )
        patient = Patient(first_name="Thomas", last_name="Edison", date_of_birth="1950-02-11", insurance=ins)
        invoice = Invoice(
            patient_id=patient.id,
            items=[InvoiceItem(item_code="99213", description="Office Visit", quantity=1, unit_price=115.0)],
        )
        claim = InsuranceClaim(
            claim_number="CLM-8833",
            invoice_id=invoice.id,
            patient_id=patient.id,
            total_claim_amount=92.0,
        )

        edi_str = X12_837P_Builder.build_837p(claim, invoice, patient)
        self.assertIn("ISA*", edi_str)
        self.assertIn("ST*837*", edi_str)
        self.assertIn("CLM*CLM-8833*", edi_str)
        self.assertIn("IEA*", edi_str)

    def test_835_remittance_parser(self):
        raw_835 = """ISA*00*          *00*          *ZZ*PAYER          *ZZ*HEALTHSPHERE   *260828*1000*^*00501*000000001*0*P*:~
BPR*I*1500.00*C*ACH*CTX*01*999999999*DA*12345678*1999999999**01*999999999*DA*87654321*20260828~
TRN*1*CHK12345678*1999999999~
N1*PR*BLUE CROSS SYNTHETIC~
CLP*CLM-1001*1*250.00*200.00*50.00*MC*123456789~
CLP*CLM-1002*1*500.00*450.00*50.00*MC*987654321~
SE*10*0001~"""
        res = X12_835_Parser.parse_835(raw_835)
        self.assertEqual(res["total_paid_amount"], 1500.00)
        self.assertEqual(res["check_trace_number"], "CHK12345678")
        self.assertEqual(len(res["claims_processed"]), 2)


if __name__ == "__main__":
    unittest.main()
