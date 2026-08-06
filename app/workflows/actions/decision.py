from .base import BaseWorkflowAction


class DecisionAction(BaseWorkflowAction):

    name = "decision.evaluate"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }