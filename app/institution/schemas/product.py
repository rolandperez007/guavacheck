from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class ProductCreate(BaseModel):
    institution_id: str

    name: str

    slug: str

    category: str

    description: str | None = None

    visibility: str = "private"

    featured: bool = False


class ProductUpdate(BaseModel):
    name: str | None = None

    category: str | None = None

    description: str | None = None

    visibility: str | None = None

    featured: bool | None = None

    status: str | None = None


class ProductResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    institution_id: str

    name: str

    slug: str

    category: str

    description: str | None

    visibility: str

    featured: bool

    status: str