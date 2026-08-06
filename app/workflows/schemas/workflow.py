from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class WorkflowSchema(BaseModel):
    """
    Root workflow definition.
    """

    id: UUID | None = None

    name: str

    description: str | None = None

    version: str = "1.0"

    active: bool = True

    nodes: list["WorkflowNode"] = Field(
        default_factory=list,
    )