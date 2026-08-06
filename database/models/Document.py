from __future__ import annotations

import uuid
from datetime import datetime

from database.base import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )

    property_id: Mapped[str] = mapped_column(ForeignKey("properties.id"))

    document_type: Mapped[str] = mapped_column(String(100))

    file_name: Mapped[str] = mapped_column(String(255))

    storage_path: Mapped[str] = mapped_column(String(500))

    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    property = relationship("Property", back_populates="documents")
