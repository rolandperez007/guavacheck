from .base import BaseWorkflowAction


class NotificationAction(BaseWorkflowAction):

    name = "notification.send"

    def execute(
        self,
        context,
    ):
        return {
            "action": self.name,
            "status": "completed",
        }