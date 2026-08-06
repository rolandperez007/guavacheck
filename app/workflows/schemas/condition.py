from typing import Any

from pydantic import BaseModel
from pydantic import Field


class WorkflowCondition(BaseModel):
    """
    Conditional workflow branch.
    """

    expression: str

    parameters: dict[str, Any] = Field(
        default_factory=dict,
    )