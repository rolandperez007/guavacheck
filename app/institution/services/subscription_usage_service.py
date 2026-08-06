from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.subscription_usage import (
    SubscriptionUsage,
)
from app.institution.repositories.subscription_usage_repository import (
    SubscriptionUsageRepository,
)
from app.institution.services.base_service import BaseService


class SubscriptionUsageService(BaseService):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

        self.usage = SubscriptionUsageRepository(db)

    def record(
        self,
        usage: SubscriptionUsage,
    ) -> SubscriptionUsage:

        self.usage.add(usage)

        self.commit()

        self.db.refresh(usage)

        return usage

    def list(
        self,
        subscription_id: str,
    ) -> list[SubscriptionUsage]:

        return self.usage.list_by_subscription(
            subscription_id,
        )