class PassportComplianceService:
    """
    Regulatory and compliance workflows.
    """

    def evaluate(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "compliance",
        }