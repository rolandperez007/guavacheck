class LedgerWorkflowService:
    """
    Financial ledger workflows.
    """

    def record(
        self,
        transaction_id,
    ):
        return {
            "transaction_id": transaction_id,
            "ledger": "recorded",
        }