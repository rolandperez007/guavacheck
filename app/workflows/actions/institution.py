from .base import BaseWorkflowAction


class InstitutionAction(BaseWorkflowAction):

    name = "institution.validate"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }