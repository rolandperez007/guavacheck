from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Webhook(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Webhook endpoint registered by an Institution.

    Webhooks allow guavacheck to notify an institution about
    platform events such as product activity, subscriptions,
    verification changes, and other integration events.
    """

    __tablename__ = "institution_webhooks"

    # ==========================================================
    # Ownership
    # ==========================================================

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================================================
    # Webhook Configuration
    # ==========================================================

    event: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    endpoint: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    secret: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    # ==========================================================
    # Relationships
    # ==========================================================

    institution: Mapped["Institution"] = relationship(
        "Institution",
        back_populates="webhooks",
    )

    # ==========================================================
    # Representation
    # ==========================================================

    def __repr__(self) -> str:
        return (
            f"<Webhook("
            f"id={self.id}, "
            f"institution={self.institution_id}, "
            f"event='{self.event}', "
            f"active={self.active}"
            f")>"
        )

