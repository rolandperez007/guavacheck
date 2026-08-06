from .base import BaseWorkflowValidator


class NodeValidator(BaseWorkflowValidator):

    name = "node"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []