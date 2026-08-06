from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin


class KYCDocument(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    KYC or compliance document submitted by an Institution.
    """

    __tablename__ = "institution_kyc_documents"

    institution_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False,
    )

    document_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    file_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    checksum: Mapped[str | None] = mapped_column(
        String(128),
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
    )

    institution = relationship("Institution")
