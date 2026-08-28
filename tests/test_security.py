"""
Unit Tests for HealthSphere Cryptography, Authentication, RBAC, and HIPAA Audit Trails
"""

import unittest
from core.audit import AuditService
from core.enums import AuditAction, UserRole
from core.exceptions import AuthenticationError, AuthorizationError
from core.security import PasswordHasher, RBACManager, SessionManager, UserContext


class TestSecuritySubsystem(unittest.TestCase):

    def test_pbkdf2_password_hashing(self):
        password = "SecureClinicalPassword#2026"
        hashed = PasswordHasher.hash_password(password)

        self.assertTrue(PasswordHasher.verify_password(password, hashed))
        self.assertFalse(PasswordHasher.verify_password("WrongPassword", hashed))

    def test_session_token_lifecycle(self):
        manager = SessionManager(secret_key="TEST_SECRET_KEY")
        token = manager.create_session(user_id="U100", username="dr_smith", role=UserRole.DOCTOR)

        context = manager.validate_token(token)
        self.assertEqual(context.username, "dr_smith")
        self.assertEqual(context.role, UserRole.DOCTOR)
        self.assertTrue(context.has_permission("patient:read"))
        self.assertFalse(context.has_permission("system:admin"))

        # Revocation
        manager.revoke_session(context.session_id)
        with self.assertRaises(AuthenticationError):
            manager.validate_token(token)

    def test_rbac_permission_checking(self):
        nurse_context = UserContext(
            user_id="U101",
            username="nurse_joy",
            role=UserRole.NURSE,
            session_id="S1",
            permissions=RBACManager.get_permissions(UserRole.NURSE),
        )

        # Nurse has vital recording permission
        RBACManager.check_permission(nurse_context, "clinical:vitals")

        # Nurse lacks doctor prescription permission
        with self.assertRaises(AuthorizationError):
            RBACManager.check_permission(nurse_context, "pharmacy:prescribe")

    def test_hipaa_audit_trail_hash_chain_integrity(self):
        audit = AuditService()
        audit.log(
            actor_id="DOC-1",
            actor_role="DOCTOR",
            action=AuditAction.READ,
            resource_type="Patient",
            resource_id="PAT-99",
        )
        audit.log(
            actor_id="DOC-1",
            actor_role="DOCTOR",
            action=AuditAction.UPDATE,
            resource_type="Encounter",
            resource_id="ENC-01",
        )

        self.assertEqual(len(audit.get_logs()), 2)
        self.assertTrue(audit.verify_integrity())


if __name__ == "__main__":
    unittest.main()
