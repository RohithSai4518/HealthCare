"""
HealthSphere Security and Access Control Module
Provides cryptographic password hashing, session/token management, and Role-Based Access Control (RBAC).
"""

import hashlib
import hmac
import os
import secrets
import time
from typing import Dict, List, Optional, Set
from core.enums import UserRole
from core.exceptions import AuthenticationError, AuthorizationError


class PasswordHasher:
    """Standard-library PBKDF2-HMAC-SHA256 password hashing with salt generation."""

    ITERATIONS = 120_000

    @classmethod
    def hash_password(cls, password: str) -> str:
        salt = os.urandom(16).hex()
        derived_key = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            cls.ITERATIONS,
        ).hex()
        return f"{salt}${cls.ITERATIONS}${derived_key}"

    @classmethod
    def verify_password(cls, password: str, hashed_value: str) -> bool:
        try:
            parts = hashed_value.split("$")
            if len(parts) != 3:
                return False
            salt, iterations_str, expected_key = parts
            iterations = int(iterations_str)
            computed_key = hashlib.pbkdf2_hmac(
                "sha256",
                password.encode("utf-8"),
                salt.encode("utf-8"),
                iterations,
            ).hex()
            return hmac.compare_digest(computed_key, expected_key)
        except Exception:
            return False


class UserContext:
    """Security context representing the currently authenticated user."""

    def __init__(
        self,
        user_id: str,
        username: str,
        role: UserRole,
        session_id: str,
        permissions: Optional[Set[str]] = None,
    ):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.session_id = session_id
        self.permissions = permissions or set()

    def has_permission(self, permission: str) -> bool:
        if self.role == UserRole.ADMIN:
            return True
        return permission in self.permissions


class RBACManager:
    """Role-Based Access Control matrix definition and verification."""

    _ROLE_PERMISSIONS: Dict[UserRole, Set[str]] = {
        UserRole.ADMIN: {
            "patient:read", "patient:write", "patient:delete",
            "clinical:read", "clinical:write", "clinical:delete",
            "appointment:read", "appointment:write", "appointment:cancel",
            "pharmacy:read", "pharmacy:write", "pharmacy:dispense",
            "lab:read", "lab:write", "lab:verify",
            "billing:read", "billing:write", "billing:adjudicate",
            "audit:read", "system:admin",
        },
        UserRole.DOCTOR: {
            "patient:read", "patient:write",
            "clinical:read", "clinical:write",
            "appointment:read", "appointment:write", "appointment:cancel",
            "pharmacy:read", "pharmacy:prescribe",
            "lab:read", "lab:order",
            "billing:read",
        },
        UserRole.NURSE: {
            "patient:read", "patient:write",
            "clinical:read", "clinical:vitals",
            "appointment:read", "appointment:write",
            "pharmacy:read",
            "lab:read", "lab:collect_sample",
        },
        UserRole.PHARMACIST: {
            "patient:read",
            "pharmacy:read", "pharmacy:write", "pharmacy:dispense",
            "billing:read",
        },
        UserRole.LAB_TECHNICIAN: {
            "patient:read",
            "lab:read", "lab:write", "lab:process", "lab:verify",
        },
        UserRole.BILLING_OFFICER: {
            "patient:read",
            "billing:read", "billing:write", "billing:adjudicate",
        },
        UserRole.RECEPTIONIST: {
            "patient:read", "patient:write",
            "appointment:read", "appointment:write", "appointment:cancel",
            "billing:read", "billing:payment",
        },
        UserRole.PATIENT: {
            "patient:read_self",
            "clinical:read_self",
            "appointment:read_self", "appointment:book_self", "appointment:cancel_self",
            "billing:read_self",
        },
    }

    @classmethod
    def get_permissions(cls, role: UserRole) -> Set[str]:
        return cls._ROLE_PERMISSIONS.get(role, set()).copy()

    @classmethod
    def check_permission(cls, context: Optional[UserContext], required_permission: str) -> None:
        if context is None:
            raise AuthenticationError("Unauthenticated request. Security context is missing.")
        if not context.has_permission(required_permission):
            raise AuthorizationError(
                f"User '{context.username}' with role '{context.role.value}' lacks required permission: '{required_permission}'"
            )


class SessionManager:
    """In-memory session token generator with cryptographic integrity verification."""

    def __init__(self, secret_key: Optional[str] = None, session_ttl_seconds: int = 86400):
        self._secret_key = (secret_key or secrets.token_hex(32)).encode("utf-8")
        self._ttl = session_ttl_seconds
        self._active_sessions: Dict[str, dict] = {}

    def create_session(self, user_id: str, username: str, role: UserRole) -> str:
        session_id = secrets.token_hex(24)
        expires_at = time.time() + self._ttl
        payload = f"{session_id}:{user_id}:{role.value}:{int(expires_at)}"
        signature = hmac.new(self._secret_key, payload.encode("utf-8"), hashlib.sha256).hexdigest()
        token = f"{payload}:{signature}"

        self._active_sessions[session_id] = {
            "user_id": user_id,
            "username": username,
            "role": role,
            "expires_at": expires_at,
            "created_at": time.time(),
        }
        return token

    def validate_token(self, token: str) -> UserContext:
        try:
            parts = token.split(":")
            if len(parts) != 5:
                raise AuthenticationError("Malformed session token format.")
            session_id, user_id, role_str, expires_str, signature = parts

            payload = f"{session_id}:{user_id}:{role_str}:{expires_str}"
            expected_sig = hmac.new(self._secret_key, payload.encode("utf-8"), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(expected_sig, signature):
                raise AuthenticationError("Invalid session token signature.")

            if time.time() > float(expires_str):
                self._active_sessions.pop(session_id, None)
                raise AuthenticationError("Session token has expired.")

            session_record = self._active_sessions.get(session_id)
            if not session_record:
                raise AuthenticationError("Session has been terminated or invalidated.")

            role = UserRole(role_str)
            permissions = RBACManager.get_permissions(role)
            return UserContext(
                user_id=user_id,
                username=session_record["username"],
                role=role,
                session_id=session_id,
                permissions=permissions,
            )
        except AuthenticationError:
            raise
        except Exception as exc:
            raise AuthenticationError(f"Session verification failed: {str(exc)}")

    def revoke_session(self, session_id: str) -> bool:
        return self._active_sessions.pop(session_id, None) is not None
