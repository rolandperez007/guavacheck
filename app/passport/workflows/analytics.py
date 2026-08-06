class PassportWorkflowAnalytics:
    """
    Analytics for passport workflow execution.
    """

    def summary(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "verification_count": 0,
            "ownership_changes": 0,
            "valuation_runs": 0,
            "active_workflows": 0,
        }