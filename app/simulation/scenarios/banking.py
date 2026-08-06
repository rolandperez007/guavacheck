from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class BankingScenario(BaseScenario):

    name = "Bank Lending"

    category = "banking"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="banking",
            scenario=self.name,
        )