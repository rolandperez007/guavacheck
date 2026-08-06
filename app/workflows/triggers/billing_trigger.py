from .base import BaseWorkflowTrigger


class BillingTrigger(BaseWorkflowTrigger):

    name = "billing"

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