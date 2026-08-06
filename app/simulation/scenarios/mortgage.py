from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class MortgageScenario(BaseScenario):

    name = "Mortgage Portfolio"

    category = "mortgage"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="mortgage",
            scenario=self.name,
        )