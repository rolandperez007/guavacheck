from .base import BaseWorkflowTrigger


class ScheduleTrigger(BaseWorkflowTrigger):

    name = "schedule"

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