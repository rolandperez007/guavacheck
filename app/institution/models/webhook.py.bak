from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class Webhook(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "institution_webhooks"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    event = mapped_column(
        String(100),
        nullable=False,
    )

    endpoint = mapped_column(
        String(500),
        nullable=False,
    )

    secret = mapped_column(
        String(255),
        nullable=False,
    )

    active = mapped_column(
        Boolean,
        default=True,
    )

    institution = relationship("Institution")
