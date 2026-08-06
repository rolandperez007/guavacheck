class CompensationManager:
    """
    Executes rollback actions.
    """

    def compensate(
        self,
        context,
    ):

        return {
            "status": "compensated",
            "execution": context.execution_id,
        }