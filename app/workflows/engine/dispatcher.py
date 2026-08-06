from .registry import WorkflowRegistry


class WorkflowDispatcher:
    """
    Resolves workflow definitions.
    """

    def __init__(
        self,
        registry: WorkflowRegistry,
    ) -> None:
        self.registry = registry

    def dispatch(
        self,
        workflow_name: str,
    ):
        return self.registry.resolve(
            workflow_name,
        )