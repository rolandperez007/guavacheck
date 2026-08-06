from .base import BaseWorkflowValidator


class ConditionValidator(BaseWorkflowValidator):

    name = "condition"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []