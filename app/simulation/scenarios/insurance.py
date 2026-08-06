from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class InsuranceScenario(BaseScenario):

    name = "Insurance Risk"

    category = "insurance"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="insurance",
            scenario=self.name,
        )