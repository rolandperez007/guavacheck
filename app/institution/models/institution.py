from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.db.mixins import TimestampMixin
from app.db.mixins import UUIDMixin

from app.institution.enums import (
    InstitutionStatus,
    InstitutionType,
    VerificationStatus,
)


class Institution(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Enterprise organization registered on guavacheck.

    Aggregate Root for the Institution Platform.
    """

    __tablename__ = "institutions"

    # ==========================================================
    # Identity
    # ==========================================================

    legal_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    display_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    institution_type: Mapped[InstitutionType] = mapped_column(
        Enum(InstitutionType),
        nullable=False,
        index=True,
    )

    registration_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    tax_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # ==========================================================
    # Branding
    # ==========================================================

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ==========================================================
    # Contact
    # ==========================================================

    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    # ==========================================================
    # Address
    # ==========================================================

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

    # ==========================================================
    # Verification
    # ==========================================================

    verification_status: Mapped[VerificationStatus] = mapped_column(
        Enum(VerificationStatus),
        default=VerificationStatus.PENDING,
        nullable=False,
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ==========================================================
    # Lifecycle
    # ==========================================================

    status: Mapped[InstitutionStatus] = mapped_column(
        Enum(InstitutionStatus),
        default=InstitutionStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    # ==========================================================
    # Organization
    # ==========================================================

    branches: Mapped[list["Branch"]] = relationship(
        "Branch",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    memberships: Mapped[list["Membership"]] = relationship(
        "Membership",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    teams: Mapped[list["Team"]] = relationship(
        "Team",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    departments: Mapped[list["Department"]] = relationship(
        "Department",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    roles: Mapped[list["Role"]] = relationship(
        "Role",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    invitations: Mapped[list["Invitation"]] = relationship(
        "Invitation",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    # ==========================================================
    # Commercial
    # ==========================================================

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    services: Mapped[list["Service"]] = relationship(
        "Service",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    subscriptions: Mapped[list["Subscription"]] = relationship(
        "Subscription",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    # ==========================================================
    # Trust
    # ==========================================================

    verifications: Mapped[list["InstitutionVerification"]] = relationship(
        "InstitutionVerification",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    licenses: Mapped[list["License"]] = relationship(
        "License",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    kyc_documents: Mapped[list["KYCDocument"]] = relationship(
        "KYCDocument",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    compliance_records: Mapped[list["Compliance"]] = relationship(
        "Compliance",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    audit_logs: Mapped[list["AuditLog"]] = relationship(
        "AuditLog",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    # ==========================================================
    # Integrations
    # ==========================================================

    api_credentials: Mapped[list["APICredential"]] = relationship(
        "APICredential",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    integrations: Mapped[list["Integration"]] = relationship(
        "Integration",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    webhooks: Mapped[list["Webhook"]] = relationship(
        "Webhook",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Institution("
            f"id={self.id}, "
            f"name='{self.display_name}', "
            f"type='{self.institution_type.value}', "
            f"status='{self.status.value}'"
            f")>"
        )