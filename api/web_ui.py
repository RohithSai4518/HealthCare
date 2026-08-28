"""
HealthSphere Embedded Clinical Web Dashboard UI
Clean, modern, single-page application (SPA) built with vanilla HTML/CSS/JS.
"""

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HealthSphere Enterprise Healthcare Platform</title>
  <style>
    :root {
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --primary-light: #e0f2fe;
      --success: #16a34a;
      --warning: #d97706;
      --danger: #dc2626;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }
    
    /* Sidebar */
    .sidebar { width: 260px; background: #0f172a; color: white; display: flex; flex-direction: column; }
    .sidebar-header { padding: 24px 20px; border-bottom: 1px solid #1e293b; }
    .sidebar-header h1 { font-size: 20px; font-weight: 700; color: #38bdf8; display: flex; align-items: center; gap: 8px; }
    .sidebar-header p { font-size: 11px; color: #94a3b8; margin-top: 4px; }
    .nav-links { list-style: none; padding: 16px 8px; flex: 1; overflow-y: auto; }
    .nav-item { padding: 12px 16px; margin-bottom: 4px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 500; color: #cbd5e1; transition: all 0.2s; }
    .nav-item:hover, .nav-item.active { background: #1e293b; color: #38bdf8; }
    .sidebar-footer { padding: 16px 20px; border-top: 1px solid #1e293b; font-size: 12px; color: #64748b; }

    /* Main Content */
    .main { flex: 1; display: flex; flex-direction: column; overflow-y: auto; }
    .topbar { background: var(--card-bg); border-bottom: 1px solid var(--border); padding: 16px 32px; display: flex; justify-content: space-between; align-items: center; }
    .topbar h2 { font-size: 20px; font-weight: 600; }
    .topbar-actions { display: flex; gap: 12px; }
    .btn { padding: 8px 16px; border-radius: 6px; border: none; font-size: 13px; font-weight: 600; cursor: pointer; transition: background 0.2s; display: inline-flex; align-items: center; gap: 6px; }
    .btn-primary { background: var(--primary); color: white; }
    .btn-primary:hover { background: var(--primary-dark); }
    .btn-secondary { background: #e2e8f0; color: var(--text); }
    .btn-secondary:hover { background: #cbd5e1; }
    
    .content { padding: 32px; }
    
    /* Stats Grid */
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 32px; }
    .stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .stat-title { font-size: 13px; color: var(--text-muted); font-weight: 500; }
    .stat-value { font-size: 28px; font-weight: 700; margin-top: 8px; color: var(--text); }
    .stat-badge { display: inline-block; padding: 2px 8px; border-radius: 999px; font-size: 11px; font-weight: 600; margin-top: 8px; }
    .badge-green { background: #dcfce7; color: var(--success); }
    
    /* Cards & Tables */
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .card-title { font-size: 16px; font-weight: 600; }
    table { width: 100%; border-collapse: collapse; text-align: left; font-size: 13px; }
    th { padding: 12px 16px; background: #f8fafc; color: var(--text-muted); font-weight: 600; border-bottom: 1px solid var(--border); }
    td { padding: 14px 16px; border-bottom: 1px solid var(--border); }
    tr:hover td { background: #f8fafc; }
    
    /* Tags */
    .tag { display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; }
    .tag-blue { background: var(--primary-light); color: var(--primary-dark); }
    .tag-green { background: #dcfce7; color: var(--success); }
    .tag-yellow { background: #fef3c7; color: var(--warning); }
    .tag-red { background: #fee2e2; color: var(--danger); }

    /* Modal / JSON Drawer */
    .json-box { background: #0f172a; color: #38bdf8; padding: 16px; border-radius: 8px; font-family: monospace; font-size: 12px; max-height: 400px; overflow-y: auto; white-space: pre-wrap; }
    .tab-pane { display: none; }
    .tab-pane.active { display: block; }
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <h1>HealthSphere</h1>
      <p>Clinical EHR & Hospital Information Platform</p>
    </div>
    <ul class="nav-links">
      <li class="nav-item active" onclick="switchTab('dashboard')">📊 Dashboard</li>
      <li class="nav-item" onclick="switchTab('patients')">👥 Patients & EHR</li>
      <li class="nav-item" onclick="switchTab('doctors')">👨‍⚕️ Clinicians & Slots</li>
      <li class="nav-item" onclick="switchTab('pharmacy')">💊 Pharmacy & Formulary</li>
      <li class="nav-item" onclick="switchTab('laboratory')">🧪 Diagnostic LIS</li>
      <li class="nav-item" onclick="switchTab('audit')">🛡️ HIPAA Audit Trail</li>
    </ul>
    <div class="sidebar-footer">
      <div>Zero PII / HIPAA Compliant</div>
      <div style="margin-top: 4px; color: #38bdf8;">Python 3.11 Clean Architecture</div>
    </div>
  </aside>

  <!-- Main Content Area -->
  <main class="main">
    <header class="topbar">
      <h2 id="pageTitle">Clinical Operations Overview</h2>
      <div class="topbar-actions">
        <button class="btn btn-secondary" onclick="seedSyntheticData()">⚡ Generate Synthetic Data</button>
        <button class="btn btn-primary" onclick="refreshData()">🔄 Refresh</button>
      </div>
    </header>

    <div class="content">

      <!-- TAB: DASHBOARD -->
      <section id="pane-dashboard" class="tab-pane active">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-title">Registered Patients</div>
            <div class="stat-value" id="statPatients">0</div>
            <span class="stat-badge badge-green">100% Synthetic PHI</span>
          </div>
          <div class="stat-card">
            <div class="stat-title">Active Clinicians</div>
            <div class="stat-value" id="statDoctors">0</div>
            <span class="stat-badge badge-green">Scheduled Slots</span>
          </div>
          <div class="stat-card">
            <div class="stat-title">Formulary Drugs</div>
            <div class="stat-value" id="statMeds">0</div>
            <span class="stat-badge badge-green">Interaction Matrix Active</span>
          </div>
          <div class="stat-card">
            <div class="stat-title">Diagnostic Assays</div>
            <div class="stat-value" id="statLabs">0</div>
            <span class="stat-badge badge-green">LOINC/CPT Mapped</span>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <h3 class="card-title">Recent Clinical Activity & Patients</h3>
          </div>
          <table>
            <thead>
              <tr>
                <th>MRN</th>
                <th>Patient Name</th>
                <th>DOB</th>
                <th>Gender</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="dashboardPatientsTable">
              <tr><td colspan="6" style="text-align: center; color: var(--text-muted);">Loading patient records...</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- TAB: PATIENTS -->
      <section id="pane-patients" class="tab-pane">
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">Patient Directory & Electronic Health Records</h3>
          </div>
          <table>
            <thead>
              <tr>
                <th>MRN</th>
                <th>Name</th>
                <th>DOB</th>
                <th>Gender</th>
                <th>Blood Group</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="patientsDirectoryTable"></tbody>
          </table>
        </div>

        <div class="card" id="patientFhirCard" style="display: none;">
          <div class="card-header">
            <h3 class="card-title">HL7 FHIR R4 Standard Export Bundle</h3>
            <button class="btn btn-secondary" onclick="document.getElementById('patientFhirCard').style.display='none'">Close</button>
          </div>
          <div class="json-box" id="patientFhirContent"></div>
        </div>
      </section>

      <!-- TAB: DOCTORS -->
      <section id="pane-doctors" class="tab-pane">
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">Attending Clinicians & Medical Specialties</h3>
          </div>
          <table>
            <thead>
              <tr>
                <th>License</th>
                <th>Doctor Name</th>
                <th>Specialty</th>
                <th>Department</th>
                <th>Consultation Fee</th>
              </tr>
            </thead>
            <tbody id="doctorsTable"></tbody>
          </table>
        </div>
      </section>

      <!-- TAB: PHARMACY -->
      <section id="pane-pharmacy" class="tab-pane">
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">Formulary & Pharmaceutical Drug Catalog</h3>
          </div>
          <table>
            <thead>
              <tr>
                <th>NDC Code</th>
                <th>Brand Name</th>
                <th>Generic Name</th>
                <th>Strength & Form</th>
                <th>Unit Price</th>
              </tr>
            </thead>
            <tbody id="pharmacyTable"></tbody>
          </table>
        </div>
      </section>

      <!-- TAB: LABORATORY -->
      <section id="pane-laboratory" class="tab-pane">
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">Diagnostic Laboratory Test Catalog (LOINC/CPT)</h3>
          </div>
          <table>
            <thead>
              <tr>
                <th>Code</th>
                <th>Test Name</th>
                <th>Category</th>
                <th>Sample Required</th>
                <th>Reference Range</th>
                <th>Price</th>
              </tr>
            </thead>
            <tbody id="laboratoryTable"></tbody>
          </table>
        </div>
      </section>

      <!-- TAB: AUDIT -->
      <section id="pane-audit" class="tab-pane">
        <div class="card">
          <div class="card-header">
            <h3 class="card-title">HIPAA Immutable Audit Trail (SHA-256 Hash Chained)</h3>
            <span class="tag tag-green">Integrity: Cryptographically Verified</span>
          </div>
          <table>
            <thead>
              <tr>
                <th>Timestamp (UTC)</th>
                <th>Actor</th>
                <th>Role</th>
                <th>Action</th>
                <th>Resource</th>
                <th>Hash Chain</th>
              </tr>
            </thead>
            <tbody id="auditTable"></tbody>
          </table>
        </div>
      </section>

    </div>
  </main>

  <script>
    function switchTab(tabId) {
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
      
      const pane = document.getElementById('pane-' + tabId);
      if (pane) pane.classList.add('active');
      
      const titles = {
        'dashboard': 'Clinical Operations Overview',
        'patients': 'Patient Management & EHR Charts',
        'doctors': 'Clinicians & Medical Staff',
        'pharmacy': 'Pharmacy Formulary & Drug Safety',
        'laboratory': 'Diagnostic Laboratory Information System',
        'audit': 'HIPAA Security & Audit Logs'
      };
      document.getElementById('pageTitle').textContent = titles[tabId] || 'HealthSphere Platform';
      event.currentTarget.classList.add('active');
    }

    async function refreshData() {
      try {
        const [patients, doctors, meds, labs, audits] = await Promise.all([
          fetch('/api/patients').then(r => r.json()),
          fetch('/api/doctors').then(r => r.json()),
          fetch('/api/medications').then(r => r.json()),
          fetch('/api/lab-tests').then(r => r.json()),
          fetch('/api/audit-logs').then(r => r.json())
        ]);

        document.getElementById('statPatients').textContent = patients.length;
        document.getElementById('statDoctors').textContent = doctors.length;
        document.getElementById('statMeds').textContent = meds.length;
        document.getElementById('statLabs').textContent = labs.length;

        // Populate Dashboard Patients
        const dBody = document.getElementById('dashboardPatientsTable');
        dBody.innerHTML = patients.length ? patients.slice(0, 5).map(p => `
          <tr>
            <td><strong>${p.mrn}</strong></td>
            <td>${p.first_name} ${p.last_name}</td>
            <td>${p.date_of_birth}</td>
            <td><span class="tag tag-blue">${p.gender}</span></td>
            <td><span class="tag tag-green">Active</span></td>
            <td><button class="btn btn-secondary" onclick="viewFhir('${p.id}')">View FHIR</button></td>
          </tr>
        `).join('') : '<tr><td colspan="6" style="text-align: center; color: var(--text-muted);">No records found. Click "Generate Synthetic Data" to populate.</td></tr>';

        // Populate Directory Patients
        const dirBody = document.getElementById('patientsDirectoryTable');
        dirBody.innerHTML = patients.map(p => `
          <tr>
            <td><strong>${p.mrn}</strong></td>
            <td>${p.first_name} ${p.last_name}</td>
            <td>${p.date_of_birth}</td>
            <td><span class="tag tag-blue">${p.gender}</span></td>
            <td>${p.blood_group || 'N/A'}</td>
            <td>
              <button class="btn btn-secondary" onclick="viewFhir('${p.id}')">Export FHIR JSON</button>
            </td>
          </tr>
        `).join('');

        // Populate Doctors
        const docBody = document.getElementById('doctorsTable');
        docBody.innerHTML = doctors.map(d => `
          <tr>
            <td>${d.license_number}</td>
            <td><strong>${d.first_name} ${d.last_name}</strong></td>
            <td><span class="tag tag-blue">${d.specialty}</span></td>
            <td>${d.department}</td>
            <td>$${d.consultation_fee.toFixed(2)}</td>
          </tr>
        `).join('');

        // Populate Pharmacy
        const pharmBody = document.getElementById('pharmacyTable');
        pharmBody.innerHTML = meds.map(m => `
          <tr>
            <td>${m.ndc_code}</td>
            <td><strong>${m.brand_name}</strong></td>
            <td>${m.generic_name}</td>
            <td>${m.strength} (${m.form})</td>
            <td>$${m.unit_price.toFixed(2)}</td>
          </tr>
        `).join('');

        // Populate Labs
        const labBody = document.getElementById('laboratoryTable');
        labBody.innerHTML = labs.map(l => `
          <tr>
            <td>${l.code}</td>
            <td><strong>${l.name}</strong></td>
            <td><span class="tag tag-blue">${l.category}</span></td>
            <td>${l.sample_type_required}</td>
            <td>${l.reference_range ? l.reference_range.low_value + ' - ' + l.reference_range.high_value + ' ' + l.reference_range.unit_of_measure : 'N/A'}</td>
            <td>$${l.standard_price.toFixed(2)}</td>
          </tr>
        `).join('');

        // Populate Audit Logs
        const auditBody = document.getElementById('auditTable');
        auditBody.innerHTML = audits.slice(-10).reverse().map(a => `
          <tr>
            <td>${a.timestamp.substring(0, 19)}</td>
            <td>${a.actor_id}</td>
            <td><span class="tag tag-blue">${a.actor_role}</span></td>
            <td><span class="tag tag-green">${a.action}</span></td>
            <td>${a.resource_type}:${a.resource_id.substring(0, 8)}</td>
            <td style="font-family: monospace; font-size: 11px;">${a.entry_hash.substring(0, 16)}...</td>
          </tr>
        `).join('');

      } catch (err) {
        console.error("Failed to load dashboard data:", err);
      }
    }

    async function viewFhir(patientId) {
      const res = await fetch('/api/patients/' + patientId + '/fhir');
      const data = await res.json();
      document.getElementById('patientFhirContent').textContent = JSON.stringify(data, null, 2);
      document.getElementById('patientFhirCard').style.display = 'block';
      document.getElementById('patientFhirCard').scrollIntoView({ behavior: 'smooth' });
    }

    async function seedSyntheticData() {
      await fetch('/api/seed', { method: 'POST' });
      await refreshData();
    }

    window.addEventListener('DOMContentLoaded', refreshData);
  </script>
</body>
</html>
"""
