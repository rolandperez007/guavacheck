from .base import BaseWorkflowAction


class SimulationAction(BaseWorkflowAction):

    name = "simulation.run"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }