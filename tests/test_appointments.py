"""
Unit Tests for HealthSphere Appointment & Scheduling Subsystem
"""

import unittest
from core.enums import AppointmentStatus, AppointmentType, Gender
from core.exceptions import ConflictError
from domain.models import Address
from repositories.memory_repo import AppointmentRepository, DoctorRepository, PatientRepository
from services.appointment_service import AppointmentService
from services.patient_service import PatientService


class TestAppointmentService(unittest.TestCase):

    def setUp(self):
        self.patient_repo = PatientRepository()
        self.doctor_repo = DoctorRepository()
        self.appointment_repo = AppointmentRepository()

        self.patient_service = PatientService(self.patient_repo)
        self.appointment_service = AppointmentService(
            self.appointment_repo, self.doctor_repo, self.patient_repo
        )

        self.patient = self.patient_service.register_patient(
            first_name="Emily", last_name="Clark", date_of_birth="1992-07-11", gender=Gender.FEMALE
        )
        self.doctor = self.appointment_service.register_doctor(
            license_number="LIC-MD-99881",
            first_name="Gregory",
            last_name="House",
            specialty="Diagnostic Medicine",
            consultation_fee=250.0,
        )

    def test_slot_generation_and_booking(self):
        slots = self.appointment_service.generate_daily_slots(
            doctor_id=self.doctor.id,
            date_str="2026-09-01",
            start_hour=9,
            end_hour=11,
            slot_duration_minutes=30,
        )
        self.assertEqual(len(slots), 4)

        chosen_slot = slots[0]
        appointment = self.appointment_service.book_appointment(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            slot_id=chosen_slot.slot_id,
            reason_for_visit="Persistent migraine",
        )
        self.assertEqual(appointment.status, AppointmentStatus.SCHEDULED)
        self.assertEqual(appointment.patient_id, self.patient.id)

        # Slot should now be booked
        updated_doc = self.doctor_repo.get_by_id(self.doctor.id)
        slot = updated_doc.find_slot(chosen_slot.slot_id)
        self.assertTrue(slot.is_booked)

    def test_double_booking_prevention(self):
        slots = self.appointment_service.generate_daily_slots(
            doctor_id=self.doctor.id,
            date_str="2026-09-02",
            start_hour=10,
            end_hour=11,
            slot_duration_minutes=30,
        )
        slot_id = slots[0].slot_id

        # First booking succeeds
        self.appointment_service.book_appointment(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            slot_id=slot_id,
            reason_for_visit="First booking",
        )

        # Second booking on same slot must raise ConflictError
        with self.assertRaises(ConflictError):
            self.appointment_service.book_appointment(
                patient_id=self.patient.id,
                doctor_id=self.doctor.id,
                slot_id=slot_id,
                reason_for_visit="Second booking attempt",
            )

    def test_cancellation_frees_slot(self):
        slots = self.appointment_service.generate_daily_slots(
            doctor_id=self.doctor.id,
            date_str="2026-09-03",
            start_hour=14,
            end_hour=15,
            slot_duration_minutes=30,
        )
        slot_id = slots[0].slot_id
        appt = self.appointment_service.book_appointment(
            patient_id=self.patient.id,
            doctor_id=self.doctor.id,
            slot_id=slot_id,
            reason_for_visit="Checkup",
        )

        cancelled = self.appointment_service.cancel_appointment(appt.id, "Patient emergency")
        self.assertEqual(cancelled.status, AppointmentStatus.CANCELLED)

        # Slot should be free again
        doc = self.doctor_repo.get_by_id(self.doctor.id)
        self.assertFalse(doc.find_slot(slot_id).is_booked)


if __name__ == "__main__":
    unittest.main()
