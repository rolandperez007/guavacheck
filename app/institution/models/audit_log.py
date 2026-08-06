from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class AuditLog(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "institution_audit_logs"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    actor_id = mapped_column(
        PG_UUID(as_uuid=True),
        nullable=True,
    )

    action = mapped_column(
        String(255),
        nullable=False,
    )

    resource = mapped_column(
        String(255),
        nullable=False,
    )

    details = mapped_column(
        Text,
        nullable=True,
    )

    ip_address = mapped_column(
        String(64),
        nullable=True,
    )

    institution = relationship("Institution")
