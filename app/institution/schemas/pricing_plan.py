from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class PricingPlanCreate(BaseModel):

    product_id: str

    name: str

    billing_interval: str

    currency: str

    price: float

    trial_days: int = 0


class PricingPlanResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    name: str

    price: float

    currency: str