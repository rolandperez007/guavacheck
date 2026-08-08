from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class SubscriptionUsage(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Tracks consumption of a subscription.
    """

    __tablename__ = "institution_subscription_usage"

    # ---------------------------------------------------------
    # Ownership
    # ---------------------------------------------------------

    subscription_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_subscriptions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Usage Metric
    # ---------------------------------------------------------

    metric: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    subscription = relationship(
        "Subscription",
        back_populates="usage_records",
    )
