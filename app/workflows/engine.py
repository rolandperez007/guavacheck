from app.workflows.registry import WorkflowRegistry


class WorkflowEngine:
    """
    Root workflow engine.
    """

    def __init__(self) -> None:
        self.registry = WorkflowRegistry()