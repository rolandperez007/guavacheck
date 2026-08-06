from __future__ import annotations

from datetime import datetime
from uuid import uuid4

try:
    from sqlalchemy import DateTime, Float, String  # type: ignore
    from sqlalchemy.orm import Mapped, mapped_column  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    String = DateTime = Float = str  # type: ignore[assignment]
    Mapped = object  # type: ignore[assignment]

    def mapped_column(*args, **kwargs):  # type: ignore[no-untyped-def]
        return None


from database.base import Base


class VerificationRecord(Base):
    __tablename__ = "verification_records"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    property_id: Mapped[str] = mapped_column(String)

    trust_score: Mapped[float] = mapped_column(Float)

    fraud_score: Mapped[float] = mapped_column(Float)

    verification_status: Mapped[str] = mapped_column(String)

    risk_level: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
