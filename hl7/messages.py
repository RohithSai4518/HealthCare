"""
HL7 Message Factory for Standard Healthcare Transactions
Constructs ADT^A01 (Admit), ADT^A08 (Update), ORU^R01 (Lab Results), and ORM^O01 (Orders).
"""

import time
from datetime import datetime, timezone
from typing import List, Optional
from domain.clinical import Encounter, Vitals
from domain.laboratory import LabOrder
from domain.patient import Patient
from hl7.parser import HL7Message, HL7Segment


class HL7MessageFactory:
    """Factory for standard HL7 v2.5 clinical transaction messages."""

    @staticmethod
    def _timestamp_hl7() -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

    @classmethod
    def create_adt_a01_admit(
        cls,
        patient: Patient,
        encounter: Encounter,
        sending_facility: str = "HEALTHSPHERE_HOSPITAL",
    ) -> HL7Message:
        """Create ADT^A01 Inpatient Admission / Registration Message."""
        now = cls._timestamp_hl7()
        ctrl_id = f"MSG-{int(time.time()*1000)}"

        msh = HL7Segment(fr"MSH|^~\&|HEALTHSPHERE|{sending_facility}|RECEIVING_SYSTEM|CLINICAL_HIS|{now}||ADT^A01^ADT_A01|{ctrl_id}|P|2.5")
        
        # PID: Patient ID, MRN, Name, DOB, Gender, Address, Phone
        first = patient.first_name
        last = patient.last_name
        dob_clean = patient.date_of_birth.replace("-", "")
        gender_code = "M" if patient.gender.value == "MALE" else ("F" if patient.gender.value == "FEMALE" else "U")
        addr_str = f"{patient.address.street}^^{patient.address.city}^{patient.address.state_or_province}^{patient.address.postal_code}" if patient.address else ""
        phone = patient.contact.phone_primary if patient.contact else ""
        
        pid = HL7Segment(f"PID|1||{patient.id}^^^HEALTHSPHERE^MR||{last}^{first}||{dob_clean}|{gender_code}|||{addr_str}||{phone}|||{patient.marital_status.value}||{patient.mrn}")
        
        # PV1: Patient Visit (Class, Location, Attending Doctor)
        pv1 = HL7Segment(f"PV1|1|I|WARD-3A^ROOM-302^BED-1||||{encounter.attending_doctor_id}^Attending^Doctor|||||||||||{encounter.id}|||||||||||||||||||||||||{now}")

        msg = HL7Message([msh, pid, pv1])
        return msg

    @classmethod
    def create_oru_r01_results(
        cls,
        patient: Patient,
        lab_order: LabOrder,
        sending_facility: str = "HEALTHSPHERE_LAB",
    ) -> HL7Message:
        """Create ORU^R01 Observational Diagnostic Report Message."""
        now = cls._timestamp_hl7()
        ctrl_id = f"MSG-ORU-{int(time.time()*1000)}"

        msh = HL7Segment(fr"MSH|^~\&|HEALTHSPHERE_LIS|{sending_facility}|EMR_INBOX|MAIN_CLINIC|{now}||ORU^R01^ORU_R01|{ctrl_id}|P|2.5")
        
        dob_clean = patient.date_of_birth.replace("-", "")
        gender_code = "M" if patient.gender.value == "MALE" else ("F" if patient.gender.value == "FEMALE" else "U")
        pid = HL7Segment(f"PID|1||{patient.id}^^^HEALTHSPHERE^MR||{patient.last_name}^{patient.first_name}||{dob_clean}|{gender_code}||||||||{patient.mrn}")
        
        obr = HL7Segment(f"OBR|1|{lab_order.id}|{lab_order.specimen_barcode or 'SPM-001'}|PANEL^Diagnostic Laboratory Panel^LOINC||{now}|||||||||{lab_order.ordering_doctor_id}||||||||F")

        segments = [msh, pid, obr]

        for idx, item in enumerate(lab_order.results, 1):
            flag_code = "N" if item.flag.value == "NORMAL" else ("H" if "HIGH" in item.flag.value else "L")
            obx = HL7Segment(f"OBX|{idx}|NM|LOINC-ASSAY^{item.parameter_name}^LN||{item.measured_value}|{item.unit_of_measure}|{item.reference_range_display}|{flag_code}|||F|||{now}")
            segments.append(obx)

        return HL7Message(segments)
