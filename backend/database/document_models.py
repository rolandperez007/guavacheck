from __future__ import annotations

from datetime import datetime
from uuid import uuid4

try:
    from sqlalchemy import DateTime, String  # type: ignore
    from sqlalchemy.orm import Mapped, mapped_column  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    String = DateTime = str  # type: ignore[assignment]
    Mapped = object  # type: ignore[assignment]

    def mapped_column(*args, **kwargs):  # type: ignore[no-untyped-def]
        return None


from database.base import Base


class DocumentRecord(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    property_id: Mapped[str] = mapped_column(String)

    document_type: Mapped[str] = mapped_column(String)

    storage_path: Mapped[str] = mapped_column(String)

    verification_status: Mapped[str] = mapped_column(String)

    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
