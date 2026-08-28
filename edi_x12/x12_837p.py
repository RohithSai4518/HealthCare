"""
ANSI ASC X12 837P (Health Care Claim: Professional) Transaction Builder
Constructs HIPAA-compliant 5010 837P electronic insurance claim interchanges.
"""

from datetime import datetime, timezone
from typing import List, Optional
from domain.billing import InsuranceClaim, Invoice
from domain.patient import Patient


class X12_837P_Builder:
    """Builds ANSI ASC X12 837P Professional Claim transactions."""

    @staticmethod
    def build_837p(
        claim: InsuranceClaim,
        invoice: Invoice,
        patient: Patient,
        billing_npi: str = "1234567890",
        payer_id: str = "PAYER001",
    ) -> str:
        """Constructs an ANSI X12 837P EDI segment payload."""
        now = datetime.now(timezone.utc)
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%M")
        ctrl_num = f"{int(now.timestamp()) % 1000000000:09d}"

        segments = []

        # ISA: Interchange Control Header
        segments.append(f"ISA*00*          *00*          *ZZ*HEALTHSPHERE   *ZZ*{payer_id:<15}*{now.strftime('%y%m%d')}*{time_str}*^*00501*{ctrl_num}*0*P*:~")
        
        # GS: Functional Group Header
        segments.append(f"GS*HC*HEALTHSPHERE*{payer_id}*{date_str}*{time_str}*1*X*005010X222A1~")
        
        # ST: Transaction Set Header
        segments.append("ST*837*0001*005010X222A1~")
        
        # BHT: Beginning of Hierarchical Transaction
        segments.append(f"BHT*0019*00*{claim.claim_number}*{date_str}*{time_str}*CH~")
        
        # 1000A Submitter Name
        segments.append("NM1*41*2*HEALTHSPHERE CLINIC*****46*HS_CLINIC_ID~")
        segments.append("PER*IC*BILLING DEPT*TE*5550199100~")
        
        # 1000B Receiver Name
        segments.append(f"NM1*40*2*{patient.insurance.provider_name if patient.insurance else 'PAYER'}*****46*{payer_id}~")
        
        # 2000A Billing Provider Hierarchical Level
        segments.append("HL*1**20*1~")
        segments.append("PRV*BI*PXC*207Q00000X~")
        segments.append(f"NM1*85*2*HEALTHSPHERE MEDICAL GROUP*****XX*{billing_npi}~")
        segments.append("N3*1000 HEALTHCARE BLVD~")
        segments.append("N4*METROPOLIS*CA*90210~")
        
        # 2000B Subscriber Hierarchical Level
        segments.append("HL*2*1*22*0~")
        segments.append("SBR*P*18*******CI~")
        segments.append(f"NM1*IL*1*{patient.last_name}*{patient.first_name}****MI*{patient.insurance.subscriber_id if patient.insurance else 'SUB001'}~")
        if patient.address:
            segments.append(f"N3*{patient.address.street}~")
            segments.append(f"N4*{patient.address.city}*{patient.address.state_or_province}*{patient.address.postal_code}~")
        segments.append(f"DMG*D8*{patient.date_of_birth.replace('-', '')}*{patient.gender.value[0]}~")
        
        # 2300 Claim Information
        segments.append(f"CLM*{claim.claim_number}*{claim.total_claim_amount:.2f}***11:B:1*Y*A*Y*Y~")
        segments.append(f"HI*ABK:I10~")  # Primary diagnosis pointer
        
        # 2400 Service Lines
        for idx, item in enumerate(invoice.items, 1):
            segments.append(f"LX*{idx}~")
            segments.append(f"SV1*HC:{item.item_code}*{item.unit_price * item.quantity:.2f}*UN*{item.quantity}***1~")
            segments.append(f"DTP*472*D8*{date_str}~")

        # SE: Transaction Set Trailer
        segments.append(f"SE*{len(segments)-2}*0001~")
        
        # GE: Functional Group Trailer
        segments.append("GE*1*1~")
        
        # IEA: Interchange Control Trailer
        segments.append(f"IEA*1*{ctrl_num}~")

        return "\n".join(segments)
