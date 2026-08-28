"""
HealthSphere HL7 FHIR R4 JSON Serializer
Exports synthetic patient records, clinical encounters, diagnostic reports, and medications into standard FHIR resources.
"""

import json
from typing import Any, Dict, List
from domain.clinical import Encounter
from domain.laboratory import LabOrder
from domain.patient import Patient
from domain.pharmacy import Prescription


class FHIRExporter:
    """Converts HealthSphere domain entities into HL7 FHIR R4 compliant JSON payloads."""

    @staticmethod
    def export_patient_resource(patient: Patient) -> Dict[str, Any]:
        """Convert Patient into FHIR R4 Patient Resource."""
        gender_map = {
            "MALE": "male",
            "FEMALE": "female",
            "OTHER": "other",
            "UNKNOWN": "unknown",
        }

        fhir_patient = {
            "resourceType": "Patient",
            "id": patient.id,
            "identifier": [
                {
                    "use": "official",
                    "type": {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                "code": "MR",
                                "display": "Medical Record Number",
                            }
                        ]
                    },
                    "system": "urn:oid:healthsphere:patient:mrn",
                    "value": patient.mrn,
                }
            ],
            "active": patient.is_active,
            "name": [
                {
                    "use": "official",
                    "family": patient.last_name,
                    "given": [patient.first_name],
                }
            ],
            "gender": gender_map.get(patient.gender.value, "unknown"),
            "birthDate": patient.date_of_birth,
        }

        if patient.contact:
            telecoms = []
            if patient.contact.phone_primary:
                telecoms.append({
                    "system": "phone",
                    "value": patient.contact.phone_primary,
                    "use": "mobile",
                })
            if patient.contact.email:
                telecoms.append({
                    "system": "email",
                    "value": patient.contact.email,
                })
            fhir_patient["telecom"] = telecoms

        if patient.address:
            fhir_patient["address"] = [
                {
                    "use": "home",
                    "line": [patient.address.street],
                    "city": patient.address.city,
                    "state": patient.address.state_or_province,
                    "postalCode": patient.address.postal_code,
                    "country": patient.address.country,
                }
            ]

        return fhir_patient

    @staticmethod
    def export_encounter_resource(encounter: Encounter) -> Dict[str, Any]:
        """Convert Encounter into FHIR R4 Encounter Resource."""
        fhir_encounter = {
            "resourceType": "Encounter",
            "id": encounter.id,
            "status": "finished" if encounter.status.value == "DISCHARGED" else "in-progress",
            "class": {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "AMB",
                "display": "ambulatory",
            },
            "subject": {
                "reference": f"Patient/{encounter.patient_id}",
            },
            "participant": [
                {
                    "individual": {
                        "reference": f"Practitioner/{encounter.attending_doctor_id}",
                    }
                }
            ],
            "period": {
                "start": encounter.start_time,
                "end": encounter.end_time,
            },
            "reasonCode": [
                {
                    "text": encounter.chief_complaint,
                }
            ],
        }

        if encounter.diagnoses:
            fhir_encounter["diagnosis"] = [
                {
                    "condition": {
                        "display": f"{d.icd10_code} - {d.description}",
                    },
                    "use": {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                                "code": "AD" if d.is_primary else "DD",
                                "display": "Admission diagnosis" if d.is_primary else "Discharge diagnosis",
                            }
                        ]
                    },
                }
                for d in encounter.diagnoses
            ]

        return fhir_encounter

    @staticmethod
    def export_diagnostic_report(lab_order: LabOrder) -> Dict[str, Any]:
        """Convert LabOrder with results into FHIR R4 DiagnosticReport Resource."""
        report = {
            "resourceType": "DiagnosticReport",
            "id": lab_order.id,
            "status": "final" if lab_order.status.value == "COMPLETED" else "preliminary",
            "subject": {
                "reference": f"Patient/{lab_order.patient_id}",
            },
            "effectiveDateTime": lab_order.completed_at or lab_order.created_at,
            "conclusion": lab_order.technician_notes or "Lab assays processed.",
            "result": [
                {
                    "parameter": item.parameter_name,
                    "valueQuantity": {
                        "value": item.measured_value,
                        "unit": item.unit_of_measure,
                    },
                    "interpretation": item.flag.value,
                    "referenceRange": item.reference_range_display,
                }
                for item in lab_order.results
            ],
        }
        return report

    @classmethod
    def export_patient_bundle(
        cls,
        patient: Patient,
        encounters: List[Encounter],
        lab_orders: List[LabOrder],
    ) -> str:
        """Export entire patient record history into a standard FHIR Bundle JSON string."""
        entries = []
        entries.append({"resource": cls.export_patient_resource(patient)})

        for enc in encounters:
            entries.append({"resource": cls.export_encounter_resource(enc)})

        for lab in lab_orders:
            entries.append({"resource": cls.export_diagnostic_report(lab)})

        bundle = {
            "resourceType": "Bundle",
            "type": "collection",
            "total": len(entries),
            "entry": entries,
        }
        return json.dumps(bundle, indent=2)
