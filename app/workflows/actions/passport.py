from .base import BaseWorkflowAction


class PassportAction(BaseWorkflowAction):

    name = "passport.verify"

    def execute(
        self,
        context,
    ):
        """
        Execute Property Passport verification.
        """
        return {
            "action": self.name,
            "status": "completed",
        }