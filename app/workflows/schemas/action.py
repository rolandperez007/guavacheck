from typing import Any

from pydantic import BaseModel
from pydantic import Field


class WorkflowAction(BaseModel):
    """
    Executable workflow action.
    """

    name: str

    parameters: dict[str, Any] = Field(
        default_factory=dict,
    )