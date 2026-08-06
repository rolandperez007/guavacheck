class WorkflowReportGenerator:
    """
    Generates workflow reports.
    """

    def generate(
        self,
        metrics,
    ):

        return {
            "summary": metrics,
            "generated": True,
        }