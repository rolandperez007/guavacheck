from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class AuditLog(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Records security, compliance, and operational events
    associated with an Institution.
    """

    __tablename__ = "institution_audit_logs"

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey("institutions.id"),
        nullable=False,
        index=True,
    )

    actor_id: Mapped[str | None] = mapped_column(
        String(UUID_LENGTH),
        nullable=True,
    )

    action: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    resource: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    details: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
    )

    institution = relationship("Institution")

    def __repr__(self) -> str:
        return (
            f"<AuditLog("
            f"institution={self.institution_id}, "
            f"action='{self.action}', "
            f"resource='{self.resource}'"
            f")>"
        )
