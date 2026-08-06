from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.pricing_plan import PricingPlan
from app.institution.repositories.pricing_plan_repository import (
    PricingPlanRepository,
)
from app.institution.services.base_service import BaseService


class PricingPlanService(BaseService):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

        self.plans = PricingPlanRepository(db)

    def create(
        self,
        plan: PricingPlan,
    ) -> PricingPlan:

        self.plans.add(plan)

        self.commit()

        self.db.refresh(plan)

        return plan

    def get(
        self,
        plan_id: str,
    ) -> PricingPlan | None:
        return self.plans.get(plan_id)

    def list_by_product(
        self,
        product_id: str,
    ) -> list[PricingPlan]:
        return self.plans.list_by_product(
            product_id,
        )