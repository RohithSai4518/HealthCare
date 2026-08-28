"""
ANSI ASC X12 835 (Electronic Remittance Advice / Payment) Parser
Parses claim payment adjustments, ERA check amounts, and payer adjudication codes.
"""

from typing import Dict, List, Any


class X12_835_Parser:
    """Parses EDI 835 Remittance Advice payloads."""

    @staticmethod
    def parse_835(raw_835: str) -> Dict[str, Any]:
        lines = [line.strip().rstrip("~") for line in raw_835.replace("\r", "").split("\n") if line.strip()]
        
        summary = {
            "payer_name": "",
            "check_trace_number": "",
            "total_paid_amount": 0.0,
            "claims_processed": [],
        }

        for line in lines:
            parts = line.split("*")
            seg = parts[0]

            if seg == "BPR" and len(parts) >= 3:
                summary["total_paid_amount"] = float(parts[2])
            elif seg == "TRN" and len(parts) >= 3:
                summary["check_trace_number"] = parts[2]
            elif seg == "N1" and len(parts) >= 3 and parts[1] == "PR":
                summary["payer_name"] = parts[2]
            elif seg == "CLP" and len(parts) >= 5:
                claim_id = parts[1]
                status_code = parts[2]
                billed = float(parts[3])
                paid = float(parts[4])
                summary["claims_processed"].append({
                    "claim_id": claim_id,
                    "status_code": status_code,
                    "total_billed": billed,
                    "total_paid": paid,
                })

        return summary
