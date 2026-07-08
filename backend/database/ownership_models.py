from __future__ import annotations

from datetime import datetime
from uuid import uuid4

try:
    from sqlalchemy import String, DateTime  # type: ignore
    from sqlalchemy.orm import Mapped, mapped_column  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    String = DateTime = str  # type: ignore[assignment]
    Mapped = object  # type: ignore[assignment]
    def mapped_column(*args, **kwargs):  # type: ignore[no-untyped-def]
        return None

from database.base import Base


class OwnershipRecord(Base):

    __tablename__ = "ownership_records"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    property_id: Mapped[str] = mapped_column(String)

    owner_name: Mapped[str] = mapped_column(String)

    ownership_type: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
