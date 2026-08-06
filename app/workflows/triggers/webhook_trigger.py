from .base import BaseWorkflowTrigger


class WebhookTrigger(BaseWorkflowTrigger):

    name = "webhook"

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