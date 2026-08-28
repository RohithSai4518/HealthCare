"""
HL7 Conformance and Cardinality Validator
Validates mandatory clinical segment presence and syntactic conformance.
"""

from typing import List, Tuple
from hl7.parser import HL7Message


class HL7Validator:
    """Validates HL7 v2 messages against healthcare compliance profiles."""

    @staticmethod
    def validate(message: HL7Message) -> Tuple[bool, List[str]]:
        errors = []

        msh = message.get_segment("MSH")
        if not msh:
            errors.append("MSH (Message Header) segment is mandatory and missing.")
            return False, errors

        if not msh.get_field(9):
            errors.append("MSH-9 (Message Type) is required.")
        if not msh.get_field(10):
            errors.append("MSH-10 (Message Control ID) is required.")
        if not msh.get_field(12):
            errors.append("MSH-12 (HL7 Version ID) is required.")

        msg_type = msh.get_field(9)
        if "ADT" in msg_type:
            if not message.get_segment("PID"):
                errors.append("PID (Patient Identification) segment is mandatory for ADT messages.")
            if not message.get_segment("PV1"):
                errors.append("PV1 (Patient Visit) segment is mandatory for ADT admission/transfer messages.")

        elif "ORM" in msg_type:
            if not message.get_segment("PID"):
                errors.append("PID segment is mandatory for ORM order messages.")
            if not message.get_segment("ORC"):
                errors.append("ORC (Common Order) segment is mandatory for ORM messages.")

        elif "ORU" in msg_type:
            if not message.get_segment("PID"):
                errors.append("PID segment is mandatory for ORU result messages.")
            if not message.get_segment("OBR"):
                errors.append("OBR (Observation Request) segment is mandatory for ORU result messages.")
            if not message.get_segment("OBX"):
                errors.append("At least one OBX (Observation/Result) segment is required for ORU messages.")

        return len(errors) == 0, errors
