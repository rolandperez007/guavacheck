from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class OfferCreate(BaseModel):

    institution_id: str

    product_id: str

    title: str

    description: str | None = None

    starts_at: datetime | None = None

    ends_at: datetime | None = None


class OfferResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    title: str

    status: str