from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.constants import UUID_LENGTH
from app.db.mixins import TimestampMixin


class TeamMember(
    TimestampMixin,
    Base,
):
    """
    Associates an institution membership with a team.
    """

    __tablename__ = "institution_team_members"

    team_id: Mapped[str] = mapped_column(
        ForeignKey(
            "institution_teams.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    membership_id: Mapped[str] = mapped_column(
        ForeignKey(
            "institution_memberships.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    team = relationship(
        "Team",
        back_populates="members",
    )

    membership = relationship(
        "Membership",
        back_populates="teams",
    )
