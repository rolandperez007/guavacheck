from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class Compliance(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "institution_compliance"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    framework = mapped_column(
        String(150),
        nullable=False,
    )

    status = mapped_column(
        String(50),
        default="pending",
    )

    score = mapped_column(
        Integer,
        default=0,
    )

    findings = mapped_column(
        Text,
        nullable=True,
    )

    last_reviewed = mapped_column(
        DateTime,
        nullable=True,
    )

    next_review = mapped_column(
        DateTime,
        nullable=True,
    )

    compliant = mapped_column(
        Boolean,
        default=False,
    )

    institution = relationship("Institution")
