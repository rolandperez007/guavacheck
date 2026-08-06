from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class SubscriptionUsage(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Tracks consumption of a subscription.
    """

    __tablename__ = "institution_subscription_usage"

    subscription_id: Mapped[str] = mapped_column(
        ForeignKey("subscriptions.id"),
        nullable=False,
    )

    metric: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    subscription = relationship("Subscription")