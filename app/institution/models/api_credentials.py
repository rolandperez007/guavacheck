from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin, UUIDMixin
from app.institution.enums import ApiKeyStatus


class ApiCredential(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    API credentials issued to an Institution.

    These credentials authenticate external systems
    connecting to guavacheck.
    """

    __tablename__ = "institution_api_credentials"

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
    # Identity
    # ---------------------------------------------------------

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ---------------------------------------------------------
    # Credentials
    # ---------------------------------------------------------

    api_key: Mapped[str] = mapped_column(
        String(128),
        unique=True,
        nullable=False,
        index=True,
    )

    api_secret_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # ---------------------------------------------------------
    # Permissions
    # ---------------------------------------------------------

    scopes: Mapped[str] = mapped_column(
        String(2000),
        default="",
        nullable=False,
    )

    # ---------------------------------------------------------
    # Rate Limiting
    # ---------------------------------------------------------

    requests_per_minute: Mapped[int] = mapped_column(
        Integer,
        default=60,
        nullable=False,
    )

    requests_per_day: Mapped[int] = mapped_column(
        Integer,
        default=10000,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------------

    status: Mapped[ApiKeyStatus] = mapped_column(
        Enum(ApiKeyStatus),
        default=ApiKeyStatus.ACTIVE,
        nullable=False,
    )

    last_used_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ---------------------------------------------------------
    # Security
    # ---------------------------------------------------------

    ip_whitelist: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    allow_sandbox: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # ---------------------------------------------------------
    # Relationships
    # ---------------------------------------------------------

    institution = relationship(
        "Institution",
    )

    def __repr__(self) -> str:
        return (
            f"<ApiCredential("
            f"institution={self.institution_id}, "
            f"name='{self.name}', "
            f"status='{self.status.value}'"
            f")>"
        )
