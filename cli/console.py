"""
HealthSphere Interactive Clinical & Hospital Management CLI
Terminal interface for clinical staff, administrators, pharmacists, and lab technicians.
"""

import sys
from typing import Optional
from api.server import HealthSphereAppContext
from core.enums import (
    AbnormalityFlag,
    AppointmentType,
    BloodGroup,
    DrugForm,
    EncounterType,
    Gender,
    MaritalStatus,
    PaymentMethod,
    UserRole,
)
from core.security import UserContext
from domain.clinical import Vitals
from domain.models import Address, ContactInfo, InsurancePolicy
from domain.patient import Allergy, MedicalHistoryRecord
from generators.fhir_exporter import FHIRExporter
from generators.synthetic_data import SyntheticDataGenerator


class HealthSphereCLI:
    """Console interface providing clinical workflow interactions."""

    def __init__(self):
        self.context = HealthSphereAppContext()
        self.generator = SyntheticDataGenerator(
            self.context.patient_service,
            self.context.appointment_service,
            self.context.clinical_service,
            self.context.pharmacy_service,
            self.context.lab_service,
            self.context.billing_service,
        )
        self.current_user = UserContext(
            user_id="ADMIN-001",
            username="admin",
            role=UserRole.ADMIN,
            session_id="CLI-SESSION",
        )

    def print_banner(self):
        print("=" * 70)
        print("   HEALTHSPHERE ENTERPRISE HEALTHCARE INFORMATION PLATFORM   ")
        print("   HIPAA-Compliant EHR, Clinical Encounters & LIS Management ")
        print("=" * 70)

    def print_menu(self):
        print("\n[MAIN OPERATIONAL MENU]")
        print("  1. System Dashboard & Real-Time Metrics")
        print("  2. Patient Registration & Search")
        print("  3. View Patient Complete Medical Chart (EHR)")
        print("  4. Doctor Scheduling & Appointment Booking")
        print("  5. Clinical Encounter & SOAP Note Charting")
        print("  6. Pharmacy Formulary & Prescription Dispensing")
        print("  7. Laboratory Information System (LIS) & Assay Results")
        print("  8. Billing, Invoicing & Insurance Claims")
        print("  9. HIPAA Immutable Audit Log & Integrity Check")
        print(" 10. Generate Safe Synthetic Patient Data (Zero PII/PHI)")
        print(" 11. Export Patient Record to HL7 FHIR R4 JSON")
        print("  0. Exit")

    def run(self):
        self.print_banner()
        while True:
            self.print_menu()
            choice = input("\nSelect Option [0-11]: ").strip()
            if choice == "0":
                print("\nExiting HealthSphere. System state preserved.")
                break
            elif choice == "1":
                self.show_dashboard()
            elif choice == "2":
                self.patient_operations()
            elif choice == "3":
                self.view_patient_chart()
            elif choice == "4":
                self.appointment_operations()
            elif choice == "5":
                self.clinical_encounter_workflow()
            elif choice == "6":
                self.pharmacy_operations()
            elif choice == "7":
                self.lab_operations()
            elif choice == "8":
                self.billing_operations()
            elif choice == "9":
                self.audit_log_operations()
            elif choice == "10":
                self.generate_synthetic_data()
            elif choice == "11":
                self.export_fhir()
            else:
                print("[!] Invalid option. Please enter a number between 0 and 11.")

    def show_dashboard(self):
        print("\n--- HEALTHSPHERE SYSTEM METRICS ---")
        p_count = self.context.patient_repo.count()
        d_count = self.context.doctor_repo.count()
        a_count = self.context.appointment_repo.count()
        e_count = self.context.encounter_repo.count()
        m_count = self.context.medication_repo.count()
        pr_count = self.context.prescription_repo.count()
        l_count = self.context.lab_order_repo.count()
        inv_count = self.context.invoice_repo.count()
        cl_count = self.context.claim_repo.count()

        print(f" Registered Patients     : {p_count}")
        print(f" Active Clinicians       : {d_count}")
        print(f" Appointments Booked     : {a_count}")
        print(f" Clinical Encounters     : {e_count}")
        print(f" Formulary Medications   : {m_count}")
        print(f" Prescriptions Issued    : {pr_count}")
        print(f" Lab Diagnostic Orders   : {l_count}")
        print(f" Invoices Generated      : {inv_count}")
        print(f" Insurance Claims Filed  : {cl_count}")

    def patient_operations(self):
        print("\n--- PATIENT MANAGEMENT ---")
        print("1. Search Patients")
        print("2. Register New Patient")
        sub_choice = input("Select: ").strip()

        if sub_choice == "1":
            q = input("Enter search query (Name or MRN): ").strip()
            results = self.context.patient_service.search_patients(q, self.current_user)
            print(f"\nFound {len(results)} patient(s):")
            for p in results:
                print(f" - [{p.mrn}] {p.full_name} | DOB: {p.date_of_birth} | Gender: {p.gender.value} | ID: {p.id}")

        elif sub_choice == "2":
            first = input("First Name: ").strip()
            last = input("Last Name: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            gender_input = input("Gender (MALE/FEMALE/OTHER): ").strip().upper()
            gender = Gender[gender_input] if gender_input in Gender.__members__ else Gender.UNKNOWN

            street = input("Street Address: ").strip()
            city = input("City: ").strip()
            state = input("State: ").strip()
            zip_code = input("Zip Code: ").strip()
            phone = input("Primary Phone: ").strip()

            address = Address(street=street, city=city, state_or_province=state, postal_code=zip_code)
            contact = ContactInfo(phone_primary=phone)

            patient = self.context.patient_service.register_patient(
                first_name=first,
                last_name=last,
                date_of_birth=dob,
                gender=gender,
                address=address,
                contact=contact,
                context=self.current_user,
            )
            print(f"\n[+] Successfully registered patient: {patient.full_name} (MRN: {patient.mrn})")

    def view_patient_chart(self):
        mrn_or_id = input("\nEnter Patient MRN or ID: ").strip()
        patient = self.context.patient_repo.get_by_mrn(mrn_or_id)
        if not patient:
            patient = self.context.patient_repo.get_by_id(mrn_or_id)

        if not patient:
            print("[!] Patient not found.")
            return

        print("\n" + "=" * 60)
        print(f"PATIENT MEDICAL RECORD: {patient.full_name.upper()} ({patient.mrn})")
        print("=" * 60)
        print(f"DOB: {patient.date_of_birth} | Gender: {patient.gender.value} | Blood: {patient.blood_group.value}")
        if patient.address:
            print(f"Address: {patient.address.formatted()}")
        if patient.contact:
            print(f"Phone: {patient.contact.phone_primary} | Email: {patient.contact.email}")

        print("\n[ALLERGIES]")
        if patient.allergies:
            for a in patient.allergies:
                print(f" * {a.allergen} ({a.category.value}) - Severity: {a.severity.value} | Symptoms: {a.reaction_symptoms}")
        else:
            print(" * No known allergies (NKDA)")

        print("\n[CLINICAL ENCOUNTERS]")
        encounters = self.context.encounter_repo.get_by_patient(patient.id)
        for enc in encounters:
            print(f"\n  [Encounter: {enc.id[:8]}] Date: {enc.start_time} | Status: {enc.status.value}")
            print(f"  Chief Complaint: {enc.chief_complaint}")
            if enc.vitals:
                v = enc.vitals
                print(f"  Vitals: BP {v.systolic_bp}/{v.diastolic_bp} ({v.bp_category}) | HR {v.heart_rate_bpm} bpm | SpO2 {v.spo2_percentage}% | Temp {v.temperature_celsius}°C | BMI {v.bmi}")
            if enc.diagnoses:
                print("  Diagnoses:")
                for d in enc.diagnoses:
                    print(f"   - [{d.icd10_code}] {d.description} (Primary: {d.is_primary})")
            if enc.clinical_note:
                print(f"  SOAP Note by {enc.clinical_note.author_doctor_name}:")
                print(f"   S: {enc.clinical_note.subjective}")
                print(f"   O: {enc.clinical_note.objective}")
                print(f"   A: {enc.clinical_note.assessment}")
                print(f"   P: {enc.clinical_note.plan}")

        print("\n[PRESCRIPTIONS]")
        prescriptions = self.context.prescription_repo.get_by_patient(patient.id)
        for rx in prescriptions:
            print(f"  Rx #{rx.id[:8]} | Status: {rx.status.value} | Issued: {rx.issued_date}")
            for item in rx.items:
                print(f"   - {item.medication_name}: {item.dosage_instruction} (Qty: {item.total_quantity})")

        print("\n[LABORATORY ORDERS & RESULTS]")
        lab_orders = self.context.lab_order_repo.get_by_patient(patient.id)
        for lo in lab_orders:
            print(f"  Lab Order #{lo.id[:8]} | Status: {lo.status.value} | Barcode: {lo.specimen_barcode}")
            for res in lo.results:
                flag_str = f" [{res.flag.value}]" if res.flag != AbnormalityFlag.NORMAL else ""
                print(f"   - {res.parameter_name}: {res.measured_value} {res.unit_of_measure} (Ref: {res.reference_range_display}){flag_str}")

        print("\n[FINANCIAL INVOICES]")
        invoices = self.context.invoice_repo.get_by_patient(patient.id)
        for inv in invoices:
            print(f"  Invoice #{inv.invoice_number} | Status: {inv.status.value} | Net: ${inv.net_total:.2f} | Patient Bal: ${inv.balance_due:.2f}")

    def appointment_operations(self):
        print("\n--- DOCTOR APPOINTMENT BOOKING ---")
        doctors = self.context.doctor_repo.get_all()
        if not doctors:
            print("[!] No doctors registered. Please generate synthetic data or add a doctor.")
            return

        print("\nAvailable Doctors:")
        for idx, d in enumerate(doctors, 1):
            print(f" {idx}. {d.full_name} ({d.specialty}) - Fee: ${d.consultation_fee}")

        doc_idx = int(input("Select Doctor [1-N]: ").strip()) - 1
        doctor = doctors[doc_idx]

        date_str = input("Enter appointment date (YYYY-MM-DD): ").strip()
        slots = self.context.appointment_service.generate_daily_slots(
            doctor_id=doctor.id,
            date_str=date_str,
            context=self.current_user,
        )

        open_slots = [s for s in slots if not s.is_booked]
        if not open_slots:
            print("[!] No open slots available for this doctor on selected date.")
            return

        print("\nOpen Slots:")
        for idx, s in enumerate(open_slots, 1):
            print(f" {idx}. {s.start_time} - {s.end_time} (Slot ID: {s.slot_id})")

        slot_idx = int(input("Select Slot [1-N]: ").strip()) - 1
        chosen_slot = open_slots[slot_idx]

        patient_mrn = input("Enter Patient MRN: ").strip()
        patient = self.context.patient_service.get_patient_by_mrn(patient_mrn, self.current_user)
        reason = input("Reason for consultation: ").strip()

        appt = self.context.appointment_service.book_appointment(
            patient_id=patient.id,
            doctor_id=doctor.id,
            slot_id=chosen_slot.slot_id,
            reason_for_visit=reason,
            context=self.current_user,
        )
        print(f"\n[+] Appointment successfully confirmed! (Appt ID: {appt.id})")

    def clinical_encounter_workflow(self):
        print("\n--- CLINICAL CARE ENCOUNTER WORKFLOW ---")
        patient_mrn = input("Enter Patient MRN: ").strip()
        patient = self.context.patient_service.get_patient_by_mrn(patient_mrn, self.current_user)

        doctors = self.context.doctor_repo.get_all()
        if not doctors:
            print("[!] No clinicians registered.")
            return
        doctor = doctors[0]

        complaint = input("Enter Chief Complaint: ").strip()
        encounter = self.context.clinical_service.start_encounter(
            patient_id=patient.id,
            attending_doctor_id=doctor.id,
            chief_complaint=complaint,
            context=self.current_user,
        )
        print(f"[+] Encounter started (ID: {encounter.id})")

        print("\n[Step 1: Record Physiological Vitals]")
        sbp = int(input("Systolic BP (mmHg): ").strip())
        dbp = int(input("Diastolic BP (mmHg): ").strip())
        hr = int(input("Heart Rate (bpm): ").strip())
        rr = int(input("Respiratory Rate: ").strip())
        temp = float(input("Body Temp (°C): ").strip())
        spo2 = float(input("SpO2 (%): ").strip())
        h_cm = float(input("Height (cm): ").strip())
        w_kg = float(input("Weight (kg): ").strip())

        vitals = self.context.clinical_service.record_vitals(
            encounter_id=encounter.id,
            systolic_bp=sbp,
            diastolic_bp=dbp,
            heart_rate_bpm=hr,
            respiratory_rate=rr,
            temperature_celsius=temp,
            spo2_percentage=spo2,
            height_cm=h_cm,
            weight_kg=w_kg,
            recorded_by_staff_id=doctor.id,
            context=self.current_user,
        )
        print(f"[+] Vitals recorded: BMI {vitals.bmi} | BP Category: {vitals.bp_category}")

        print("\n[Step 2: Diagnosis & SOAP Notes]")
        icd_code = input("ICD-10 Diagnosis Code (e.g. I10, E11.9): ").strip()
        icd_desc = input("Diagnosis Description: ").strip()
        self.context.clinical_service.add_diagnosis(encounter.id, icd_code, icd_desc, True)

        subj = input("Subjective: ").strip()
        obj = input("Objective: ").strip()
        assess = input("Assessment: ").strip()
        plan = input("Plan: ").strip()
        self.context.clinical_service.document_soap_note(
            encounter.id, subj, obj, assess, plan, doctor.id, self.current_user
        )

        disc = input("Discharge Summary: ").strip()
        self.context.clinical_service.complete_encounter(encounter.id, disc, self.current_user)
        print(f"\n[+] Clinical Encounter {encounter.id[:8]} finalized and discharged.")

    def pharmacy_operations(self):
        print("\n--- PHARMACY & DISPENSARY ---")
        print("1. View Active Prescriptions & Dispense")
        print("2. View Formulary Stock Inventory")
        opt = input("Select [1-2]: ").strip()

        if opt == "1":
            active_rx = self.context.prescription_repo.find(lambda r: r.status.value == "ACTIVE")
            if not active_rx:
                print("[!] No active pending prescriptions found.")
                return
            for idx, rx in enumerate(active_rx, 1):
                p = self.context.patient_repo.get_by_id(rx.patient_id)
                p_name = p.full_name if p else rx.patient_id
                print(f" {idx}. Rx #{rx.id[:8]} | Patient: {p_name} | Items: {len(rx.items)}")

            rx_idx = int(input("Select Prescription to Dispense [1-N]: ").strip()) - 1
            chosen_rx = active_rx[rx_idx]
            try:
                self.context.pharmacy_service.dispense_prescription(
                    chosen_rx.id,
                    pharmacist_id="PHARM-001",
                    context=self.current_user,
                )
                print(f"[+] Prescription #{chosen_rx.id[:8]} successfully dispensed! Stock decremented.")
            except Exception as e:
                print(f"[!] Dispensation failed: {str(e)}")

        elif opt == "2":
            meds = self.context.medication_repo.get_all()
            print("\nPharmacy Formulary Inventory:")
            for m in meds:
                total_stock = self.context.inventory_repo.get_total_stock(m.id)
                print(f" - [{m.ndc_code}] {m.display_name} | Unit Price: ${m.unit_price:.2f} | Stock: {total_stock} units")

    def lab_operations(self):
        print("\n--- LABORATORY INFORMATION SYSTEM (LIS) ---")
        orders = self.context.lab_order_repo.get_all()
        if not orders:
            print("[!] No laboratory orders found.")
            return

        for idx, o in enumerate(orders, 1):
            p = self.context.patient_repo.get_by_id(o.patient_id)
            p_name = p.full_name if p else o.patient_id
            print(f" {idx}. Order #{o.id[:8]} | Patient: {p_name} | Status: {o.status.value} | Barcode: {o.specimen_barcode or 'Pending'}")

        order_idx = int(input("Select Order [1-N]: ").strip()) - 1
        chosen_order = orders[order_idx]

        if chosen_order.status.value == "ORDERED":
            barcode = input("Enter or auto-generate specimen barcode (leave blank for auto): ").strip()
            self.context.lab_service.collect_specimen(
                chosen_order.id, technician_id="TECH-001", barcode=barcode or None, context=self.current_user
            )
            print(f"[+] Specimen collected. Status updated to SAMPLE_COLLECTED.")

        elif chosen_order.status.value in ("SAMPLE_COLLECTED", "PROCESSING"):
            measurements = []
            for tid in chosen_order.test_type_ids:
                tt = self.context.lab_test_repo.get_by_id(tid)
                val = float(input(f"Enter measured value for {tt.name} ({tt.reference_range.unit_of_measure if tt.reference_range else ''}): ").strip())
                measurements.append({"test_type_id": tid, "value": val})

            self.context.lab_service.submit_results(
                chosen_order.id, measurements, technician_notes="Assay validated.", context=self.current_user
            )
            print(f"[+] Diagnostic results processed and verified!")

    def billing_operations(self):
        print("\n--- BILLING & INSURANCE CLAIMS ---")
        invoices = self.context.invoice_repo.get_all()
        for idx, inv in enumerate(invoices, 1):
            p = self.context.patient_repo.get_by_id(inv.patient_id)
            p_name = p.full_name if p else inv.patient_id
            print(f" {idx}. Invoice #{inv.invoice_number} | Patient: {p_name} | Net: ${inv.net_total:.2f} | Status: {inv.status.value}")

    def audit_log_operations(self):
        from core.audit import audit_service
        print("\n--- HIPAA IMMUTABLE AUDIT TRAIL ---")
        logs = audit_service.get_logs(limit=20)
        for l in logs:
            print(f" [{l.timestamp[:19]}] Actor: {l.actor_id} ({l.actor_role}) -> Action: {l.action} on {l.resource_type}:{l.resource_id[:8]} | Hash: {l.entry_hash[:12]}...")

        is_valid = audit_service.verify_integrity()
        print(f"\nAudit Log Hash Chain Cryptographic Integrity: {'[VALID - UNTAMPERED]' if is_valid else '[INVALID - TAMPERED]'}")

    def generate_synthetic_data(self):
        print("\n--- SAFE SYNTHETIC DATA GENERATOR ---")
        count = int(input("Enter number of synthetic patient records to generate [e.g. 5, 10, 25]: ").strip() or "5")
        print(f"[*] Generating {count} complete synthetic patient profiles with clinical histories...")
        patients = self.generator.seed_synthetic_patients_and_scenarios(patient_count=count)
        print(f"[+] Successfully generated and seeded {len(patients)} synthetic patient charts.")

    def export_fhir(self):
        print("\n--- HL7 FHIR R4 EXPORT ---")
        patient_mrn = input("Enter Patient MRN: ").strip()
        patient = self.context.patient_service.get_patient_by_mrn(patient_mrn, self.current_user)
        encounters = self.context.encounter_repo.get_by_patient(patient.id)
        labs = self.context.lab_order_repo.get_by_patient(patient.id)

        bundle_json = FHIRExporter.export_patient_bundle(patient, encounters, labs)
        print("\n[HL7 FHIR R4 Bundle JSON Preview]:")
        print(bundle_json[:1200] + "\n... [truncated for display]")
