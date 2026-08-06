from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import OfferStatus


class Product(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Product offered by an Institution.

    Examples:

    - Mortgage
    - Home Insurance
    - Land Banking
    - Property Development
    - Investment Fund
    """

    __tablename__ = "institution_products"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        default="USD",
    )

    base_price: Mapped[float | None] = mapped_column(
        Numeric(18, 2),
        nullable=True,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    status: Mapped[OfferStatus] = mapped_column(
        Enum(OfferStatus),
        default=OfferStatus.DRAFT,
    )

    institution = relationship(
        "Institution",
    )

    offers = relationship(
        "Offer",
        back_populates="product",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name='{self.name}')>"
