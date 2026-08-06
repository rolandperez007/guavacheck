class ExecutionTracker:
    """
    Tracks workflow progress.
    """

    def __init__(self):

        self.steps = []

    def start(
        self,
        step: str,
    ):

        self.steps.append(
            (
                step,
                "started",
            )
        )

    def complete(
        self,
        step: str,
    ):

        self.steps.append(
            (
                step,
                "completed",
            )
        )

    def fail(
        self,
        step: str,
    ):

        self.steps.append(
            (
                step,
                "failed",
            )
        )

    def history(self):

        return self.steps