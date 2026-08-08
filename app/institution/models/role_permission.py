from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin


class RolePermission(
    TimestampMixin,
    Base,
):
    """
    Permissions granted to Roles.
    """

    __tablename__ = "institution_role_permissions"

    role_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_roles.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    permission_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_permissions.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )