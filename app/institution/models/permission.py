from __future__ import annotations

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class Permission(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Global permission definition.

    Permissions are intentionally not owned by an institution.
    They represent reusable capabilities such as:

        institution.read
        institution.manage
        members.invite
        products.create
        offers.approve
    """

    __tablename__ = "institution_permissions"

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    resource: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    action: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"<Permission("
            f"name='{self.name}', "
            f"resource='{self.resource}', "
            f"action='{self.action}'"
            f")>"
        )
