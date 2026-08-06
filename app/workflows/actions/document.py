from .base import BaseWorkflowAction


class DocumentAction(BaseWorkflowAction):

    name = "document.generate"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }