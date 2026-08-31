"""
HealthSphere HL7 v2.5 Master Segment Field Definitions
Complete metadata registry for standard HL7 healthcare message segments.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class HL7FieldDefinition:
    field_index: int
    field_name: str
    data_type: str
    max_length: int
    is_required: bool
    description: str


@dataclass(frozen=True)
class HL7SegmentMetadata:
    segment_id: str
    segment_name: str
    chapter: str
    fields: List[HL7FieldDefinition]


class HL7SegmentRegistry:
    """Complete registry of HL7 v2.5 standard segments."""

    _SEGMENTS: Dict[str, HL7SegmentMetadata] = {}

    @classmethod
    def initialize(cls):
        if cls._SEGMENTS:
            return


        cls._SEGMENTS["MSH"] = HL7SegmentMetadata(
            segment_id="MSH",
            segment_name="Message Header",
            chapter="Control",
            fields=[
                HL7FieldDefinition(field_index=1, field_name="Field Separator", data_type="ST", max_length=1, is_required=True, description="Defines field delimiter"),
                HL7FieldDefinition(field_index=2, field_name="Encoding Characters", data_type="ST", max_length=4, is_required=True, description="Component, repetition, escape, subcomponent delimiters"),
                HL7FieldDefinition(field_index=3, field_name="Sending Application", data_type="HD", max_length=227, is_required=False, description="Originating system name"),
                HL7FieldDefinition(field_index=4, field_name="Sending Facility", data_type="HD", max_length=227, is_required=False, description="Originating hospital/clinic unit"),
                HL7FieldDefinition(field_index=5, field_name="Receiving Application", data_type="HD", max_length=227, is_required=False, description="Destination server"),
                HL7FieldDefinition(field_index=6, field_name="Receiving Facility", data_type="HD", max_length=227, is_required=False, description="Destination healthcare site"),
                HL7FieldDefinition(field_index=7, field_name="Date/Time of Message", data_type="TS", max_length=26, is_required=True, description="Message origination timestamp"),
                HL7FieldDefinition(field_index=8, field_name="Security", data_type="ST", max_length=40, is_required=False, description="Security and authorization credentials"),
                HL7FieldDefinition(field_index=9, field_name="Message Type", data_type="MSG", max_length=15, is_required=True, description="Message trigger event (e.g. ADT^A01)"),
                HL7FieldDefinition(field_index=10, field_name="Message Control ID", data_type="ST", max_length=199, is_required=True, description="Unique transaction identifier"),
                HL7FieldDefinition(field_index=11, field_name="Processing ID", data_type="PT", max_length=3, is_required=True, description="Production (P) or Test (T)"),
                HL7FieldDefinition(field_index=12, field_name="Version ID", data_type="VID", max_length=60, is_required=True, description="HL7 Version (2.5)")
            ],
        )
        cls._SEGMENTS["PID"] = HL7SegmentMetadata(
            segment_id="PID",
            segment_name="Patient Identification",
            chapter="Patient Administration",
            fields=[
                HL7FieldDefinition(field_index=1, field_name="Set ID - PID", data_type="SI", max_length=4, is_required=False, description="Sequence number"),
                HL7FieldDefinition(field_index=2, field_name="Patient ID", data_type="CX", max_length=20, is_required=False, description="External patient identifier"),
                HL7FieldDefinition(field_index=3, field_name="Patient Identifier List", data_type="CX", max_length=250, is_required=True, description="Medical Record Number (MRN)"),
                HL7FieldDefinition(field_index=4, field_name="Alternate Patient ID", data_type="CX", max_length=20, is_required=False, description="Secondary tracking identifier"),
                HL7FieldDefinition(field_index=5, field_name="Patient Name", data_type="XPN", max_length=250, is_required=True, description="Family name, given name, middle initials"),
                HL7FieldDefinition(field_index=6, field_name="Mother's Maiden Name", data_type="XPN", max_length=250, is_required=False, description="Maternal birth family name"),
                HL7FieldDefinition(field_index=7, field_name="Date/Time of Birth", data_type="TS", max_length=26, is_required=False, description="Date of birth (YYYYMMDD)"),
                HL7FieldDefinition(field_index=8, field_name="Administrative Sex", data_type="IS", max_length=1, is_required=False, description="Biological gender (M/F/O/U)"),
                HL7FieldDefinition(field_index=10, field_name="Race", data_type="CE", max_length=250, is_required=False, description="Racial demographic code"),
                HL7FieldDefinition(field_index=11, field_name="Patient Address", data_type="XAD", max_length=250, is_required=False, description="Physical street address"),
                HL7FieldDefinition(field_index=13, field_name="Phone Number - Home", data_type="XTN", max_length=250, is_required=False, description="Primary telephone number"),
                HL7FieldDefinition(field_index=14, field_name="Phone Number - Business", data_type="XTN", max_length=250, is_required=False, description="Workplace contact number"),
                HL7FieldDefinition(field_index=16, field_name="Marital Status", data_type="CE", max_length=250, is_required=False, description="Marital state classification"),
                HL7FieldDefinition(field_index=18, field_name="Patient Account Number", data_type="CX", max_length=250, is_required=False, description="Financial billing account reference"),
                HL7FieldDefinition(field_index=19, field_name="SSN Number - Patient", data_type="ST", max_length=16, is_required=False, description="Social security identifier")
            ],
        )
        cls._SEGMENTS["PV1"] = HL7SegmentMetadata(
            segment_id="PV1",
            segment_name="Patient Visit",
            chapter="Patient Administration",
            fields=[
                HL7FieldDefinition(field_index=1, field_name="Set ID - PV1", data_type="SI", max_length=4, is_required=False, description="Sequence number"),
                HL7FieldDefinition(field_index=2, field_name="Patient Class", data_type="IS", max_length=1, is_required=True, description="Inpatient (I), Outpatient (O), Emergency (E)"),
                HL7FieldDefinition(field_index=3, field_name="Assigned Patient Location", data_type="PL", max_length=80, is_required=False, description="Point of care / Ward / Room / Bed"),
                HL7FieldDefinition(field_index=4, field_name="Admission Type", data_type="IS", max_length=2, is_required=False, description="Routine, Urgent, Elective, Emergency"),
                HL7FieldDefinition(field_index=7, field_name="Attending Doctor", data_type="XCN", max_length=250, is_required=False, description="Primary physician identifier"),
                HL7FieldDefinition(field_index=8, field_name="Referring Doctor", data_type="XCN", max_length=250, is_required=False, description="Referring clinician identifier"),
                HL7FieldDefinition(field_index=9, field_name="Consulting Doctor", data_type="XCN", max_length=250, is_required=False, description="Specialist consultant identifier"),
                HL7FieldDefinition(field_index=10, field_name="Hospital Service", data_type="IS", max_length=3, is_required=False, description="Clinical service / specialty department"),
                HL7FieldDefinition(field_index=14, field_name="Admit Source", data_type="IS", max_length=6, is_required=False, description="Admission source channel"),
                HL7FieldDefinition(field_index=18, field_name="Patient Type", data_type="IS", max_length=2, is_required=False, description="Clinical patient category"),
                HL7FieldDefinition(field_index=19, field_name="Visit Number", data_type="CX", max_length=250, is_required=False, description="Encounter registration identifier"),
                HL7FieldDefinition(field_index=44, field_name="Admit Date/Time", data_type="TS", max_length=26, is_required=False, description="Admission timestamp"),
                HL7FieldDefinition(field_index=45, field_name="Discharge Date/Time", data_type="TS", max_length=26, is_required=False, description="Discharge timestamp")
            ],
        )
        cls._SEGMENTS["OBR"] = HL7SegmentMetadata(
            segment_id="OBR",
            segment_name="Observation Request",
            chapter="Order Entry",
            fields=[
                HL7FieldDefinition(field_index=1, field_name="Set ID - OBR", data_type="SI", max_length=4, is_required=False, description="Sequence number"),
                HL7FieldDefinition(field_index=2, field_name="Placer Order Number", data_type="EI", max_length=22, is_required=False, description="Order number assigned by clinician"),
                HL7FieldDefinition(field_index=3, field_name="Filler Order Number", data_type="EI", max_length=22, is_required=False, description="Order number assigned by lab/radiology"),
                HL7FieldDefinition(field_index=4, field_name="Universal Service Identifier", data_type="CE", max_length=250, is_required=True, description="LOINC or CPT test definition"),
                HL7FieldDefinition(field_index=7, field_name="Observation Date/Time", data_type="TS", max_length=26, is_required=False, description="Clinically relevant specimen collection time"),
                HL7FieldDefinition(field_index=16, field_name="Ordering Provider", data_type="XCN", max_length=250, is_required=False, description="Physician placing order"),
                HL7FieldDefinition(field_index=25, field_name="Result Status", data_type="ID", max_length=1, is_required=False, description="Preliminary (P), Final (F), Corrected (C)")
            ],
        )
        cls._SEGMENTS["OBX"] = HL7SegmentMetadata(
            segment_id="OBX",
            segment_name="Observation / Result",
            chapter="Order Entry",
            fields=[
                HL7FieldDefinition(field_index=1, field_name="Set ID - OBX", data_type="SI", max_length=4, is_required=False, description="Sequence index"),
                HL7FieldDefinition(field_index=2, field_name="Value Type", data_type="ID", max_length=3, is_required=False, description="Numeric (NM), String (ST), Coded (CE)"),
                HL7FieldDefinition(field_index=3, field_name="Observation Identifier", data_type="CE", max_length=250, is_required=True, description="LOINC observation assay parameter"),
                HL7FieldDefinition(field_index=5, field_name="Observation Value", data_type="varies", max_length=65536, is_required=False, description="Clinical measured numerical or text result"),
                HL7FieldDefinition(field_index=6, field_name="Units", data_type="CE", max_length=250, is_required=False, description="Unit of measure (e.g. mg/dL, mmol/L)"),
                HL7FieldDefinition(field_index=7, field_name="References Range", data_type="ST", max_length=60, is_required=False, description="Biological reference interval"),
                HL7FieldDefinition(field_index=8, field_name="Abnormal Flags", data_type="IS", max_length=5, is_required=False, description="Normal (N), High (H), Low (L), Critical (HH/LL)"),
                HL7FieldDefinition(field_index=11, field_name="Observation Result Status", data_type="ID", max_length=1, is_required=True, description="Final result validation status")
            ],
        )

    @classmethod
    def get_segment(cls, segment_id: str) -> Optional[HL7SegmentMetadata]:
        cls.initialize()
        return cls._SEGMENTS.get(segment_id.strip().upper())

    @classmethod
    def count(cls) -> int:
        cls.initialize()
        return len(cls._SEGMENTS)
