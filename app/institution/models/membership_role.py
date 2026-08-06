from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin


class MembershipRole(
    TimestampMixin,
    Base,
):
    """
    Many-to-many relationship between
    Memberships and Roles.
    """

    __tablename__ = "institution_membership_roles"

    membership_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_memberships.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    role_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_roles.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
