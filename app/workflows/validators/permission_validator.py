from .base import BaseWorkflowValidator


class PermissionValidator(BaseWorkflowValidator):

    name = "permission"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []