from typing import Any

from pydantic import BaseModel
from pydantic import Field


class SimulationOptimization(BaseModel):
    """
    Optimization recommendations.
    """

    objective: str

    improvements: dict[str, Any] = Field(
        default_factory=dict,
    )

    expected_gain: float | None = None