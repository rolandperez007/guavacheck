class ExecutionSerializer:
    """
    Converts execution state
    to serializable dictionaries.
    """

    @staticmethod
    def serialize(
        context,
    ):

        return {
            "workflow_id": context.workflow_id,
            "execution_id": context.execution_id,
            "current_step": context.current_step,
            "variables": context.variables,
            "metadata": context.metadata,
        }