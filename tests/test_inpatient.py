"""
Unit Tests for Inpatient Bed and Ward Management
"""

import unittest
from inpatient.ward import BedStatus, WardManager


class TestInpatientWard(unittest.TestCase):

    def setUp(self):
        self.mgr = WardManager()

    def test_ward_occupancy_and_allocation(self):
        icu = self.mgr.get_ward("ICU")
        self.assertIsNotNone(icu)
        self.assertEqual(icu.total_capacity, 10)
        self.assertEqual(icu.occupied_count, 0)

        # Assign patient
        assigned = self.mgr.assign_patient_to_bed("ICU", "ICU-B01", "PAT-100", "NURSE-01")
        self.assertTrue(assigned)
        self.assertEqual(icu.occupied_count, 1)
        self.assertEqual(icu.occupancy_rate, 10.0)

        # Discharge bed
        discharged = self.mgr.discharge_bed("ICU", "ICU-B01")
        self.assertTrue(discharged)
        bed = next(b for b in icu.beds if b.bed_id == "ICU-B01")
        self.assertEqual(bed.status, BedStatus.CLEANING)


if __name__ == "__main__":
    unittest.main()
