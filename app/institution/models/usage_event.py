from __future__ import annotations

from sqlalchemy import ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class UsageEvent(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Immutable commercial usage event.
    """

    __tablename__ = "institution_usage_events"

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

    product_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_products.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Event
    # ---------------------------------------------------------

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    actor_id: Mapped[str | None] = mapped_column(
        String(UUID_LENGTH),
        nullable=True,
    )

    event_metadata: Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution: Mapped["Institution"] = relationship(
        "Institution",
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="usage_events",
    )

