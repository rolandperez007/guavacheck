from pydantic import BaseModel


class SimulationAssumption(BaseModel):
    """
    Assumptions applied during simulation.
    """

    title: str

    value: str

    source: str | None = None