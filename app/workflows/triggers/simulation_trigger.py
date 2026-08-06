from .base import BaseWorkflowTrigger


class SimulationTrigger(BaseWorkflowTrigger):

    name = "simulation"

    def should_fire(
        self,
        event,
    ) -> bool:
        return True

    def fire(
        self,
        context,
    ):
        return context