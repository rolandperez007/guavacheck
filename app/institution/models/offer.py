from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import OfferStatus


class Offer(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Promotional offer attached to a Product.
    """

    __tablename__ = "institution_offers"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    product_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institution_products.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    discount_percentage: Mapped[float | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    valid_from: Mapped[datetime] = mapped_column(
        DateTime,
    )

    valid_until: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    status: Mapped[OfferStatus] = mapped_column(
        Enum(OfferStatus),
        default=OfferStatus.DRAFT,
    )

    institution = relationship("Institution")

    product = relationship(
        "Product",
        back_populates="offers",
    )
