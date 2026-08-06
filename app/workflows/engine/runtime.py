from .dispatcher import WorkflowDispatcher
from .executor import WorkflowExecutor
from .pipeline import WorkflowPipeline
from .registry import WorkflowRegistry


class WorkflowRuntime:
    """
    Enterprise runtime for workflow execution.
    """

    def __init__(self) -> None:

        self.registry = WorkflowRegistry()

        self.dispatcher = WorkflowDispatcher(
            self.registry,
        )

        self.executor = WorkflowExecutor()

        self.pipeline = WorkflowPipeline(
            self.dispatcher,
            self.executor,
        )