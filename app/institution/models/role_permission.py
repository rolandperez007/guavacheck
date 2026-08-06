from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin


class RolePermission(
    TimestampMixin,
    Base,
):
    """
    Permissions granted to Roles.
    """

    __tablename__ = "institution_role_permissions"

    role_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_roles.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    permission_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_permissions.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
