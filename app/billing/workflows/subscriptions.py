class SubscriptionWorkflowService:
    """
    Subscription lifecycle workflows.
    """

    def activate(
        self,
        subscription_id,
    ):
        return {
            "subscription_id": subscription_id,
            "status": "active",
        }