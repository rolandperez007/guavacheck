from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.usage_event import UsageEvent
from app.institution.repositories.usage_event_repository import (
    UsageEventRepository,
)
from app.institution.services.base_service import BaseService


class UsageEventService(BaseService):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

        self.events = UsageEventRepository(db)

    def record(
        self,
        event: UsageEvent,
    ) -> UsageEvent:

        self.events.add(event)

        self.commit()

        self.db.refresh(event)

        return event

    def by_product(
        self,
        product_id: str,
    ) -> list[UsageEvent]:

        return self.events.list_by_product(
            product_id,
        )

    def by_institution(
        self,
        institution_id: str,
    ) -> list[UsageEvent]:

        return self.events.list_by_institution(
            institution_id,
        )