from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
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

    # ---------------------------------------------------------
    # Ownership
    # ---------------------------------------------------------

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # License Identity
    # ---------------------------------------------------------

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
        nullable=False,
    )

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    issued_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="licenses",
    )