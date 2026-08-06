from app.simulation.schemas import SimulationRequest

from .base import BaseScenario


class ClimateScenario(BaseScenario):

    name = "Climate Impact"

    category = "climate"

    def build(self) -> SimulationRequest:

        return SimulationRequest(
            engine="climate",
            scenario=self.name,
        )