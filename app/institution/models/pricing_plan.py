from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class PricingPlan(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Pricing plan attached to a product.
    """

    __tablename__ = "institution_pricing_plans"

    product_id: Mapped[str] = mapped_column(
        ForeignKey("institution_products.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    billing_interval: Mapped[str] = mapped_column(
        String(30),
        default="monthly",
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        default="USD",
    )

    price: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    trial_days: Mapped[int] = mapped_column(
        default=0,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="pricing_plans",
    )