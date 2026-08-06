from .base import BaseWorkflowTrigger


class EventTrigger(BaseWorkflowTrigger):

    name = "event"

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