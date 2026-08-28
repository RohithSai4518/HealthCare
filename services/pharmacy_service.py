"""
HealthSphere Pharmacy & Medication Safety Service
Formulary management, drug-drug interaction matrix, allergy contraindication checks, and dispensing workflows.
"""

from typing import List, Optional, Tuple
from core.audit import audit_service
from core.enums import AuditAction, DrugForm, InteractionSeverity, PrescriptionStatus
from core.exceptions import (
    ConflictError,
    DrugInteractionError,
    EntityNotFoundError,
    InsufficientStockError,
    ValidationError,
)
from core.security import RBACManager, UserContext
from domain.pharmacy import (
    DrugInteraction,
    Medication,
    PharmacyInventoryItem,
    Prescription,
    PrescriptionItem,
)
from repositories.memory_repo import (
    DoctorRepository,
    InventoryRepository,
    MedicationRepository,
    PatientRepository,
    PrescriptionRepository,
)


class PharmacyService:
    """Manages medications, prescription lifecycle, patient drug safety checks, and inventory."""

    def __init__(
        self,
        medication_repo: MedicationRepository,
        prescription_repo: PrescriptionRepository,
        inventory_repo: InventoryRepository,
        patient_repo: PatientRepository,
        doctor_repo: DoctorRepository,
    ):
        self.medication_repo = medication_repo
        self.prescription_repo = prescription_repo
        self.inventory_repo = inventory_repo
        self.patient_repo = patient_repo
        self.doctor_repo = doctor_repo
        self._interactions: List[DrugInteraction] = []
        self._initialize_interaction_rules()

    def _initialize_interaction_rules(self) -> None:
        """Seed known critical and major clinical drug-drug interaction pairs."""
        self._interactions.extend([
            DrugInteraction(
                drug_name_a="Warfarin",
                drug_name_b="Aspirin",
                severity=InteractionSeverity.MAJOR,
                clinical_effect="Significantly increased risk of severe gastrointestinal and systemic bleeding.",
                management_recommendation="Avoid combination or closely monitor INR levels.",
            ),
            DrugInteraction(
                drug_name_a="Simvastatin",
                drug_name_b="Amiodarone",
                severity=InteractionSeverity.MAJOR,
                clinical_effect="Increased risk of severe myopathy and rhabdomyolysis.",
                management_recommendation="Limit simvastatin dose or switch to alternative statin (e.g. rosuvastatin).",
            ),
            DrugInteraction(
                drug_name_a="Ciprofloxacin",
                drug_name_b="Theophylline",
                severity=InteractionSeverity.MAJOR,
                clinical_effect="Ciprofloxacin elevates theophylline serum levels risking toxicity.",
                management_recommendation="Dose reduction of theophylline and monitor therapeutic levels.",
            ),
            DrugInteraction(
                drug_name_a="Lisinopril",
                drug_name_b="Spironolactone",
                severity=InteractionSeverity.MAJOR,
                clinical_effect="Synergistic potassium retention leading to severe hyperkalemia.",
                management_recommendation="Regular serum potassium and renal function monitoring.",
            ),
            DrugInteraction(
                drug_name_a="Methotrexate",
                drug_name_b="Ibuprofen",
                severity=InteractionSeverity.CONTRAINDICATED,
                clinical_effect="NSAIDs decrease methotrexate clearance causing severe bone marrow suppression.",
                management_recommendation="Contraindicated with high-dose methotrexate; avoid combination.",
            ),
        ])

    def register_medication(
        self,
        ndc_code: str,
        generic_name: str,
        brand_name: str,
        form: DrugForm = DrugForm.TABLET,
        strength: str = "500mg",
        unit_price: float = 15.0,
        active_ingredients: Optional[List[str]] = None,
        context: Optional[UserContext] = None,
    ) -> Medication:
        if context:
            RBACManager.check_permission(context, "pharmacy:write")

        med = Medication(
            ndc_code=ndc_code.strip(),
            generic_name=generic_name.strip(),
            brand_name=brand_name.strip(),
            form=form,
            strength=strength.strip(),
            unit_price=unit_price,
            active_ingredients=active_ingredients or [generic_name.strip()],
        )
        return self.medication_repo.save(med)

    def restock_inventory(
        self,
        medication_id: str,
        batch_number: str,
        quantity: int,
        unit_cost: float = 5.0,
        expiry_date: str = "2027-12-31",
        context: Optional[UserContext] = None,
    ) -> PharmacyInventoryItem:
        if context:
            RBACManager.check_permission(context, "pharmacy:write")

        self.medication_repo.get_by_id_or_raise(medication_id)
        item = PharmacyInventoryItem(
            medication_id=medication_id,
            batch_number=batch_number,
            quantity_on_hand=quantity,
            unit_cost=unit_cost,
            expiry_date=expiry_date,
        )
        return self.inventory_repo.save(item)

    def check_safety(
        self,
        patient_id: str,
        candidate_medications: List[str],  # list of generic or brand names
    ) -> List[dict]:
        """
        Evaluates potential drug-drug interactions and allergy contraindications.
        """
        warnings = []
        patient = self.patient_repo.get_by_id_or_raise(patient_id)

        # 1. Check patient allergies
        for med_name in candidate_medications:
            for allergy in patient.allergies:
                if allergy.is_active and (
                    allergy.allergen.lower() in med_name.lower() or med_name.lower() in allergy.allergen.lower()
                ):
                    warnings.append({
                        "type": "ALLERGY_ALERT",
                        "severity": allergy.severity.value,
                        "medication": med_name,
                        "allergen": allergy.allergen,
                        "reaction": allergy.reaction_symptoms,
                    })

        # 2. Check candidate drug interactions among themselves
        for i in range(len(candidate_medications)):
            for j in range(i + 1, len(candidate_medications)):
                d1 = candidate_medications[i]
                d2 = candidate_medications[j]
                for rule in self._interactions:
                    if rule.matches(d1, d2):
                        warnings.append({
                            "type": "DRUG_INTERACTION",
                            "severity": rule.severity.value,
                            "drugs": [d1, d2],
                            "effect": rule.clinical_effect,
                            "recommendation": rule.management_recommendation,
                        })

        return warnings

    def create_prescription(
        self,
        patient_id: str,
        doctor_id: str,
        items_data: List[dict],
        encounter_id: Optional[str] = None,
        clinical_rationale: Optional[str] = None,
        force_override_warnings: bool = False,
        context: Optional[UserContext] = None,
    ) -> Prescription:
        """Issues a new clinical prescription after safety checks."""
        if context:
            RBACManager.check_permission(context, "pharmacy:prescribe")

        self.patient_repo.get_by_id_or_raise(patient_id)
        self.doctor_repo.get_by_id_or_raise(doctor_id)

        candidate_names = []
        prescription_items: List[PrescriptionItem] = []

        for data in items_data:
            med_id = data["medication_id"]
            med = self.medication_repo.get_by_id_or_raise(med_id)
            candidate_names.append(med.generic_name)

            freq = data.get("frequency_per_day", 1)
            duration = data.get("duration_days", 7)
            total_qty = data.get("total_quantity", freq * duration)

            p_item = PrescriptionItem(
                medication_id=med_id,
                medication_name=med.display_name,
                dosage_instruction=data.get("dosage_instruction", "Take as directed"),
                frequency_per_day=freq,
                duration_days=duration,
                total_quantity=total_qty,
                refills_authorized=data.get("refills_authorized", 0),
                refills_remaining=data.get("refills_authorized", 0),
            )
            prescription_items.append(p_item)

        # Evaluate safety
        safety_warnings = self.check_safety(patient_id, candidate_names)
        has_contraindication = any(w.get("severity") in ("CONTRAINDICATED", "LIFE_THREATENING") for w in safety_warnings)

        if has_contraindication and not force_override_warnings:
            raise DrugInteractionError(
                "Prescription blocked due to severe contraindication or allergy match.",
                drugs=candidate_names,
                severity="CONTRAINDICATED",
            )

        prescription = Prescription(
            patient_id=patient_id,
            prescribing_doctor_id=doctor_id,
            encounter_id=encounter_id,
            status=PrescriptionStatus.ACTIVE,
            items=prescription_items,
            clinical_rationale=clinical_rationale,
        )

        saved_prescription = self.prescription_repo.save(prescription)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="Prescription",
            resource_id=saved_prescription.id,
            details={"patient_id": patient_id, "item_count": str(len(prescription_items))},
        )

        return saved_prescription

    def dispense_prescription(
        self,
        prescription_id: str,
        pharmacist_id: str,
        context: Optional[UserContext] = None,
    ) -> Prescription:
        """Dispense prescription items and deduct stock from pharmacy inventory batches."""
        if context:
            RBACManager.check_permission(context, "pharmacy:dispense")

        prescription = self.prescription_repo.get_by_id_or_raise(prescription_id)
        if prescription.status == PrescriptionStatus.DISPENSED:
            raise ConflictError("Prescription has already been dispensed.")

        # Check stock availability for all items first
        for item in prescription.items:
            available_stock = self.inventory_repo.get_total_stock(item.medication_id)
            if available_stock < item.total_quantity:
                raise InsufficientStockError(item.medication_id, item.total_quantity, available_stock)

        # Deduct stock across batches
        for item in prescription.items:
            needed = item.total_quantity
            batches = self.inventory_repo.get_by_medication(item.medication_id)
            for batch in batches:
                if needed <= 0:
                    break
                deduct_qty = min(batch.quantity_on_hand, needed)
                batch.deduct(deduct_qty)
                self.inventory_repo.save(batch)
                needed -= deduct_qty

        prescription.mark_dispensed(pharmacist_id)
        self.prescription_repo.save(prescription)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.DISPENSE,
            resource_type="Prescription",
            resource_id=prescription_id,
            details={"dispensed_by": pharmacist_id},
        )

        return prescription
