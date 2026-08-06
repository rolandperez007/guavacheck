class RefundWorkflowService:
    """
    Refund processing workflows.
    """

    def initiate(
        self,
        payment_id,
    ):
        return {
            "payment_id": payment_id,
            "status": "refund_requested",
        }