from typing import Any

from pydantic import BaseModel


class SimulationParameter(BaseModel):
    """
    Configurable simulation parameter.
    """

    name: str

    value: Any

    unit: str | None = None

    description: str | None = None