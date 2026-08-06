from .base import BaseWorkflowAction


class IntegrationAction(BaseWorkflowAction):

    name = "integration.call"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }