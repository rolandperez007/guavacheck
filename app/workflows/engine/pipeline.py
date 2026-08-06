from .dispatcher import WorkflowDispatcher
from .executor import WorkflowExecutor


class WorkflowPipeline:
    """
    Complete workflow execution pipeline.
    """

    def __init__(
        self,
        dispatcher: WorkflowDispatcher,
        executor: WorkflowExecutor,
    ) -> None:
        self.dispatcher = dispatcher
        self.executor = executor

    def execute(
        self,
        workflow_name: str,
    ):
        workflow = self.dispatcher.dispatch(
            workflow_name,
        )

        return self.executor.execute(
            workflow,
        )