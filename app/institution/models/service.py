from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import OfferStatus


class Service(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Professional service provided by an Institution.
    """

    __tablename__ = "institution_services"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    fee: Mapped[float | None] = mapped_column(
        Numeric(18, 2),
        nullable=True,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        default="USD",
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

    def __repr__(self) -> str:
        return f"<Service(id={self.id}, name='{self.name}')>"
