from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.subscription_usage import (
    SubscriptionUsage,
)
from app.institution.repositories.base_repository import (
    BaseRepository,
)


class SubscriptionUsageRepository(
    BaseRepository[SubscriptionUsage]
):
    """
    Repository for Subscription Usage.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def list_by_subscription(
        self,
        subscription_id: str,
    ) -> list[SubscriptionUsage]:
        return (
            self.db.query(SubscriptionUsage)
            .filter(
                SubscriptionUsage.subscription_id
                == subscription_id
            )
            .all()
        )