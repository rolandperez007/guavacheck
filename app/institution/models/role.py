from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Role(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Institution-specific role definition.
    """

    __tablename__ = "institution_roles"

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    system_role: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    institution = relationship(
        "Institution",
        back_populates="roles",
    )

    def __repr__(self) -> str:
        return (
            f"<Role("
            f"name='{self.name}', "
            f"institution={self.institution_id}"
            f")>"
        )