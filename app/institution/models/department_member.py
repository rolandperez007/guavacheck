from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin


class DepartmentMember(
    TimestampMixin,
    Base,
):
    """
    Users belonging to Departments.
    """

    __tablename__ = "institution_department_members"

    department_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_departments.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    membership_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institution_memberships.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )