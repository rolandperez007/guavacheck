from app.workflows.executions.executor import (
    WorkflowExecutor,
)


class ExecutionManager:
    """
    Coordinates workflow execution.
    """

    def __init__(self):

        self.executor = WorkflowExecutor()

    def run(
        self,
        workflow,
        context,
    ):

        return self.executor.execute(
            workflow,
            context,
        )