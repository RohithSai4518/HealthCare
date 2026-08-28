"""
Unit Tests for HL7 v2 Messaging Subsystem
"""

import unittest
from domain.clinical import Encounter
from domain.patient import Patient
from hl7.messages import HL7MessageFactory
from hl7.mllp import MLLPFraming
from hl7.parser import HL7Parser
from hl7.validator import HL7Validator


class TestHL7Engine(unittest.TestCase):

    def test_hl7_adt_creation_and_parsing(self):
        patient = Patient(first_name="Arthur", last_name="Conan", date_of_birth="1960-05-22")
        encounter = Encounter(patient_id=patient.id, attending_doctor_id="DOC-99")

        msg = HL7MessageFactory.create_adt_a01_admit(patient, encounter)
        raw_hl7 = msg.to_hl7()

        self.assertIn("MSH|", raw_hl7)
        self.assertIn("PID|", raw_hl7)
        self.assertIn("PV1|", raw_hl7)

        # Validate
        valid, errs = HL7Validator.validate(msg)
        self.assertTrue(valid, f"Validation errors: {errs}")

        # Parse back
        parsed = HL7Parser.parse(raw_hl7)
        self.assertEqual(parsed.get_segment("PID").get_component(5, 0), "Conan")

    def test_mllp_framing(self):
        sample = "MSH|^~\&|SYS|HOSP|||20260101||ADT^A01|101|P|2.5"
        framed = MLLPFraming.frame_message(sample)
        self.assertTrue(framed.startswith(b"\x0b"))
        self.assertTrue(framed.endswith(b"\x1c\x0d"))
        unframed = MLLPFraming.unframe_message(framed)
        self.assertEqual(unframed, sample)


if __name__ == "__main__":
    unittest.main()
