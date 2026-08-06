from __future__ import annotations

from datetime import datetime
from uuid import uuid4

try:
    from sqlalchemy import DateTime, Float, String  # type: ignore
    from sqlalchemy.orm import Mapped, mapped_column  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    String = Float = DateTime = str  # type: ignore[assignment]
    Mapped = object  # type: ignore[assignment]

    def mapped_column(*args, **kwargs):  # type: ignore[no-untyped-def]
        return None


from database.base import Base


class PropertyRecord(Base):
    __tablename__ = "properties"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    title: Mapped[str] = mapped_column(String)

    address: Mapped[str] = mapped_column(String)

    country: Mapped[str] = mapped_column(String)

    latitude: Mapped[float] = mapped_column(Float)

    longitude: Mapped[float] = mapped_column(Float)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
