from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Compliance(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Compliance assessment and monitoring record
    associated with an Institution.
    """

    __tablename__ = "institution_compliance"

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey("institutions.id"),
        nullable=False,
        index=True,
    )

    framework: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending",
        nullable=False,
    )

    score: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    findings: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    last_reviewed: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    next_review: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    compliant: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    institution = relationship("Institution")

    def __repr__(self) -> str:
        return (
            f"<Compliance("
            f"institution={self.institution_id}, "
            f"framework='{self.framework}', "
            f"status='{self.status}'"
            f")>"
        )
