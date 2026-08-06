class BillingWorkflowAnalytics:
    """
    Billing workflow metrics.
    """

    def summary(
        self,
    ):
        return {
            "payments": 0,
            "subscriptions": 0,
            "refunds": 0,
            "escrow_transactions": 0,
            "commissions": 0,
            "revenue": 0.0,
        }