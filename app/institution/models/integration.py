from __future__ import annotations

from uuid import UUID

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class Integration(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "institution_integrations"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    provider = mapped_column(
        String(100),
        nullable=False,
    )

    integration_type = mapped_column(
        String(100),
        nullable=False,
    )

    configuration = mapped_column(
        Text,
        nullable=True,
    )

    enabled = mapped_column(
        Boolean,
        default=True,
    )

    institution = relationship("Institution")
