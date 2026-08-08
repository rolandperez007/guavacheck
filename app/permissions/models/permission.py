from datetime import datetime
from uuid import uuid4

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Permission(Base):

    __tablename__ = "permissions"


    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )


    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )


    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )