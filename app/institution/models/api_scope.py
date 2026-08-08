from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class APIScope(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Individual permission scope assigned to an API credential.
    """

    __tablename__ = "institution_api_scopes"

    credential_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_api_credentials.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    scope: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    credential = relationship(
        "ApiCredential",
        back_populates="scopes",
    )
