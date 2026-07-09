from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255)
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
