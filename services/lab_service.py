"""
HealthSphere Laboratory Information System (LIS) Service
Test order placement, specimen barcode handling, and automated clinical reference range evaluation.
"""

import time
from typing import List, Optional
from core.audit import audit_service
from core.enums import AbnormalityFlag, AuditAction, LabOrderStatus, LabTestCategory
from core.exceptions import ConflictError, EntityNotFoundError, ValidationError
from core.security import RBACManager, UserContext
from domain.laboratory import LabOrder, LabResultItem, LabTestType, ReferenceRange
from repositories.memory_repo import (
    DoctorRepository,
    LabOrderRepository,
    LabTestTypeRepository,
    PatientRepository,
)


class LabService:
    """Manages diagnostic laboratory testing, specimen logistics, and result reporting."""

    def __init__(
        self,
        lab_order_repo: LabOrderRepository,
        test_type_repo: LabTestTypeRepository,
        patient_repo: PatientRepository,
        doctor_repo: DoctorRepository,
    ):
        self.lab_order_repo = lab_order_repo
        self.test_type_repo = test_type_repo
        self.patient_repo = patient_repo
        self.doctor_repo = doctor_repo
        self._initialize_standard_test_catalog()

    def _initialize_standard_test_catalog(self) -> None:
        """Seed common clinical diagnostic assays with biological reference intervals."""
        tests = [
            LabTestType(
                code="LOINC-718-7",
                name="Hemoglobin (Hb)",
                category=LabTestCategory.HEMATOLOGY,
                sample_type_required="Whole Blood (EDTA)",
                standard_price=25.0,
                turnaround_time_hours=2,
                reference_range=ReferenceRange(
                    low_value=13.5,
                    high_value=17.5,
                    unit_of_measure="g/dL",
                    critical_low=7.0,
                    critical_high=20.0,
                ),
            ),
            LabTestType(
                code="LOINC-2345-7",
                name="Fasting Blood Glucose",
                category=LabTestCategory.BIOCHEMISTRY,
                sample_type_required="Fluoride Oxalate Plasma",
                standard_price=20.0,
                turnaround_time_hours=2,
                reference_range=ReferenceRange(
                    low_value=70.0,
                    high_value=99.0,
                    unit_of_measure="mg/dL",
                    critical_low=45.0,
                    critical_high=400.0,
                ),
            ),
            LabTestType(
                code="LOINC-2160-0",
                name="Serum Creatinine",
                category=LabTestCategory.BIOCHEMISTRY,
                sample_type_required="Serum (SST)",
                standard_price=30.0,
                turnaround_time_hours=3,
                reference_range=ReferenceRange(
                    low_value=0.7,
                    high_value=1.3,
                    unit_of_measure="mg/dL",
                    critical_high=5.0,
                ),
            ),
            LabTestType(
                code="LOINC-2823-3",
                name="Serum Potassium (K+)",
                category=LabTestCategory.BIOCHEMISTRY,
                sample_type_required="Serum (SST)",
                standard_price=25.0,
                turnaround_time_hours=2,
                reference_range=ReferenceRange(
                    low_value=3.5,
                    high_value=5.0,
                    unit_of_measure="mmol/L",
                    critical_low=2.8,
                    critical_high=6.2,
                ),
            ),
        ]
        for t in tests:
            if not self.test_type_repo.get_by_code(t.code):
                self.test_type_repo.save(t)

    def order_lab_tests(
        self,
        patient_id: str,
        doctor_id: str,
        test_type_ids: List[str],
        clinical_indication: str,
        encounter_id: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> LabOrder:
        """Place a new diagnostic laboratory order."""
        if context:
            RBACManager.check_permission(context, "lab:order")

        self.patient_repo.get_by_id_or_raise(patient_id)
        self.doctor_repo.get_by_id_or_raise(doctor_id)

        if not test_type_ids:
            raise ValidationError("At least one diagnostic test type must be selected.")

        for tid in test_type_ids:
            self.test_type_repo.get_by_id_or_raise(tid)

        order = LabOrder(
            patient_id=patient_id,
            ordering_doctor_id=doctor_id,
            encounter_id=encounter_id,
            test_type_ids=test_type_ids,
            clinical_indication=clinical_indication,
            status=LabOrderStatus.ORDERED,
        )
        saved_order = self.lab_order_repo.save(order)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.CREATE,
            resource_type="LabOrder",
            resource_id=saved_order.id,
            details={"patient_id": patient_id, "test_count": str(len(test_type_ids))},
        )

        return saved_order

    def collect_specimen(
        self,
        order_id: str,
        technician_id: str,
        barcode: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> LabOrder:
        """Record specimen phlebotomy/collection and assign laboratory barcode."""
        if context:
            RBACManager.check_permission(context, "lab:collect_sample")

        order = self.lab_order_repo.get_by_id_or_raise(order_id)
        if order.status != LabOrderStatus.ORDERED:
            raise ConflictError(f"Cannot collect specimen for order in status {order.status.value}")

        generated_barcode = barcode or f"SPM-{int(time.time())}-{order_id[:4].upper()}"
        order.collect_sample(generated_barcode, technician_id)
        return self.lab_order_repo.save(order)

    def submit_results(
        self,
        order_id: str,
        measurements: List[dict],  # list of {"test_type_id": str, "value": float, "notes": Optional[str]}
        technician_notes: Optional[str] = None,
        context: Optional[UserContext] = None,
    ) -> LabOrder:
        """Process assay readings, evaluate against biological reference ranges, and complete order."""
        if context:
            RBACManager.check_permission(context, "lab:verify")

        order = self.lab_order_repo.get_by_id_or_raise(order_id)
        if order.status not in (LabOrderStatus.SAMPLE_COLLECTED, LabOrderStatus.PROCESSING):
            raise ConflictError("Specimen must be collected before submitting results.")

        result_items: List[LabResultItem] = []
        for item in measurements:
            tt_id = item["test_type_id"]
            val = float(item["value"])
            test_type = self.test_type_repo.get_by_id_or_raise(tt_id)

            flag = AbnormalityFlag.NORMAL
            range_disp = "N/A"
            unit = ""
            if test_type.reference_range:
                flag = test_type.reference_range.evaluate(val)
                range_disp = f"{test_type.reference_range.low_value} - {test_type.reference_range.high_value} {test_type.reference_range.unit_of_measure}"
                unit = test_type.reference_range.unit_of_measure

            result_item = LabResultItem(
                parameter_name=test_type.name,
                measured_value=val,
                unit_of_measure=unit,
                reference_range_display=range_disp,
                flag=flag,
                notes=item.get("notes"),
            )
            result_items.append(result_item)

        order.submit_results(result_items, technician_notes)
        self.lab_order_repo.save(order)

        actor_id = context.user_id if context else "SYSTEM"
        actor_role = context.role.value if context else "SYSTEM"
        audit_service.log(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.UPDATE,
            resource_type="LabOrder",
            resource_id=order_id,
            details={"has_critical": str(order.has_critical_values), "results_count": str(len(result_items))},
        )

        return order
