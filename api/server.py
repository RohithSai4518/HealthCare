"""
HealthSphere RESTful HTTP API Server
Native standard-library HTTP server exposing clinical, administrative, and pharmacy REST endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Any, Dict, Optional, Tuple
from urllib.parse import parse_qs, urlparse
from api.web_ui import HTML_DASHBOARD
from core.enums import Gender, UserRole
from core.exceptions import HealthSphereException
from core.security import PasswordHasher, SessionManager, UserContext
from domain.models import Address, ContactInfo, InsurancePolicy
from domain.patient import Allergy
from repositories.memory_repo import (
    AppointmentRepository,
    ClaimRepository,
    DoctorRepository,
    EncounterRepository,
    InventoryRepository,
    InvoiceRepository,
    LabOrderRepository,
    LabTestTypeRepository,
    MedicationRepository,
    PatientRepository,
    PrescriptionRepository,
    UserAccount,
    UserRepository,
)
from services.appointment_service import AppointmentService
from services.billing_service import BillingService
from services.clinical_service import ClinicalService
from services.lab_service import LabService
from services.patient_service import PatientService
from services.pharmacy_service import PharmacyService


class HealthSphereAppContext:
    """Dependency injection container for all repositories and services."""

    def __init__(self):
        # Repositories
        self.patient_repo = PatientRepository()
        self.doctor_repo = DoctorRepository()
        self.appointment_repo = AppointmentRepository()
        self.encounter_repo = EncounterRepository()
        self.medication_repo = MedicationRepository()
        self.prescription_repo = PrescriptionRepository()
        self.inventory_repo = InventoryRepository()
        self.lab_test_repo = LabTestTypeRepository()
        self.lab_order_repo = LabOrderRepository()
        self.invoice_repo = InvoiceRepository()
        self.claim_repo = ClaimRepository()
        self.user_repo = UserRepository()

        # Services
        self.session_manager = SessionManager()
        self.patient_service = PatientService(self.patient_repo)
        self.appointment_service = AppointmentService(
            self.appointment_repo, self.doctor_repo, self.patient_repo
        )
        self.clinical_service = ClinicalService(
            self.encounter_repo, self.patient_repo, self.doctor_repo, self.appointment_repo
        )
        self.pharmacy_service = PharmacyService(
            self.medication_repo,
            self.prescription_repo,
            self.inventory_repo,
            self.patient_repo,
            self.doctor_repo,
        )
        self.lab_service = LabService(
            self.lab_order_repo, self.lab_test_repo, self.patient_repo, self.doctor_repo
        )
        self.billing_service = BillingService(
            self.invoice_repo, self.claim_repo, self.patient_repo, self.encounter_repo
        )

        self._seed_default_users()

    def _seed_default_users(self):
        admin = UserAccount(
            username="admin",
            password_hash=PasswordHasher.hash_password("Admin@123"),
            role=UserRole.ADMIN,
        )
        doctor = UserAccount(
            username="dr_smith",
            password_hash=PasswordHasher.hash_password("Doctor@123"),
            role=UserRole.DOCTOR,
        )
        self.user_repo.save(admin)
        self.user_repo.save(doctor)


class HealthSphereRequestHandler(BaseHTTPRequestHandler):
    """Handles incoming HTTP requests and dispatches to REST controller methods."""

    app_context: HealthSphereAppContext = None

    def _send_html_response(self, status_code: int, html_content: str):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

    def _send_json_response(self, status_code: int, payload: Any):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.end_headers()

        response_bytes = json.dumps(payload, default=str).encode("utf-8")
        self.wfile.write(response_bytes)

    def _read_json_body(self) -> Dict[str, Any]:
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0:
            return {}
        body = self.rfile.read(content_length).decode("utf-8")
        return json.loads(body)

    def _get_auth_context(self) -> Optional[UserContext]:
        auth_header = self.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ", 1)[1].strip()
            try:
                return self.app_context.session_manager.validate_token(token)
            except Exception:
                return None
        return None

    def do_OPTIONS(self):
        self._send_json_response(200, {"status": "ok"})

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        context = self._get_auth_context()

        try:
            if path in ("/", "/index.html"):
                self._send_html_response(200, HTML_DASHBOARD)

            elif path == "/api/health":
                self._send_json_response(200, {"status": "HEALTHY", "version": "1.0.0"})

            elif path == "/api/patients":
                q = query_params.get("query", [""])[0]
                if q:
                    patients = self.app_context.patient_service.search_patients(q, context)
                else:
                    patients = self.app_context.patient_repo.get_all()
                self._send_json_response(200, [p.to_dict() for p in patients])

            elif path.startswith("/api/patients/") and not path.endswith("/fhir"):
                patient_id = path.split("/")[3]
                patient = self.app_context.patient_service.get_patient_by_id(patient_id, context)
                self._send_json_response(200, patient.to_dict())

            elif path.startswith("/api/patients/") and path.endswith("/fhir"):
                patient_id = path.split("/")[3]
                patient = self.app_context.patient_service.get_patient_by_id(patient_id, context)
                from generators.fhir_exporter import FHIRExporter
                encs = self.app_context.encounter_repo.get_by_patient(patient_id)
                labs = self.app_context.lab_order_repo.get_by_patient(patient_id)
                bundle_json = FHIRExporter.export_patient_bundle(patient, encs, labs)
                self._send_json_response(200, json.loads(bundle_json))

            elif path == "/api/doctors":
                doctors = self.app_context.doctor_repo.get_all()
                self._send_json_response(200, [d.to_dict() for d in doctors])

            elif path == "/api/medications":
                meds = self.app_context.medication_repo.get_all()
                self._send_json_response(200, [m.to_dict() for m in meds])

            elif path == "/api/lab-tests":
                tests = self.app_context.lab_test_repo.get_all()
                self._send_json_response(200, [t.to_dict() for t in tests])

            elif path == "/api/audit-logs":
                from core.audit import audit_service
                logs = audit_service.get_logs()
                self._send_json_response(200, [l.__dict__ for l in logs])

            else:
                self._send_json_response(404, {"error": "Not Found", "path": path})

        except HealthSphereException as exc:
            self._send_json_response(400, exc.to_dict())
        except Exception as exc:
            self._send_json_response(500, {"error": "Internal Server Error", "message": str(exc)})

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        context = self._get_auth_context()

        try:
            body = self._read_json_body()

            if path == "/api/seed":
                from generators.synthetic_data import SyntheticDataGenerator
                generator = SyntheticDataGenerator(
                    self.app_context.patient_service,
                    self.app_context.appointment_service,
                    self.app_context.clinical_service,
                    self.app_context.pharmacy_service,
                    self.app_context.lab_service,
                    self.app_context.billing_service,
                )
                seeded = generator.seed_synthetic_patients_and_scenarios(patient_count=5)
                self._send_json_response(200, {"status": "SUCCESS", "message": f"Generated {len(seeded)} synthetic patient charts."})

            elif path == "/api/auth/login":
                username = body.get("username", "")
                password = body.get("password", "")
                user = self.app_context.user_repo.get_by_username(username)
                if not user or not PasswordHasher.verify_password(password, user.password_hash):
                    self._send_json_response(401, {"error": "Invalid username or password."})
                    return

                token = self.app_context.session_manager.create_session(
                    user_id=user.id,
                    username=user.username,
                    role=user.role,
                )
                self._send_json_response(200, {"token": token, "username": user.username, "role": user.role.value})

            elif path == "/api/patients":
                addr_data = body.get("address")
                address = Address(**addr_data) if addr_data else None
                contact_data = body.get("contact")
                contact = ContactInfo(**contact_data) if contact_data else None

                patient = self.app_context.patient_service.register_patient(
                    first_name=body["first_name"],
                    last_name=body["last_name"],
                    date_of_birth=body["date_of_birth"],
                    gender=Gender(body.get("gender", "UNKNOWN")),
                    address=address,
                    contact=contact,
                    context=context,
                )
                self._send_json_response(201, patient.to_dict())

            elif path == "/api/appointments":
                appointment = self.app_context.appointment_service.book_appointment(
                    patient_id=body["patient_id"],
                    doctor_id=body["doctor_id"],
                    slot_id=body["slot_id"],
                    reason_for_visit=body.get("reason_for_visit", "Routine"),
                    context=context,
                )
                self._send_json_response(201, appointment.to_dict())

            elif path == "/api/encounters":
                encounter = self.app_context.clinical_service.start_encounter(
                    patient_id=body["patient_id"],
                    attending_doctor_id=body["doctor_id"],
                    chief_complaint=body.get("chief_complaint", ""),
                    context=context,
                )
                self._send_json_response(201, encounter.to_dict())

            elif path.startswith("/api/encounters/") and path.endswith("/vitals"):
                encounter_id = path.split("/")[3]
                vitals = self.app_context.clinical_service.record_vitals(
                    encounter_id=encounter_id,
                    systolic_bp=int(body["systolic_bp"]),
                    diastolic_bp=int(body["diastolic_bp"]),
                    heart_rate_bpm=int(body["heart_rate_bpm"]),
                    respiratory_rate=int(body["respiratory_rate"]),
                    temperature_celsius=float(body["temperature_celsius"]),
                    spo2_percentage=float(body["spo2_percentage"]),
                    height_cm=float(body["height_cm"]),
                    weight_kg=float(body["weight_kg"]),
                    recorded_by_staff_id=context.user_id if context else "STAFF-01",
                    context=context,
                )
                self._send_json_response(200, vitals.to_dict())

            elif path == "/api/prescriptions":
                prescription = self.app_context.pharmacy_service.create_prescription(
                    patient_id=body["patient_id"],
                    doctor_id=body["doctor_id"],
                    items_data=body["items"],
                    clinical_rationale=body.get("clinical_rationale"),
                    context=context,
                )
                self._send_json_response(201, prescription.to_dict())

            elif path == "/api/invoices":
                invoice = self.app_context.billing_service.create_invoice(
                    patient_id=body["patient_id"],
                    items_data=body["items"],
                    context=context,
                )
                self._send_json_response(201, invoice.to_dict())

            else:
                self._send_json_response(404, {"error": "Endpoint not found."})

        except HealthSphereException as exc:
            self._send_json_response(400, exc.to_dict())
        except Exception as exc:
            self._send_json_response(500, {"error": "Internal Server Error", "message": str(exc)})


def create_server(host: str = "127.0.0.1", port: int = 8000, context: Optional[HealthSphereAppContext] = None) -> HTTPServer:
    """Create configured HTTP server instance."""
    app_ctx = context or HealthSphereAppContext()
    HealthSphereRequestHandler.app_context = app_ctx
    return HTTPServer((host, port), HealthSphereRequestHandler)
