from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class PropertyPassport(Base):
    __tablename__ = "property_passports"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    passport_id: Mapped[str] = mapped_column(
        String(32),
        unique=True,
        index=True,
    )
    asset_uid: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )
    property_name: Mapped[str] = mapped_column(
        String(200),
    )

    property_type: Mapped[str] = mapped_column(
        String(100),
    )

    owner_id: Mapped[str] = mapped_column(
        String(36),
    )

    country: Mapped[str] = mapped_column(
        String(100),
    )

    state: Mapped[str] = mapped_column(
        String(100),
    )

    city: Mapped[str] = mapped_column(
        String(100),
    )

    address: Mapped[str] = mapped_column(
        String(500),
    )

    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    construction_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    land_area: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    building_area: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    dna_generated: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    twin_generated: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    published: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
