from __future__ import annotations

from typing import Any
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class SimulationRequest(BaseModel):
    """
    Root request passed to every simulation engine.
    """

    engine: str

    scenario: str

    institution_id: UUID | None = None

    property_id: UUID | None = None

    user_id: UUID | None = None

    parameters: dict[str, Any] = Field(
        default_factory=dict,
    )

    assumptions: list[str] = Field(
        default_factory=list,
    )