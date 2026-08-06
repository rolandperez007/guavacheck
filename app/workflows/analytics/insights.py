class WorkflowInsights:
    """
    AI-ready workflow insights.
    """

    def generate(
        self,
        metrics,
    ):

        insights = []

        if metrics.success_rate < 90:

            insights.append(
                "Workflow success rate is below target."
            )

        if metrics.failed:

            insights.append(
                "Investigate failed workflow executions."
            )

        return insights