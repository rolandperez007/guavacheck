from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import VerificationStatus


class InstitutionVerification(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Verification lifecycle for an Institution.

    Every verification event is stored as its own
    record, providing a complete audit history.
    """

    __tablename__ = "institution_verifications"

    # ---------------------------------------------------------
    # Ownership
    # ---------------------------------------------------------

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ---------------------------------------------------------
    # Verification
    # ---------------------------------------------------------

    verification_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[VerificationStatus] = mapped_column(
        Enum(VerificationStatus),
        default=VerificationStatus.PENDING,
        nullable=False,
    )

    confidence_score: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    risk_score: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    # ---------------------------------------------------------
    # Documents
    # ---------------------------------------------------------

    submitted_document: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    supporting_documents: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Review
    # ---------------------------------------------------------

    reviewer_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        nullable=True,
    )

    review_notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Expiry
    # ---------------------------------------------------------

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
    )

    def __repr__(self) -> str:
        return (
            f"<InstitutionVerification("
            f"institution={self.institution_id}, "
            f"type='{self.verification_type}', "
            f"status='{self.status.value}'"
            f")>"
        )
