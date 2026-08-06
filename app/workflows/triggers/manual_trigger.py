from .base import BaseWorkflowTrigger


class ManualTrigger(BaseWorkflowTrigger):

    name = "manual"

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