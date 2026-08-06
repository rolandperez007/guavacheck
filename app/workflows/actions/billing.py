from .base import BaseWorkflowAction


class BillingAction(BaseWorkflowAction):

    name = "billing.invoice"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }