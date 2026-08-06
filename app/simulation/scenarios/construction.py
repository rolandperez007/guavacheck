from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class ConstructionScenario(BaseScenario):

    name = "Construction Planning"

    category = "construction"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="construction",
            scenario=self.name,
        )