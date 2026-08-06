"""Compatibility model registry for the database package."""

from __future__ import annotations

from .base import Base

try:
    from .audit_models import AuditLog
    from .document_models import DocumentRecord
    from .ownership_models import OwnershipRecord
    from .property_models import PropertyRecord
    from .verification_models import VerificationRecord
except ImportError:  # pragma: no cover - optional dependency
    AuditLog = DocumentRecord = OwnershipRecord = PropertyRecord = (
        VerificationRecord
    ) = None  # type: ignore[assignment]

__all__ = [
    "AuditLog",
    "Base",
    "DocumentRecord",
    "OwnershipRecord",
    "PropertyRecord",
    "VerificationRecord",
]
