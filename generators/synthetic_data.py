"""
HealthSphere Safe Synthetic Clinical Data Generator
Procedural generation of realistic, completely fictional healthcare records (Zero PII / Zero PHI).
"""

import random
from typing import Dict, List, Tuple
from core.enums import (
    AllergyCategory,
    AllergySeverity,
    AppointmentType,
    BloodGroup,
    DrugForm,
    EncounterType,
    Gender,
    MaritalStatus,
    PaymentMethod,
)
from domain.clinical import Diagnosis, Vitals
from domain.models import Address, ContactInfo, InsurancePolicy
from domain.patient import Allergy, EmergencyContact, MedicalHistoryRecord, Patient
from domain.pharmacy import Medication
from repositories.memory_repo import (
    AppointmentRepository,
    DoctorRepository,
    EncounterRepository,
    InventoryRepository,
    LabOrderRepository,
    LabTestTypeRepository,
    MedicationRepository,
    PatientRepository,
)
from services.appointment_service import AppointmentService
from services.billing_service import BillingService
from services.clinical_service import ClinicalService
from services.lab_service import LabService
from services.patient_service import PatientService
from services.pharmacy_service import PharmacyService


class SyntheticDataGenerator:
    """Generates comprehensive, clinically coherent synthetic healthcare scenarios."""

    FIRST_NAMES_M = ["James", "Robert", "John", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles", "Daniel", "Matthew"]
    FIRST_NAMES_F = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy", "Lisa"]
    LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez"]
    STREETS = ["Oakridge Ave", "Maple Street", "Pinecrest Blvd", "Highland Road", "Cedar Way", "Elm Court", "Riverwalk Lane"]
    CITIES = ["Metropolis", "Springfield", "Riverdale", "Gotham", "Starling", "Central City", "Emerald Bay"]
    STATES = ["CA", "NY", "TX", "FL", "IL", "WA", "MA"]

    COMMON_DIAGNOSES = [
        ("I10", "Essential (primary) hypertension"),
        ("E11.9", "Type 2 diabetes mellitus without complications"),
        ("J45.909", "Unspecified asthma, uncomplicated"),
        ("M54.5", "Low back pain, unspecified"),
        ("K21.9", "Gastro-esophageal reflux disease without esophagitis"),
        ("J06.9", "Acute upper respiratory infection, unspecified"),
        ("E78.5", "Hyperlipidemia, unspecified"),
        ("F41.1", "Generalized anxiety disorder"),
    ]

    COMMON_DRUGS = [
        ("0071-0155-23", "Atorvastatin", "Lipitor", DrugForm.TABLET, "20mg", 15.0),
        ("0093-0105-01", "Metformin", "Glucophage", DrugForm.TABLET, "500mg", 10.0),
        ("0006-0740-54", "Lisinopril", "Prinivil", DrugForm.TABLET, "10mg", 12.0),
        ("0085-1132-01", "Albuterol", "Ventolin HFA", DrugForm.INHALER, "90mcg", 35.0),
        ("0029-6086-12", "Amoxicillin", "Amoxil", DrugForm.CAPSULE, "500mg", 18.0),
        ("50458-580-60", "Omeprazole", "Prilosec", DrugForm.CAPSULE, "20mg", 14.0),
        ("0054-0007-25", "Aspirin", "Bayer", DrugForm.TABLET, "81mg", 8.0),
        ("0054-0010-25", "Warfarin", "Coumadin", DrugForm.TABLET, "5mg", 22.0),
    ]

    DOCTOR_SPECIALTIES = [
        ("Cardiology", "Cardiovascular Medicine"),
        ("Endocrinology", "Metabolic Diseases"),
        ("Pulmonology", "Respiratory Medicine"),
        ("Pediatrics", "Child Health"),
        ("Orthopedics", "Musculoskeletal Surgery"),
        ("General Medicine", "Internal Medicine"),
        ("Dermatology", "Skin Health"),
    ]

    def __init__(
        self,
        patient_service: PatientService,
        appointment_service: AppointmentService,
        clinical_service: ClinicalService,
        pharmacy_service: PharmacyService,
        lab_service: LabService,
        billing_service: BillingService,
    ):
        self.patient_service = patient_service
        self.appointment_service = appointment_service
        self.clinical_service = clinical_service
        self.pharmacy_service = pharmacy_service
        self.lab_service = lab_service
        self.billing_service = billing_service

    def seed_medications_and_inventory(self) -> List[Medication]:
        meds = []
        for ndc, generic, brand, form, strength, price in self.COMMON_DRUGS:
            existing = self.pharmacy_service.medication_repo.get_by_ndc(ndc)
            if not existing:
                med = self.pharmacy_service.register_medication(
                    ndc_code=ndc,
                    generic_name=generic,
                    brand_name=brand,
                    form=form,
                    strength=strength,
                    unit_price=price,
                )
                self.pharmacy_service.restock_inventory(
                    medication_id=med.id,
                    batch_number=f"BAT-{random.randint(1000, 9999)}",
                    quantity=random.randint(200, 500),
                    unit_cost=round(price * 0.4, 2),
                )
                meds.append(med)
            else:
                meds.append(existing)
        return meds

    def seed_doctors(self, count: int = 5) -> List:
        doctors = []
        for i in range(count):
            spec, dept = random.choice(self.DOCTOR_SPECIALTIES)
            first_name = random.choice(self.FIRST_NAMES_M if i % 2 == 0 else self.FIRST_NAMES_F)
            last_name = random.choice(self.LAST_NAMES)
            lic = f"LIC-MD-{random.randint(10000, 99999)}"

            doc = self.appointment_service.register_doctor(
                license_number=lic,
                first_name=first_name,
                last_name=last_name,
                specialty=spec,
                department=dept,
                consultation_fee=float(random.choice([120, 150, 180, 200])),
            )
            doctors.append(doc)
        return doctors

    def seed_synthetic_patients_and_scenarios(
        self,
        patient_count: int = 10,
        generate_encounters: bool = True,
    ) -> List[Patient]:
        """Creates complete patient charts with encounters, prescriptions, labs, and billing."""
        patients = []
        doctors = self.appointment_service.doctor_repo.get_all()
        if not doctors:
            doctors = self.seed_doctors(5)

        meds = self.pharmacy_service.medication_repo.get_all()
        if not meds:
            meds = self.seed_medications_and_inventory()

        lab_types = self.lab_service.test_type_repo.get_all()

        for idx in range(patient_count):
            is_male = idx % 2 == 0
            gender = Gender.MALE if is_male else Gender.FEMALE
            first_name = random.choice(self.FIRST_NAMES_M if is_male else self.FIRST_NAMES_F)
            last_name = random.choice(self.LAST_NAMES)
            birth_year = random.randint(1950, 2005)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28)
            dob = f"{birth_year}-{birth_month:02d}-{birth_day:02d}"

            address = Address(
                street=f"{random.randint(100, 9999)} {random.choice(self.STREETS)}",
                city=random.choice(self.CITIES),
                state_or_province=random.choice(self.STATES),
                postal_code=f"{random.randint(10000, 99999)}",
            )
            contact = ContactInfo(
                phone_primary=f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
                email=f"dummy_{first_name.lower()}.{last_name.lower()}{random.randint(10,99)}@synthetic-health.org",
            )
            has_insurance = random.random() > 0.3
            insurance = None
            if has_insurance:
                insurance = InsurancePolicy(
                    provider_name=random.choice(["Apex Health Plan", "Blue Cross Synthetic", "CarePlus PPO"]),
                    policy_number=f"POL-{random.randint(100000, 999999)}",
                    group_number=f"GRP-{random.randint(1000, 9999)}",
                    subscriber_id=f"SUB-{random.randint(10000, 99999)}",
                    co_pay_amount=float(random.choice([20, 25, 30, 40])),
                    coverage_percentage=random.choice([0.75, 0.80, 0.85]),
                    deductible=500.0,
                    deductible_met=random.choice([0.0, 250.0, 500.0]),
                )

            patient = self.patient_service.register_patient(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=dob,
                gender=gender,
                blood_group=random.choice(list(BloodGroup)),
                marital_status=random.choice(list(MaritalStatus)),
                address=address,
                contact=contact,
                insurance=insurance,
            )

            # Add emergency contact
            patient.add_emergency_contact(
                EmergencyContact(
                    full_name=f"Contact {last_name}",
                    relationship=random.choice(["Spouse", "Parent", "Sibling", "Partner"]),
                    phone_number=f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
                )
            )

            # Optional allergy
            if random.random() > 0.6:
                patient.add_allergy(
                    Allergy(
                        allergen=random.choice(["Penicillin", "Sulfa drugs", "Peanuts", "Latex"]),
                        category=AllergyCategory.MEDICATION,
                        severity=AllergySeverity.MODERATE,
                        reaction_symptoms="Urticaria and mild skin rash",
                    )
                )

            # Optional medical history
            if random.random() > 0.5:
                patient.add_history(
                    MedicalHistoryRecord(
                        condition_or_procedure="Appendectomy",
                        diagnosed_or_performed_date="2018-05-12",
                    )
                )

            self.patient_service.patient_repo.save(patient)

            if generate_encounters and doctors:
                doctor = random.choice(doctors)
                diag_code, diag_name = random.choice(self.COMMON_DIAGNOSES)

                # 1. Clinical encounter
                encounter = self.clinical_service.start_encounter(
                    patient_id=patient.id,
                    attending_doctor_id=doctor.id,
                    encounter_type=EncounterType.OUTPATIENT,
                    chief_complaint=f"Patient reports symptoms consistent with {diag_name.lower()}.",
                )

                # 2. Vitals
                self.clinical_service.record_vitals(
                    encounter_id=encounter.id,
                    systolic_bp=random.randint(110, 145),
                    diastolic_bp=random.randint(70, 95),
                    heart_rate_bpm=random.randint(65, 88),
                    respiratory_rate=random.randint(14, 18),
                    temperature_celsius=round(random.uniform(36.4, 37.4), 1),
                    spo2_percentage=round(random.uniform(96.0, 99.0), 1),
                    height_cm=round(random.uniform(155.0, 185.0), 1),
                    weight_kg=round(random.uniform(55.0, 95.0), 1),
                    recorded_by_staff_id=doctor.id,
                )

                # 3. Diagnosis & SOAP Note
                self.clinical_service.add_diagnosis(
                    encounter_id=encounter.id,
                    icd10_code=diag_code,
                    description=diag_name,
                    is_primary=True,
                )
                self.clinical_service.document_soap_note(
                    encounter_id=encounter.id,
                    subjective="Patient presents for evaluation of persistent symptoms over past two weeks.",
                    objective="Physical examination reveals stable cardiopulmonary findings.",
                    assessment=f"Confirmed diagnosis of {diag_name}.",
                    plan="Initiate targeted pharmacotherapy and routine laboratory monitoring.",
                    author_doctor_id=doctor.id,
                )

                # 4. Prescription
                chosen_med = random.choice(meds)
                p_items = [{
                    "medication_id": chosen_med.id,
                    "dosage_instruction": "Take 1 unit daily with water",
                    "frequency_per_day": 1,
                    "duration_days": 14,
                    "total_quantity": 14,
                    "refills_authorized": 1,
                }]
                prescription = self.pharmacy_service.create_prescription(
                    patient_id=patient.id,
                    doctor_id=doctor.id,
                    items_data=p_items,
                    encounter_id=encounter.id,
                    clinical_rationale=f"Management for {diag_name}",
                )

                # 5. Lab order
                if lab_types:
                    chosen_lab = random.choice(lab_types)
                    lab_order = self.lab_service.order_lab_tests(
                        patient_id=patient.id,
                        doctor_id=doctor.id,
                        test_type_ids=[chosen_lab.id],
                        clinical_indication=f"Baseline monitoring for {diag_name}",
                        encounter_id=encounter.id,
                    )
                    self.lab_service.collect_specimen(lab_order.id, technician_id="TECH-001")
                    ref = chosen_lab.reference_range
                    val = (ref.low_value + ref.high_value) / 2.0 if ref else 100.0
                    self.lab_service.submit_results(
                        order_id=lab_order.id,
                        measurements=[{"test_type_id": chosen_lab.id, "value": val}],
                    )

                # 6. Complete encounter
                self.clinical_service.complete_encounter(
                    encounter_id=encounter.id,
                    discharge_summary=f"Patient discharged in stable condition with prescription for {chosen_med.brand_name}.",
                )

                # 7. Billing
                invoice_items = [
                    {"item_code": "CPT-99213", "description": "Outpatient Office Visit (Standard)", "quantity": 1, "unit_price": doctor.consultation_fee},
                    {"item_code": chosen_med.ndc_code, "description": chosen_med.display_name, "quantity": 14, "unit_price": chosen_med.unit_price},
                ]
                invoice = self.billing_service.create_invoice(
                    patient_id=patient.id,
                    items_data=invoice_items,
                    encounter_id=encounter.id,
                )

                if invoice.patient_responsibility > 0:
                    self.billing_service.record_payment(
                        invoice_id=invoice.id,
                        amount=invoice.patient_responsibility,
                        method=PaymentMethod.CREDIT_CARD,
                    )

                if invoice.insurance_responsibility > 0 and patient.insurance:
                    claim = self.billing_service.submit_insurance_claim(invoice_id=invoice.id)
                    self.billing_service.adjudicate_claim(
                        claim_id=claim.id,
                        approved_amount=claim.total_claim_amount,
                        is_approved=True,
                        notes="Clean claim adjudication - fully approved.",
                    )

            patients.append(patient)

        return patients
