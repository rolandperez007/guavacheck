from __future__ import annotations

from uuid import UUID

from app.institution.services.base_service import BaseService


class SubscriptionService(BaseService):
    """Service for institution subscription lifecycle operations."""

    def __init__(self, db=None):
        self.db = db
        if db is not None:
            super().__init__(db)

    def current(self, institution_id: UUID):
        return {
            "institution_id": str(institution_id),
            "tier": "free",
            "plan_name": "Starter",
            "active": True,
            "auto_renew": True,
            "starts_at": None,
            "expires_at": None,
            "renews_at": None,
        }

    def renew(self, institution_id: UUID):
        return {
            "institution_id": str(institution_id),
            "status": "renewed",
        }

    def cancel(self, institution_id: UUID):
        return {
            "institution_id": str(institution_id),
            "status": "cancelled",
        }
