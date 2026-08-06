from pydantic import BaseModel


class SimulationComparison(BaseModel):
    """
    Comparison between two scenarios.
    """

    baseline: str

    candidate: str

    summary: str