from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Team(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Team within an Institution.

    Teams provide an operational grouping layer for institution
    members and can represent departments, business units, project
    teams, regional teams, or other internal groups.
    """

    __tablename__ = "institution_teams"

    institution_id: Mapped[str] = mapped_column(
        String(UUID_LENGTH),
        ForeignKey(
            "institutions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    code: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    institution = relationship(
        "Institution",
        back_populates="teams",
    )

    members = relationship(
        "TeamMember",
        back_populates="team",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Team("
            f"id={self.id}, "
            f"institution={self.institution_id}, "
            f"name='{self.name}'"
            f")>"
        )
