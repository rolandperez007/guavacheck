from app.workflows.engine import WorkflowEngine


class WorkflowCoordinator:
    """
    Coordinates enterprise workflows.
    """

    def __init__(
        self,
        engine: WorkflowEngine,
    ) -> None:
        self.engine = engine