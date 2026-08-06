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


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    action: Mapped[str] = mapped_column(String)

    actor: Mapped[str] = mapped_column(String)

    target: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
