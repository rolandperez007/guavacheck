from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class InvestmentScenario(BaseScenario):

    name = "Investment Growth"

    category = "investment"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="investment",
            scenario=self.name,
        )