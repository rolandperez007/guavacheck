from .base import BaseWorkflowTrigger


class InstitutionTrigger(BaseWorkflowTrigger):

    name = "institution"

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