from .base import BaseWorkflowValidator


class TriggerValidator(BaseWorkflowValidator):

    name = "trigger"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []