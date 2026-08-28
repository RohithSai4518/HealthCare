"""
Mathematical Electrocardiogram (ECG) Waveform Synthesizer
Generates realistic multi-lead P-Q-R-S-T voltage waveform intervals.
"""

import math
from typing import List, Dict, Tuple


class ECGSynthesizer:
    """Synthesizes high-fidelity mathematical 12-lead ECG waveforms."""

    @staticmethod
    def generate_lead_ii_signal(
        heart_rate_bpm: int = 75,
        duration_seconds: float = 5.0,
        sampling_rate_hz: int = 250,
        noise_amplitude: float = 0.02,
    ) -> List[Dict[str, float]]:
        """
        Generates simulated Lead II millivolt potential signal over time.
        """
        total_samples = int(duration_seconds * sampling_rate_hz)
        rr_interval_sec = 60.0 / heart_rate_bpm
        samples_per_beat = int(rr_interval_sec * sampling_rate_hz)

        signal = []

        for i in range(total_samples):
            t = i / sampling_rate_hz
            t_beat = (i % samples_per_beat) / sampling_rate_hz

            # Baseline voltage
            v = 0.0

            # P Wave (Atrial Depolarization)
            p_center = 0.15 * rr_interval_sec
            p_width = 0.04
            p_amp = 0.15
            v += p_amp * math.exp(-((t_beat - p_center) ** 2) / (2 * p_width ** 2))

            # Q Wave (Septal Depolarization)
            q_center = 0.22 * rr_interval_sec
            q_width = 0.015
            q_amp = -0.15
            v += q_amp * math.exp(-((t_beat - q_center) ** 2) / (2 * q_width ** 2))

            # R Wave (Ventricular Depolarization Spike)
            r_center = 0.25 * rr_interval_sec
            r_width = 0.02
            r_amp = 1.20
            v += r_amp * math.exp(-((t_beat - r_center) ** 2) / (2 * r_width ** 2))

            # S Wave
            s_center = 0.28 * rr_interval_sec
            s_width = 0.02
            s_amp = -0.25
            v += s_amp * math.exp(-((t_beat - s_center) ** 2) / (2 * s_width ** 2))

            # T Wave (Ventricular Repolarization)
            t_center = 0.45 * rr_interval_sec
            t_width = 0.07
            t_amp = 0.30
            v += t_amp * math.exp(-((t_beat - t_center) ** 2) / (2 * t_width ** 2))

            signal.append({
                "time_sec": round(t, 4),
                "voltage_mv": round(v, 4),
            })

        return signal
