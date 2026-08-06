from typing import Any

from pydantic import BaseModel
from pydantic import Field


class SimulationResult(BaseModel):
    """
    Standard simulation output.
    """

    success: bool

    score: float | None = None

    confidence: float | None = None

    metrics: dict[str, Any] = Field(
        default_factory=dict,
    )

    recommendations: list[str] = Field(
        default_factory=list,
    )