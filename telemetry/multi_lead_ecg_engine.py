"""
HealthSphere 12-Lead Electrocardiogram (ECG) Vector Projection Engine
Implements Einthoven's triangle, Goldberger unipolar limb leads, and Wilson precordial lead models.
"""

import math
from typing import Dict, List, Any


class TwelveLeadECGEngine:
    """Mathematical multi-lead ECG synthesis and spatial cardiac dipole projections."""

    # Lead projection angles in frontal and horizontal planes
    LEAD_ANGLES = {
        "I": 0.0,
        "II": 60.0,
        "III": 120.0,
        "aVR": -150.0,
        "aVL": -30.0,
        "aVF": 90.0,
        "V1": 120.0,
        "V2": 90.0,
        "V3": 60.0,
        "V4": 30.0,
        "V5": 0.0,
        "V6": -30.0,
    }

    @classmethod
    def synthesize_12_leads(
        cls,
        heart_rate_bpm: int = 72,
        duration_seconds: float = 2.5,
        sampling_rate_hz: int = 250,
        has_st_elevation_stemi: bool = False,
    ) -> Dict[str, List[Dict[str, float]]]:
        """
        Synthesize simultaneous 12-lead voltage waveforms.
        """
        leads_output = {lead: [] for lead in cls.LEAD_ANGLES}
        total_samples = int(duration_seconds * sampling_rate_hz)
        rr_sec = 60.0 / heart_rate_bpm
        samples_per_beat = int(rr_sec * sampling_rate_hz)

        for i in range(total_samples):
            t = i / sampling_rate_hz
            t_beat = (i % samples_per_beat) / sampling_rate_hz

            # Dipole components in 2D cardiac vector plane
            p_dipole = 0.20 * math.exp(-((t_beat - 0.16 * rr_sec) ** 2) / (2 * 0.03 ** 2))
            q_dipole = -0.15 * math.exp(-((t_beat - 0.23 * rr_sec) ** 2) / (2 * 0.015 ** 2))
            r_dipole = 1.40 * math.exp(-((t_beat - 0.26 * rr_sec) ** 2) / (2 * 0.02 ** 2))
            s_dipole = -0.30 * math.exp(-((t_beat - 0.29 * rr_sec) ** 2) / (2 * 0.02 ** 2))
            t_dipole = 0.35 * math.exp(-((t_beat - 0.46 * rr_sec) ** 2) / (2 * 0.07 ** 2))

            # STEMI ST-Elevation segment
            st_elevation = 0.0
            if has_st_elevation_stemi and (0.29 * rr_sec <= t_beat <= 0.42 * rr_sec):
                st_elevation = 0.35 * math.sin(math.pi * (t_beat - 0.29 * rr_sec) / (0.13 * rr_sec))

            base_signal = p_dipole + q_dipole + r_dipole + s_dipole + t_dipole + st_elevation

            for lead, angle_deg in cls.LEAD_ANGLES.items():
                rad = math.radians(angle_deg)
                # Geometric vector projection
                lead_voltage = base_signal * math.cos(rad)
                leads_output[lead].append({
                    "time_sec": round(t, 4),
                    "voltage_mv": round(lead_voltage, 4),
                })

        return leads_output
