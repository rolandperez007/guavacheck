from .base import BaseWorkflowTrigger


class APITrigger(BaseWorkflowTrigger):

    name = "api"

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