from __future__ import annotations

import uuid
from datetime import datetime

from database.base import Base
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    title_number: Mapped[str] = mapped_column(String(120), unique=True)

    owner_name: Mapped[str] = mapped_column(String(255))

    address: Mapped[str] = mapped_column(String(500))

    latitude: Mapped[float] = mapped_column(Float)

    longitude: Mapped[float] = mapped_column(Float)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    verifications = relationship(
        "Verification", back_populates="property", cascade="all, delete-orphan"
    )

    documents = relationship(
        "Document", back_populates="property", cascade="all, delete-orphan"
    )

    ownerships = relationship(
        "Ownership", back_populates="property", cascade="all, delete-orphan"
    )
