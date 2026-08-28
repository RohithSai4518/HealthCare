"""
HealthSphere Healthcare Information & EHR Platform Entry Point
Supports running the interactive CLI, starting the REST API server, running test suites, or seeding synthetic data.
"""

import argparse
import sys
import unittest
from api.server import HealthSphereAppContext, create_server
from cli.console import HealthSphereCLI
from generators.fhir_exporter import FHIRExporter
from generators.synthetic_data import SyntheticDataGenerator


def run_tests():
    """Execute all automated test suites."""
    print("=" * 70)
    print(" Running HealthSphere Automated Test Suite")
    print("=" * 70)
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    runner = unittest.runner.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


def seed_data(count: int = 10):
    """Seed synthetic patient records and export sample FHIR bundle."""
    print(f"[*] Initializing HealthSphere and generating {count} synthetic clinical records...")
    context = HealthSphereAppContext()
    generator = SyntheticDataGenerator(
        context.patient_service,
        context.appointment_service,
        context.clinical_service,
        context.pharmacy_service,
        context.lab_service,
        context.billing_service,
    )
    patients = generator.seed_synthetic_patients_and_scenarios(patient_count=count)
    print(f"[+] Successfully generated {len(patients)} synthetic patient charts.")

    if patients:
        sample_p = patients[0]
        encs = context.encounter_repo.get_by_patient(sample_p.id)
        labs = context.lab_order_repo.get_by_patient(sample_p.id)
        bundle_str = FHIRExporter.export_patient_bundle(sample_p, encs, labs)
        with open("sample_fhir_patient_bundle.json", "w", encoding="utf-8") as f:
            f.write(bundle_str)
        print(f"[+] Exported sample HL7 FHIR R4 Bundle to 'sample_fhir_patient_bundle.json'.")


def start_api_server(host: str = "127.0.0.1", port: int = 8000, seed: bool = True):
    """Launch RESTful HTTP Server."""
    context = HealthSphereAppContext()
    if seed:
        generator = SyntheticDataGenerator(
            context.patient_service,
            context.appointment_service,
            context.clinical_service,
            context.pharmacy_service,
            context.lab_service,
            context.billing_service,
        )
        generator.seed_synthetic_patients_and_scenarios(patient_count=5)

    server = create_server(host=host, port=port, context=context)
    print("=" * 70)
    print(f" HealthSphere RESTful API Server running at http://{host}:{port}")
    print(" Available endpoints:")
    print("   GET  /api/health")
    print("   POST /api/auth/login")
    print("   GET  /api/patients")
    print("   POST /api/patients")
    print("   GET  /api/patients/<id>")
    print("   GET  /api/patients/<id>/fhir")
    print("   GET  /api/doctors")
    print("   POST /api/appointments")
    print("   POST /api/encounters")
    print("   POST /api/encounters/<id>/vitals")
    print("   POST /api/prescriptions")
    print("   GET  /api/medications")
    print("   GET  /api/lab-tests")
    print("   POST /api/invoices")
    print("   GET  /api/audit-logs")
    print("=" * 70)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping API server.")
        server.server_close()


def main():
    parser = argparse.ArgumentParser(description="HealthSphere Healthcare Management System")
    parser.add_argument("--cli", action="store_true", help="Launch interactive clinical CLI console")
    parser.add_argument("--serve", action="store_true", help="Start REST API HTTP server")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="API server host")
    parser.add_argument("--port", type=int, default=8000, help="API server port")
    parser.add_argument("--test", action="store_true", help="Execute automated test suite")
    parser.add_argument("--seed", type=int, nargs="?", const=10, help="Generate synthetic patient records")

    args = parser.parse_args()

    if args.test:
        run_tests()
    elif args.serve:
        start_api_server(host=args.host, port=args.port)
    elif args.seed is not None:
        seed_data(args.seed)
    else:
        # Default to interactive CLI
        cli = HealthSphereCLI()
        cli.run()


if __name__ == "__main__":
    main()
