from .base import BaseWorkflowValidator


class GraphValidator(BaseWorkflowValidator):

    name = "graph"

    def validate(
        self,
        workflow,
    ) -> list[str]:
        """
        Future:
        - Detect cycles
        - Detect orphan nodes
        - Detect unreachable nodes
        """
        return []