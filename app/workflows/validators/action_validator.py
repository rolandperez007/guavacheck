from .base import BaseWorkflowValidator


class ActionValidator(BaseWorkflowValidator):

    name = "action"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []