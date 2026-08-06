from .base import BaseWorkflowAction


class AnalyticsAction(BaseWorkflowAction):

    name = "analytics.generate"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }