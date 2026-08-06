class InvoiceWorkflowService:
    """
    Invoice generation workflows.
    """

    def generate(
        self,
        reference_id,
    ):
        return {
            "reference_id": reference_id,
            "invoice": "generated",
        }