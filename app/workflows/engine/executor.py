class WorkflowExecutor:
    """
    Executes workflow nodes sequentially.

    Later versions will support:

    • parallel execution
    • retries
    • compensation
    • distributed workers
    """

    def execute(
        self,
        workflow,
    ):
        return workflow.run()