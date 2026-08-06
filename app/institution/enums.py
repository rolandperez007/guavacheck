from enum import Enum


class InstitutionType(str, Enum):
    """
    Categories of organizations that can register
    on the guavacheck platform.
    """

    BANK = "bank"

    MORTGAGE_PROVIDER = "mortgage_provider"

    DEVELOPER = "developer"

    REAL_ESTATE_COMPANY = "real_estate_company"

    PROPERTY_MANAGER = "property_manager"

    FACILITY_MANAGER = "facility_manager"

    LAW_FIRM = "law_firm"

    SURVEYOR = "surveyor"

    VALUER = "valuer"

    ARCHITECT = "architect"

    CONTRACTOR = "contractor"

    INSURANCE = "insurance"

    GOVERNMENT = "government"

    NGO = "ngo"

    INVESTOR = "investor"

    OTHER = "other"


class InstitutionStatus(str, Enum):
    """
    Overall operational state of an institution.
    """

    ACTIVE = "active"

    INACTIVE = "inactive"

    SUSPENDED = "suspended"

    ARCHIVED = "archived"


class VerificationStatus(str, Enum):
    """
    Institution verification lifecycle.
    """

    PENDING = "pending"

    SUBMITTED = "submitted"

    UNDER_REVIEW = "under_review"

    VERIFIED = "verified"

    REJECTED = "rejected"

    SUSPENDED = "suspended"


class MembershipRole(str, Enum):
    """
    Roles assigned to institution members.
    """

    OWNER = "owner"

    ADMIN = "admin"

    MANAGER = "manager"

    STAFF = "staff"

    AUDITOR = "auditor"

    COMPLIANCE = "compliance"

    API_CLIENT = "api_client"

    VIEWER = "viewer"


class SubscriptionTier(str, Enum):
    """
    Commercial subscription plans.
    """

    FREE = "free"

    STARTER = "starter"

    PROFESSIONAL = "professional"

    BUSINESS = "business"

    ENTERPRISE = "enterprise"


class BranchStatus(str, Enum):
    """
    Operational status of a branch.
    """

    ACTIVE = "active"

    INACTIVE = "inactive"

    CLOSED = "closed"


class ApiKeyStatus(str, Enum):
    """
    API credential lifecycle.
    """

    ACTIVE = "active"

    REVOKED = "revoked"

    EXPIRED = "expired"


class InvitationStatus(str, Enum):
    """
    Membership invitation workflow.
    """

    PENDING = "pending"

    ACCEPTED = "accepted"

    DECLINED = "declined"

    EXPIRED = "expired"


class OfferStatus(str, Enum):
    """
    Institution product or offer lifecycle.
    """

    DRAFT = "draft"

    ACTIVE = "active"

    PAUSED = "paused"

    EXPIRED = "expired"

    ARCHIVED = "archived"
