class ReceiptWorkflowService:
    """
    Receipt issuance workflows.
    """

    def issue(
        self,
        payment_id,
    ):
        return {
            "payment_id": payment_id,
            "receipt": "issued",
        }