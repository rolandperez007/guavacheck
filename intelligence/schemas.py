from pydantic import BaseModel, Field
from typing import Any

class IntelligenceEvent(BaseModel):
    event_name: str = Field(..., min_length=1)

    session_id: str | None = None
    user_id: str | None = None

    page: str | None = None

    category: str | None = None

    source: str | None = None

    metadata: dict[str, Any] = {}