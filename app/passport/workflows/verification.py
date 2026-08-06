class PassportVerificationService:
    """
    Property verification workflows.
    """

    def start(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "verification",
        }