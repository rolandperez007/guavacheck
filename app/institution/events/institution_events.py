from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class InstitutionEvent:
    """
    Base institution domain event.
    """

    institution_id: UUID

    occurred_at: datetime


@dataclass(slots=True)
class InstitutionCreated(InstitutionEvent):
    pass


@dataclass(slots=True)
class InstitutionVerified(InstitutionEvent):
    pass


@dataclass(slots=True)
class BranchCreated(InstitutionEvent):
    branch_id: UUID


@dataclass(slots=True)
class MemberInvited(InstitutionEvent):
    member_id: UUID


@dataclass(slots=True)
class ProductPublished(InstitutionEvent):
    product_id: UUID


@dataclass(slots=True)
class SubscriptionActivated(InstitutionEvent):
    subscription_id: UUID