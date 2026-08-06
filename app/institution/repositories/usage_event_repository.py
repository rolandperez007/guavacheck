from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.usage_event import UsageEvent
from app.institution.repositories.base_repository import BaseRepository


class UsageEventRepository(
    BaseRepository[UsageEvent]
):
    """
    Repository for immutable usage events.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def list_by_product(
        self,
        product_id: str,
    ) -> list[UsageEvent]:
        return (
            self.db.query(UsageEvent)
            .filter(
                UsageEvent.product_id == product_id
            )
            .all()
        )

    def list_by_institution(
        self,
        institution_id: str,
    ) -> list[UsageEvent]:
        return (
            self.db.query(UsageEvent)
            .filter(
                UsageEvent.institution_id == institution_id
            )
            .all()
        )