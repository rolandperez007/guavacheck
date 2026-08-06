class PassportInsuranceService:
    """
    Insurance-related workflows.
    """

    def quote(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "insurance",
        }