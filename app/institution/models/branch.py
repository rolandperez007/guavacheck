from __future__ import annotations

from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import BranchStatus


class Branch(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Physical or virtual branch belonging to an Institution.
    """

    __tablename__ = "institution_branches"

    # ------------------------------------------------------------------
    # Relationship
    # ------------------------------------------------------------------

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    code: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        unique=True,
    )

    # ------------------------------------------------------------------
    # Contact
    # ------------------------------------------------------------------

    email: Mapped[str | None] = mapped_column(
        String(320),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    # ------------------------------------------------------------------
    # Address
    # ------------------------------------------------------------------

    country: Mapped[str] = mapped_column(
        String(2),
        nullable=False,
    )

    state: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ------------------------------------------------------------------
    # Branch Status
    # ------------------------------------------------------------------

    status: Mapped[BranchStatus] = mapped_column(
        Enum(BranchStatus),
        default=BranchStatus.ACTIVE,
        nullable=False,
    )

    # ------------------------------------------------------------------
    # Relationships
    # ------------------------------------------------------------------

    institution = relationship(
        "Institution",
        back_populates="branches",
    )

    members = relationship(
        "Membership",
        back_populates="branch",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Branch("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"institution_id={self.institution_id}"
            f")>"
        )
