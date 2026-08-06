from .base import BaseWorkflowAction


class VisionAction(BaseWorkflowAction):

    name = "vision.analyze"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }