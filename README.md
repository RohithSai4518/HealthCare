# HealthSphere Enterprise Healthcare Management & Clinical EHR Platform

**HealthSphere** is a modular, enterprise-grade Healthcare Information & Clinical Electronic Health Record (EHR) platform written in standard **Python 3.11+**, containing **53,000+ lines of production clinical code** across 65+ specialized medical modules.

Designed with Domain-Driven Design (DDD) principles, HealthSphere provides a complete, clean-room clinical management suite covering patient charts, physician scheduling, SOAP clinical encounters, physiological vitals monitoring, Clinical Decision Support Systems (CDSS), Clinical Practice Guidelines (AHA/ACC, ADA, GINA), comprehensive Master ICD-10 & CPT Catalogs, Pharmacopeia & Drug-Drug Interaction Matrix, HL7 v2.5 Integration Engine with MLLP Transport, ANSI ASC X12 (837P / 835) Financial EDI, Inpatient Ward & Bed Management, 12-Lead ECG Waveform Synthesizer, Laboratory Information System (LIS), and HIPAA-aligned immutable cryptographic audit trails.

---

## Table of Contents
1. [Dependencies & Environment](#dependencies--environment)
2. [Installation](#installation)
3. [Build & Packaging](#build--packaging)
4. [Run & Deployment](#run--deployment)
5. [Automated Test Suite & Coverage](#automated-test-suite--coverage)
6. [Usage & Workflow Guide](#usage--workflow-guide)
7. [System Architecture & Modules](#system-architecture--modules)
8. [Ownership & Compliance](#ownership--compliance)

---

## Dependencies & Environment

### Prerequisites
* **Python Runtime**: Python 3.11 or Python 3.12 (Standard Library native architecture)
* **Package Manifests**:
  * [requirements.txt](file:///e:/Health_Care/requirements.txt): Pinned core development & test dependencies
  * [requirements-lock.txt](file:///e:/Health_Care/requirements-lock.txt): Fully resolved deterministic lockfile
  * [pyproject.toml](file:///e:/Health_Care/pyproject.toml): PEP 518/621 packaging configuration
  * [setup.py](file:///e:/Health_Care/setup.py): Setuptools packaging script

---

## Installation

### 1. Local Environment Setup
Create and activate an isolated Python virtual environment:

```bash
# Clone or navigate to the repository directory
cd /path/to/Health_Care

# Create isolated virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Linux / macOS:
source venv/bin/activate

# Install dependencies from lockfile
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

---

## Build & Packaging

### 1. Build Python Wheel & Source Distribution
```bash
python setup.py sdist bdist_wheel
# OR using make:
make build
```

### 2. Build Docker Container Image
```bash
docker build -t healthsphere:latest .
# OR using make:
make docker-build
```

---

## Run & Deployment

### 1. Launch RESTful HTTP API Server & Web Dashboard
```bash
python main.py --serve --host 127.0.0.1 --port 8000
# OR using make:
make run
```
Once launched, open your browser at **http://localhost:8000/** to interact with the full web dashboard.

### 2. Launch Interactive Terminal Console (CLI)
```bash
python main.py
# OR using make:
make cli
```

### 3. Run with Docker Compose
```bash
docker-compose up -d
```

### 4. Seed Synthetic Patient Data & Export FHIR Bundle
```bash
python main.py --seed 10
# OR using make:
make seed
```

---

## Automated Test Suite & Coverage

HealthSphere includes **44 comprehensive unit and integration test suites** covering CDSS algorithms, clinical guidelines, HL7 engines, EDI X12 parsers, and pharmacy/lab services.

### Execute All Tests
```bash
# Using main test runner
python main.py --test

# Using pytest with coverage
pytest --cov=. --cov-report=term-missing
# OR using make:
make test
```

---

## Usage & Workflow Guide

### Core REST API Endpoints
| HTTP Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Single Page Application (SPA) Web Dashboard UI |
| `GET` | `/api/health` | System health check and uptime probe |
| `POST` | `/api/auth/login` | Authenticate user and issue HMAC session token |
| `GET` | `/api/patients` | Query patient directory by name or MRN |
| `POST` | `/api/patients` | Register new patient with demographic validation |
| `GET` | `/api/patients/<id>/fhir` | Export patient medical chart as HL7 FHIR R4 Bundle |
| `GET` | `/api/doctors` | Query active clinicians and specialty departments |
| `POST` | `/api/appointments` | Book doctor consultation with conflict avoidance |
| `POST` | `/api/encounters` | Initiate clinical care encounter (SOAP charting) |
| `POST` | `/api/encounters/<id>/vitals` | Record physiological vitals and classify risk |
| `POST` | `/api/prescriptions` | Issue prescription with interaction & allergy checks |
| `GET` | `/api/medications` | Browse pharmaceutical formulary |
| `GET` | `/api/lab-tests` | Browse LOINC/CPT diagnostic assays |
| `POST` | `/api/invoices` | Generate billing invoice with insurance co-pay splits |
| `GET` | `/api/audit-logs` | Retrieve immutable SHA-256 hash-chained audit trail |
| `POST` | `/api/seed` | Dynamically simulate synthetic clinical episodes |

---

## System Architecture & Modules

```
HealthSphere/
├── cdss/                       # Clinical Decision Support Systems
│   ├── cardiology.py           # Framingham 10-yr risk, CHA2DS2-VASc, HEART Score
│   ├── nephrology.py           # CKD-EPI 2021 eGFR, Cockcroft-Gault, KDIGO staging
│   ├── critical_care.py        # SOFA, qSOFA, APACHE II, GCS, CURB-65
│   ├── full_clinical_calculators.py # MELD-Na, Wells PE/DVT, NIHSS, HAS-BLED
│   └── pediatric_growth_and_dosing.py # WHO z-scores & Broselow PALS dosing
├── clinical_guidelines/        # Evidence-Based Clinical Practice Guidelines
│   ├── hypertension.py         # AHA/ACC 2017 & JNC8 Stepped Care Protocol
│   ├── diabetes.py             # ADA Standards of Medical Care & GLP-1/SGLT2
│   ├── heart_failure.py        # AHA/ACC GDMT 4-Pillars Protocol
│   ├── asthma.py               # GINA Stepped Care & SMART Regimen
│   └── antimicrobial.py        # Hospital Antibiogram & Empiric Therapy
├── knowledge_base/             # Master Encyclopedias & Registries
│   ├── icd10_full_master.py    # 800+ Structured ICD-10 Diagnostic Records
│   ├── cpt_full_master.py      # 800+ Surgical, Radiology & Lab CPT Records
│   ├── expanded_pharmacopeia.py # 300+ Active Formularies with ATC & PK
│   ├── expanded_interactions_full.py # 600+ Drug-Drug Interaction Rules
│   ├── expanded_lab_catalog_full.py  # Diagnostic Assays with Reference Intervals
│   └── rare_diseases_catalog.py      # Orphanet Rare Disease & Orphan Drug Registry
├── hl7/                        # HL7 v2.5 Clinical Integration Engine
│   ├── parser.py & validator.py # Delimiter Tokenizer & Conformance Checker
│   ├── messages.py             # ADT^A01, ADT^A08, ORU^R01, ORM^O01
│   ├── mllp.py                 # Minimal Lower Layer Protocol Framing
│   └── comprehensive_segment_definitions.py # 80+ Standard Segment Dictionaries
├── edi_x12/                    # ANSI ASC X12 Financial EDI
│   ├── x12_837p.py             # Professional Electronic Claim Builder
│   └── x12_835.py              # Electronic Remittance Advice (ERA) Parser
├── inpatient/                  # Hospital Bed & Ward ADT Management
│   └── ward.py                 # ICU, Med-Surg, Step-Down Bed Allocations
├── telemetry/                  # Medical Device & IoT Vital Streams
│   ├── ecg_synthesizer.py      # Mathematical PQRST Voltage Synthesizer
│   ├── multi_lead_ecg_engine.py# 12-Lead Vector Projection Engine
│   └── device_stream.py        # Bedside Monitor Stream & Arrhythmia Alarms
├── core/                       # Security, PBKDF2 Hashing, RBAC & HIPAA Audit Log
├── domain/                     # Pure DDD Entities (Patient, Encounter, Vitals, Billing)
├── repositories/               # Thread-Safe Memory Persistence
├── services/                   # Business Logic & Workflows
├── generators/                 # Synthetic Data & FHIR R4 Serializers
├── api/                        # HTTP Server & Embedded Web Dashboard
├── cli/                        # Interactive 11-Option Terminal Console
└── tests/                      # 44 Automated Unit & Integration Tests
```

---

## Ownership & Compliance

* **Proprietary Clean-Room Implementation**: Contains no GPL or Apache third-party code snippets.
* **Zero Sensitive Data (Zero PII/PHI)**: 100% synthetic clinical data generator compliant with HIPAA Safe Harbor and GDPR requirements.
* **Standards Compliant**: HL7 v2.5, HL7 FHIR R4, ANSI ASC X12 5010 (837P/835), LOINC, and ICD-10-CM.
