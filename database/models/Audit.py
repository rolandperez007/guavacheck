from __future__ import annotations

import uuid
from datetime import datetime

from database.base import Base
from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Audit(Base):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    actor: Mapped[str] = mapped_column(String(255))

    action: Mapped[str] = mapped_column(String(255))

    resource: Mapped[str] = mapped_column(String(255))

    details: Mapped[str] = mapped_column(Text, default="")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
