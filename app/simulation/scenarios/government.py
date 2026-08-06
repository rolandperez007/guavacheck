from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class GovernmentScenario(BaseScenario):

    name = "Government Policy"

    category = "government"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="government",
            scenario=self.name,
        )