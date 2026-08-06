from typing import Any

from pydantic import BaseModel


class AustinExecuteRequest(BaseModel):
    input: str
    context: dict[str, Any] | None = {}
