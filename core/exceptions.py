"""
HealthSphere Domain and Operational Exceptions
Standardized exception hierarchy for application errors, validation, and domain constraints.
"""


class HealthSphereException(Exception):
    """Base exception for all HealthSphere application errors."""

    def __init__(self, message: str, code: str = "INTERNAL_ERROR", details: dict = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    def to_dict(self) -> dict:
        return {
            "error": self.__class__.__name__,
            "code": self.code,
            "message": self.message,
            "details": self.details,
        }


class EntityNotFoundError(HealthSphereException):
    """Raised when a requested domain entity cannot be located."""

    def __init__(self, entity_type: str, entity_id: str):
        message = f"{entity_type} with ID '{entity_id}' not found."
        super().__init__(message, code="NOT_FOUND", details={"entity_type": entity_type, "entity_id": entity_id})


class ValidationError(HealthSphereException):
    """Raised when business validation or domain constraint fails."""

    def __init__(self, message: str, field: str = None):
        details = {"field": field} if field else {}
        super().__init__(message, code="VALIDATION_FAILED", details=details)


class ConflictError(HealthSphereException):
    """Raised when an operation conflicts with current state (e.g. double booking)."""

    def __init__(self, message: str, conflict_type: str = "STATE_CONFLICT"):
        super().__init__(message, code="CONFLICT", details={"conflict_type": conflict_type})


class AuthenticationError(HealthSphereException):
    """Raised when user credentials or tokens are invalid or expired."""

    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message, code="UNAUTHENTICATED")


class AuthorizationError(HealthSphereException):
    """Raised when user lacks permission to execute an action."""

    def __init__(self, message: str = "Access denied for this resource."):
        super().__init__(message, code="FORBIDDEN")


class DrugInteractionError(HealthSphereException):
    """Raised when medication contraindications or severe interactions are detected."""

    def __init__(self, message: str, drugs: list, severity: str):
        super().__init__(
            message,
            code="DRUG_INTERACTION_DETECTED",
            details={"interacting_drugs": drugs, "severity": severity},
        )


class InsufficientStockError(HealthSphereException):
    """Raised when pharmacy inventory has insufficient medication quantity."""

    def __init__(self, medication_id: str, requested: int, available: int):
        super().__init__(
            f"Insufficient stock for medication {medication_id}. Requested: {requested}, Available: {available}",
            code="INSUFFICIENT_STOCK",
            details={"medication_id": medication_id, "requested": requested, "available": available},
        )


class ClaimAdjudicationError(HealthSphereException):
    """Raised when insurance claim processing fails policy rules."""

    def __init__(self, claim_id: str, reason: str):
        super().__init__(
            f"Claim {claim_id} adjudication failed: {reason}",
            code="CLAIM_REJECTED",
            details={"claim_id": claim_id, "reason": reason},
        )
