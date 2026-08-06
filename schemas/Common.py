from datetime import datetime

from pydantic import BaseModel


class APIResponse(BaseModel):
    success: bool = True

    message: str


class TimestampMixin(BaseModel):
    created_at: datetime | None = None

    updated_at: datetime | None = None


class Pagination(BaseModel):
    page: int = 1

    page_size: int = 20
