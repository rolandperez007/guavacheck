from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin


class UsageEvent(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Immutable commercial usage event.
    """

    __tablename__ = "institution_usage_events"

    institution_id: Mapped[str] = mapped_column(
        ForeignKey("institutions.id"),
        nullable=False,
    )

    product_id: Mapped[str] = mapped_column(
        ForeignKey("institution_products.id"),
        nullable=False,
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    actor_id: Mapped[str | None] = mapped_column(
        String(36),
    )

    event_metadata: Mapped[dict | None] = mapped_column(
        "metadata",
        JSON,
    )

    institution: Mapped["Institution"] = relationship(
        "Institution",
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="usage_events",
    )