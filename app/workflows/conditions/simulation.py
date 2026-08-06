from .base import BaseCondition


class SimulationCondition(BaseCondition):

    name = "simulation"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True