class EscrowWorkflowService:
    """
    Escrow management workflows.
    """

    def open(
        self,
        transaction_id,
    ):
        return {
            "transaction_id": transaction_id,
            "escrow": "opened",
        }