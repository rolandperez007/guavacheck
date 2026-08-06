from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.pricing_plan import PricingPlan
from app.institution.repositories.base_repository import BaseRepository


class PricingPlanRepository(
    BaseRepository[PricingPlan]
):
    """
    Repository for Pricing Plans.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def get(
        self,
        plan_id: str,
    ) -> PricingPlan | None:
        return (
            self.db.query(PricingPlan)
            .filter(PricingPlan.id == plan_id)
            .first()
        )

    def list_by_product(
        self,
        product_id: str,
    ) -> list[PricingPlan]:
        return (
            self.db.query(PricingPlan)
            .filter(
                PricingPlan.product_id == product_id
            )
            .all()
        )