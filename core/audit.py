"""
HealthSphere Audit Logging & Event Bus Subsystem
Provides immutable, HIPAA-aligned audit trails with cryptographic hash chaining and event dispatching.
"""

import hashlib
import json
import threading
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Callable, Dict, List, Optional
from core.enums import AuditAction


@dataclass(frozen=True)
class AuditEntry:
    """Immutable audit record representing a security or clinical action."""

    entry_id: str
    timestamp: str
    actor_id: str
    actor_role: str
    action: str
    resource_type: str
    resource_id: str
    ip_address: str
    status: str
    details: Dict[str, str] = field(default_factory=dict)
    previous_hash: str = ""
    entry_hash: str = ""

    def calculate_hash(self, prev_hash: str) -> str:
        payload = {
            "entry_id": self.entry_id,
            "timestamp": self.timestamp,
            "actor_id": self.actor_id,
            "actor_role": self.actor_role,
            "action": self.action,
            "resource_type": self.resource_type,
            "resource_id": self.resource_id,
            "ip_address": self.ip_address,
            "status": self.status,
            "details": self.details,
            "previous_hash": prev_hash,
        }
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


class AuditService:
    """HIPAA Audit Trail Manager with tamper-evident cryptographic hash chaining."""

    def __init__(self):
        self._entries: List[AuditEntry] = []
        self._lock = threading.RLock()
        self._last_hash = "GENESIS_BLOCK_00000000000000000000000000000000"

    def log(
        self,
        actor_id: str,
        actor_role: str,
        action: AuditAction,
        resource_type: str,
        resource_id: str,
        status: str = "SUCCESS",
        ip_address: str = "127.0.0.1",
        details: Optional[Dict[str, str]] = None,
    ) -> AuditEntry:
        with self._lock:
            entry_id = f"AUD-{int(time.time()*1000)}-{len(self._entries)+1:06d}"
            now_iso = datetime.now(timezone.utc).isoformat()
            prev_hash = self._last_hash

            raw_entry = AuditEntry(
                entry_id=entry_id,
                timestamp=now_iso,
                actor_id=actor_id,
                actor_role=str(actor_role),
                action=action.value if isinstance(action, AuditAction) else str(action),
                resource_type=resource_type,
                resource_id=resource_id,
                ip_address=ip_address,
                status=status,
                details=details or {},
                previous_hash=prev_hash,
                entry_hash="",
            )

            calculated_hash = raw_entry.calculate_hash(prev_hash)
            final_entry = AuditEntry(
                entry_id=raw_entry.entry_id,
                timestamp=raw_entry.timestamp,
                actor_id=raw_entry.actor_id,
                actor_role=raw_entry.actor_role,
                action=raw_entry.action,
                resource_type=raw_entry.resource_type,
                resource_id=raw_entry.resource_id,
                ip_address=raw_entry.ip_address,
                status=raw_entry.status,
                details=raw_entry.details,
                previous_hash=prev_hash,
                entry_hash=calculated_hash,
            )

            self._entries.append(final_entry)
            self._last_hash = calculated_hash
            return final_entry

    def get_logs(
        self,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        actor_id: Optional[str] = None,
        limit: int = 100,
    ) -> List[AuditEntry]:
        with self._lock:
            results = self._entries
            if resource_type:
                results = [e for e in results if e.resource_type == resource_type]
            if resource_id:
                results = [e for e in results if e.resource_id == resource_id]
            if actor_id:
                results = [e for e in results if e.actor_id == actor_id]
            return results[-limit:]

    def verify_integrity(self) -> bool:
        """Verifies that the audit log chain has not been tampered with or modified."""
        with self._lock:
            current_prev_hash = "GENESIS_BLOCK_00000000000000000000000000000000"
            for entry in self._entries:
                if entry.previous_hash != current_prev_hash:
                    return False
                recomputed = entry.calculate_hash(current_prev_hash)
                if recomputed != entry.entry_hash:
                    return False
                current_prev_hash = entry.entry_hash
            return True


class EventBus:
    """Internal synchronous event dispatcher for cross-module healthcare events."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[dict], None]]] = {}
        self._lock = threading.RLock()

    def subscribe(self, event_name: str, handler: Callable[[dict], None]) -> None:
        with self._lock:
            if event_name not in self._subscribers:
                self._subscribers[event_name] = []
            self._subscribers[event_name].append(handler)

    def publish(self, event_name: str, payload: dict) -> None:
        with self._lock:
            handlers = self._subscribers.get(event_name, []).copy()
        for handler in handlers:
            try:
                handler(payload)
            except Exception:
                # Event dispatch errors should not abort core transaction
                pass


# Global singleton instances for audit and event distribution
audit_service = AuditService()
event_bus = EventBus()
