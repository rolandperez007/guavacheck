from pydantic import BaseModel


class SimulationScenario(BaseModel):
    """
    Named business scenario.
    """

    name: str

    description: str

    category: str

    version: str = "1.0"