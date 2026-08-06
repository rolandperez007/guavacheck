class PassportValuationService:
    """
    Property valuation workflows.
    """

    def run(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "valuation",
        }