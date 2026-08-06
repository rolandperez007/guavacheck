from .base import BaseWorkflowValidator


class ApprovalValidator(BaseWorkflowValidator):

    name = "approval"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []