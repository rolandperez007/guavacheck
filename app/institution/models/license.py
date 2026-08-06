from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class License(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Regulatory or professional license.
    """

    __tablename__ = "institution_licenses"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    authority: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
    )

    issued_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    institution = relationship("Institution")
