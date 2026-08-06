from __future__ import annotations

from datetime import datetime
from uuid import UUID

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

    This is the aggregate root for the Institution Platform.
    """

    __tablename__ = "institutions"

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Branding
    # ------------------------------------------------------------------

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ------------------------------------------------------------------
    # Contact
    # ------------------------------------------------------------------

    email: Mapped[str] = mapped_column(
        String(320),
        nullable=False,
        unique=True,
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
    # Verification
    # ------------------------------------------------------------------

    verification_status: Mapped[VerificationStatus] = mapped_column(
        Enum(VerificationStatus),
        default=VerificationStatus.PENDING,
        nullable=False,
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    status: Mapped[InstitutionStatus] = mapped_column(
        Enum(InstitutionStatus),
        default=InstitutionStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    # ------------------------------------------------------------------
    # Relationships
    # ------------------------------------------------------------------

    branches = relationship(
        "Branch",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    members = relationship(
        "Membership",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    subscriptions = relationship(
        "Subscription",
        back_populates="institution",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Institution("
            f"id={self.id}, "
            f"name='{self.display_name}', "
            f"type='{self.institution_type.value}'"
            f")>"
        )
    # ---------------------------------------------------------
# Organization
# ---------------------------------------------------------

branches = relationship(
    "Branch",
    back_populates="institution",
    cascade="all, delete-orphan",
)

memberships = relationship(
    "Membership",
    back_populates="institution",
    cascade="all, delete-orphan",
)

teams = relationship(
    "Team",
    back_populates="institution",
    cascade="all, delete-orphan",
)

departments = relationship(
    "Department",
    back_populates="institution",
    cascade="all, delete-orphan",
)

roles = relationship(
    "Role",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Commercial
# ---------------------------------------------------------

products = relationship(
    "Product",
    back_populates="institution",
    cascade="all, delete-orphan",
)

services = relationship(
    "Service",
    back_populates="institution",
    cascade="all, delete-orphan",
)

subscriptions = relationship(
    "Subscription",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Trust
# ---------------------------------------------------------

verifications = relationship(
    "InstitutionVerification",
    back_populates="institution",
    cascade="all, delete-orphan",
)

licenses = relationship(
    "License",
    back_populates="institution",
    cascade="all, delete-orphan",
)

kyc_documents = relationship(
    "KYCDocument",
    back_populates="institution",
    cascade="all, delete-orphan",
)

compliance_records = relationship(
    "Compliance",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Integrations
# ---------------------------------------------------------

api_credentials = relationship(
    "APICredential",
    back_populates="institution",
    cascade="all, delete-orphan",
)

integrations = relationship(
    "Integration",
    back_populates="institution",
    cascade="all, delete-orphan",
)

webhooks = relationship(
    "Webhook",
    back_populates="institution",
    cascade="all, delete-orphan",
)

audit_logs = relationship(
    "AuditLog",
    back_populates="institution",
    cascade="all, delete-orphan",
)

invitations = relationship(
    "Invitation",
    back_populates="institution",
    cascade="all, delete-orphan",
)# ---------------------------------------------------------
# Organization
# ---------------------------------------------------------

branches = relationship(
    "Branch",
    back_populates="institution",
    cascade="all, delete-orphan",
)

memberships = relationship(
    "Membership",
    back_populates="institution",
    cascade="all, delete-orphan",
)

teams = relationship(
    "Team",
    back_populates="institution",
    cascade="all, delete-orphan",
)

departments = relationship(
    "Department",
    back_populates="institution",
    cascade="all, delete-orphan",
)

roles = relationship(
    "Role",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Commercial
# ---------------------------------------------------------

products = relationship(
    "Product",
    back_populates="institution",
    cascade="all, delete-orphan",
)

services = relationship(
    "Service",
    back_populates="institution",
    cascade="all, delete-orphan",
)

subscriptions = relationship(
    "Subscription",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Trust
# ---------------------------------------------------------

verifications = relationship(
    "InstitutionVerification",
    back_populates="institution",
    cascade="all, delete-orphan",
)

licenses = relationship(
    "License",
    back_populates="institution",
    cascade="all, delete-orphan",
)

kyc_documents = relationship(
    "KYCDocument",
    back_populates="institution",
    cascade="all, delete-orphan",
)

compliance_records = relationship(
    "Compliance",
    back_populates="institution",
    cascade="all, delete-orphan",
)

# ---------------------------------------------------------
# Integrations
# ---------------------------------------------------------

api_credentials = relationship(
    "APICredential",
    back_populates="institution",
    cascade="all, delete-orphan",
)

integrations = relationship(
    "Integration",
    back_populates="institution",
    cascade="all, delete-orphan",
)

webhooks = relationship(
    "Webhook",
    back_populates="institution",
    cascade="all, delete-orphan",
)

audit_logs = relationship(
    "AuditLog",
    back_populates="institution",
    cascade="all, delete-orphan",
)

invitations = relationship(
    "Invitation",
    back_populates="institution",
    cascade="all, delete-orphan",
)