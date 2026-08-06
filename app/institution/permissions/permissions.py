from __future__ import annotations

from enum import Enum


class Permission(str, Enum):
    """
    Institution permission catalogue.
    """

    # ---------------------------------------------------------
    # Institution
    # ---------------------------------------------------------

    INSTITUTION_VIEW = "institution:view"
    INSTITUTION_CREATE = "institution:create"
    INSTITUTION_UPDATE = "institution:update"
    INSTITUTION_DELETE = "institution:delete"

    # ---------------------------------------------------------
    # Branches
    # ---------------------------------------------------------

    BRANCH_VIEW = "branch:view"
    BRANCH_CREATE = "branch:create"
    BRANCH_UPDATE = "branch:update"
    BRANCH_DELETE = "branch:delete"

    # ---------------------------------------------------------
    # Membership
    # ---------------------------------------------------------

    MEMBER_VIEW = "member:view"
    MEMBER_INVITE = "member:invite"
    MEMBER_REMOVE = "member:remove"

    # ---------------------------------------------------------
    # Products
    # ---------------------------------------------------------

    PRODUCT_VIEW = "product:view"
    PRODUCT_CREATE = "product:create"
    PRODUCT_UPDATE = "product:update"
    PRODUCT_DELETE = "product:delete"

    # ---------------------------------------------------------
    # Subscription
    # ---------------------------------------------------------

    SUBSCRIPTION_VIEW = "subscription:view"
    SUBSCRIPTION_MANAGE = "subscription:manage"

    # ---------------------------------------------------------
    # Verification
    # ---------------------------------------------------------

    VERIFY_DOCUMENT = "verification:document"
    VERIFY_LICENSE = "verification:license"
    VERIFY_KYC = "verification:kyc"

    # ---------------------------------------------------------
    # Administration
    # ---------------------------------------------------------

    ADMIN = "institution:admin"