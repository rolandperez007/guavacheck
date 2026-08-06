from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class UsageEventCreate(BaseModel):

    institution_id: str

    product_id: str

    event_type: str

    actor_id: str | None = None

    metadata: dict | None = None


class UsageEventResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    event_type: str

    product_id: str