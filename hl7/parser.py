"""
HL7 v2 Message Parser and Object Tree Serializer
Implements delimiter-based segment, field, repetition, component, and subcomponent tokenization.
"""

from typing import List, Optional, Dict, Any


class HL7Segment:
    """Represents a single pipe-delimited HL7 segment."""

    def __init__(self, raw_segment: str, field_sep: str = "|", comp_sep: str = "^"):
        self.raw = raw_segment.strip()
        self.field_sep = field_sep
        self.comp_sep = comp_sep
        self.fields: List[str] = self.raw.split(field_sep) if self.raw else []

    @property
    def name(self) -> str:
        return self.fields[0] if self.fields else ""

    def get_field(self, field_index: int, default: str = "") -> str:
        if self.name == "MSH":
            if field_index == 1:
                return self.field_sep
            array_idx = field_index - 1
        else:
            array_idx = field_index
        if 0 <= array_idx < len(self.fields):
            return self.fields[array_idx]
        return default

    def get_component(self, field_index: int, component_index: int, default: str = "") -> str:
        f_val = self.get_field(field_index)
        if not f_val:
            return default
        comps = f_val.split(self.comp_sep)
        if 0 <= component_index < len(comps):
            return comps[component_index]
        return default

    def to_hl7(self) -> str:
        return self.field_sep.join(self.fields)


class HL7Message:
    """Represents a structured multi-segment HL7 v2 message."""

    def __init__(self, segments: Optional[List[HL7Segment]] = None):
        self.segments: List[HL7Segment] = segments or []

    @property
    def message_type(self) -> str:
        msh = self.get_segment("MSH")
        if msh:
            return msh.get_field(9)  # e.g., ADT^A01^ADT_A01
        return "UNKNOWN"

    @property
    def control_id(self) -> str:
        msh = self.get_segment("MSH")
        return msh.get_field(10) if msh else ""

    def get_segment(self, segment_name: str) -> Optional[HL7Segment]:
        for s in self.segments:
            if s.name == segment_name:
                return s
        return None

    def get_all_segments(self, segment_name: str) -> List[HL7Segment]:
        return [s for s in self.segments if s.name == segment_name]

    def add_segment(self, segment: HL7Segment) -> None:
        self.segments.append(segment)

    def to_hl7(self) -> str:
        return "\r".join(s.to_hl7() for s in self.segments) + "\r"


class HL7Parser:
    """High-performance parser for raw HL7 v2.x text payloads."""

    @staticmethod
    def parse(raw_hl7: str) -> HL7Message:
        normalized = raw_hl7.replace("\r\n", "\r").replace("\n", "\r")
        lines = [line.strip() for line in normalized.split("\r") if line.strip()]

        if not lines:
            raise ValueError("Empty HL7 message payload.")

        msh_line = lines[0]
        if not msh_line.startswith("MSH"):
            raise ValueError("Invalid HL7 message: Header must start with MSH segment.")

        field_sep = msh_line[3]  # Standard: '|'
        encoding_chars = msh_line[4:8]  # Standard: '^~\&'
        comp_sep = encoding_chars[0] if len(encoding_chars) > 0 else "^"

        segments = []
        for line in lines:
            seg = HL7Segment(line, field_sep=field_sep, comp_sep=comp_sep)
            segments.append(seg)

        return HL7Message(segments)
