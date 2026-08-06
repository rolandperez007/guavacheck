class PassportFinancingService:
    """
    Financing and mortgage workflows.
    """

    def request(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "financing",
        }