from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class APIScope(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "institution_api_scopes"

    credential_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_api_credentials.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    scope = mapped_column(
        String(150),
        nullable=False,
    )

    description = mapped_column(
        String(500),
        nullable=True,
    )

    credential = relationship("APICredential")
