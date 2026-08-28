"""
Real-Time ICU Telemetry Patient Monitor Stream Simulator
Emulates multi-parameter bedside physiological monitors with alarm threshold triggers.
"""

import random
from typing import Dict, Any, List


class TelemetryMonitorStream:
    """Emulates continuous bedside medical telemetry streams."""

    @staticmethod
    def generate_monitor_frame(
        patient_id: str,
        base_hr: int = 75,
        base_spo2: float = 98.0,
        base_sbp: int = 120,
        base_dbp: int = 80,
    ) -> Dict[str, Any]:
        """Generate a single real-time physiological sensor frame."""
        hr = max(30, min(220, base_hr + random.randint(-2, 2)))
        spo2 = max(70.0, min(100.0, base_spo2 + random.uniform(-0.5, 0.5)))
        sbp = max(50, min(250, base_sbp + random.randint(-3, 3)))
        dbp = max(30, min(140, base_dbp + random.randint(-2, 2)))
        resp = random.randint(14, 18)
        temp = round(36.8 + random.uniform(-0.2, 0.2), 1)

        alarms = []
        if hr > 120:
            alarms.append({"level": "WARNING", "parameter": "HEART_RATE", "message": f"Tachycardia ({hr} bpm)"})
        elif hr < 50:
            alarms.append({"level": "WARNING", "parameter": "HEART_RATE", "message": f"Bradycardia ({hr} bpm)"})
        if spo2 < 90.0:
            alarms.append({"level": "CRITICAL", "parameter": "SPO2", "message": f"Severe Desaturation ({spo2:.1f}%)"})
        if sbp > 180:
            alarms.append({"level": "CRITICAL", "parameter": "BP", "message": f"Hypertensive Crisis ({sbp}/{dbp})"})

        return {
            "patient_id": patient_id,
            "heart_rate_bpm": hr,
            "spo2_percent": round(spo2, 1),
            "blood_pressure_systolic": sbp,
            "blood_pressure_diastolic": dbp,
            "respiratory_rate": resp,
            "temperature_celsius": temp,
            "active_alarms": alarms,
        }
