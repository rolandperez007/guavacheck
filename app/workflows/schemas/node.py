from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field


class WorkflowNode(BaseModel):
    """
    Single workflow node.
    """

    id: str

    name: str

    type: str

    configuration: dict[str, Any] = Field(
        default_factory=dict,
    )