from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import SubscriptionTier


class Subscription(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Commercial subscription assigned to an Institution.

    Payment processing is handled by the Billing module.
    """

    __tablename__ = "institution_subscriptions"

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Plan
    # ---------------------------------------------------------

    tier: Mapped[SubscriptionTier] = mapped_column(
        Enum(SubscriptionTier),
        nullable=False,
        default=SubscriptionTier.FREE,
    )

    plan_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Billing
    # ---------------------------------------------------------

    billing_provider: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    external_subscription_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    # ---------------------------------------------------------
    # Limits
    # ---------------------------------------------------------

    max_members: Mapped[int] = mapped_column(
        Integer,
        default=5,
        nullable=False,
    )

    max_branches: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    max_api_calls_per_month: Mapped[int] = mapped_column(
        Integer,
        default=10000,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    starts_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    renews_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    auto_renew: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="subscriptions",
    )

    def __repr__(self) -> str:
        return (
            f"<Subscription("
            f"institution={self.institution_id}, "
            f"tier={self.tier.value}, "
            f"active={self.active}"
            f")>"
        )
