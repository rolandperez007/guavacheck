from __future__ import annotations

import uuid
from datetime import datetime

from database.base import Base
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Verification(Base):
    __tablename__ = "verifications"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    property_id: Mapped[str] = mapped_column(ForeignKey("properties.id"))

    trust_score: Mapped[int] = mapped_column(Integer, default=0)

    status: Mapped[str] = mapped_column(String(40), default="PENDING")

    certificate_id: Mapped[str] = mapped_column(String(100), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    property = relationship("Property", back_populates="verifications")
