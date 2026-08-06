from .metrics import WorkflowMetrics


class MetricsAggregator:
    """
    Aggregates workflow statistics.
    """

    def aggregate(
        self,
        executions,
    ) -> WorkflowMetrics:

        metrics = WorkflowMetrics()

        metrics.total_workflows = len(
            executions,
        )

        metrics.completed = sum(
            1
            for e in executions
            if getattr(
                e,
                "status",
                "",
            )
            == "completed"
        )

        metrics.failed = sum(
            1
            for e in executions
            if getattr(
                e,
                "status",
                "",
            )
            == "failed"
        )

        if metrics.total_workflows:

            metrics.success_rate = (
                metrics.completed
                / metrics.total_workflows
            ) * 100

        return metrics