from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Integration(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    External system integration belonging to an Institution.
    """

    __tablename__ = "institution_integrations"

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
    # Integration
    # ---------------------------------------------------------

    provider: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    integration_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    configuration: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="integrations",
    )