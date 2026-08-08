from datetime import datetime
from uuid import uuid4

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Token(Base):

    __tablename__ = "auth_tokens"


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )


    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        nullable=False
    )


    token: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )


    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )