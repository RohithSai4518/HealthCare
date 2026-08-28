"""
MLLP (Minimal Lower Layer Protocol) Framing Transport Handlers
Wraps HL7 text payloads in standard start-block (0x0B) and end-block (0x1C, 0x0D) bytes.
"""


class MLLPFraming:
    """Encapsulates and decapsulates HL7 frames over TCP sockets."""

    START_BLOCK = b"\x0b"
    END_BLOCK = b"\x1c\x0d"

    @classmethod
    def frame_message(cls, hl7_string: str) -> bytes:
        return cls.START_BLOCK + hl7_string.encode("utf-8") + cls.END_BLOCK

    @classmethod
    def unframe_message(cls, raw_bytes: bytes) -> str:
        if raw_bytes.startswith(cls.START_BLOCK) and raw_bytes.endswith(cls.END_BLOCK):
            payload = raw_bytes[1:-2]
            return payload.decode("utf-8")
        raise ValueError("Invalid MLLP byte frame boundaries.")
