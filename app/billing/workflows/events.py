class BillingWorkflowEvents:
    """
    Billing workflow event publisher.
    """

    def payment_created(
        self,
        payment_id,
    ):
        return {
            "event": "billing.payment.created",
            "payment_id": payment_id,
        }

    def payment_completed(
        self,
        payment_id,
    ):
        return {
            "event": "billing.payment.completed",
            "payment_id": payment_id,
        }

    def refund_processed(
        self,
        refund_id,
    ):
        return {
            "event": "billing.refund.processed",
            "refund_id": refund_id,
        }