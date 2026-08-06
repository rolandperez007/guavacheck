from app.workflows.executions.tracker import (
    ExecutionTracker,
)


class WorkflowExecutor:
    """
    Executes workflow actions.
    """

    def __init__(self):

        self.tracker = ExecutionTracker()

    def execute(
        self,
        workflow,
        context,
    ):

        for action in workflow:

            self.tracker.start(action)

            #
            # Future:
            # Action Registry executes here
            #

            self.tracker.complete(action)

        return self.tracker.history()