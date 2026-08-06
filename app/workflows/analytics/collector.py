class MetricsCollector:
    """
    Collects runtime execution data.
    """

    def __init__(self):

        self.executions = []

    def collect(
        self,
        execution,
    ):

        self.executions.append(
            execution,
        )

    def all(self):

        return self.executions