from __future__ import annotations

import uuid
from datetime import datetime

from database.base import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Ownership(Base):
    __tablename__ = "ownerships"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    property_id: Mapped[str] = mapped_column(ForeignKey("properties.id"))

    owner_name: Mapped[str] = mapped_column(String(255))

    acquisition_method: Mapped[str] = mapped_column(String(100), default="UNKNOWN")

    acquisition_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    property = relationship("Property", back_populates="ownerships")
