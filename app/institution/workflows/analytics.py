class InstitutionWorkflowAnalytics:
    """
    Institution workflow reporting.
    """

    def dashboard(
        self,
        institution_id,
    ):
        return {
            "institution_id": institution_id,
            "active": 0,
            "completed": 0,
            "failed": 0,
        }