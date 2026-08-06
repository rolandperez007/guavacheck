from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class SubscriptionUsageCreate(BaseModel):

    subscription_id: str

    metric: str

    quantity: int


class SubscriptionUsageResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    subscription_id: str

    metric: str

    quantity: int