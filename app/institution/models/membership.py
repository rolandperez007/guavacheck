from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import (
    InvitationStatus,
    MembershipRole,
)


class Membership(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Represents a user's membership within an Institution.

    A user may belong to multiple institutions and
    may have different roles in each one.
    """

    __tablename__ = "institution_memberships"

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    branch_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institution_branches.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Role
    # ---------------------------------------------------------

    role: Mapped[MembershipRole] = mapped_column(
        Enum(MembershipRole),
        nullable=False,
        default=MembershipRole.STAFF,
    )

    job_title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    department: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # ---------------------------------------------------------
    # Invitation
    # ---------------------------------------------------------

    invitation_status: Mapped[InvitationStatus] = mapped_column(
        Enum(InvitationStatus),
        default=InvitationStatus.PENDING,
        nullable=False,
    )

    invited_by: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True,
    )

    invited_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    accepted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Access
    # ---------------------------------------------------------

    is_primary_contact: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="members",
    )

    branch = relationship(
        "Branch",
        back_populates="members",
    )

    user = relationship(
        "User",
        foreign_keys=[user_id],
    )

    inviter = relationship(
        "User",
        foreign_keys=[invited_by],
    )

    def __repr__(self) -> str:
        return (
            f"<Membership("
            f"institution={self.institution_id}, "
            f"user={self.user_id}, "
            f"role={self.role.value}"
            f")>"
        )
