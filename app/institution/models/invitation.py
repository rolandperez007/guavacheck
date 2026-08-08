from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Invitation(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Invitation issued to a prospective Institution member.
    """

    __tablename__ = "institution_invitations"

    # ---------------------------------------------------------
    # Ownership
    # ---------------------------------------------------------

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Invitation
    # ---------------------------------------------------------

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    invited_by: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        nullable=False,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="invitations",
    )