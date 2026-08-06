class PassportOwnershipService:
    """
    Ownership transfer workflows.
    """

    def transfer(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "workflow": "ownership_transfer",
        }