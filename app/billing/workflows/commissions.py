class CommissionWorkflowService:
    """
    Commission calculation workflows.
    """

    def calculate(
        self,
        transaction_id,
    ):
        return {
            "transaction_id": transaction_id,
            "commission": "calculated",
        }