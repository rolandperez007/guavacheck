from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin


class DepartmentMember(
    TimestampMixin,
    Base,
):
    """
    Users belonging to Departments.
    """

    __tablename__ = "institution_department_members"

    department_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_departments.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    membership_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_memberships.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
