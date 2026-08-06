from app.workflows.schemas import WorkflowCondition


class ConditionBuilder:
    """
    Creates workflow conditions.
    """

    def create(
        self,
        expression: str,
        **parameters,
    ):
        return WorkflowCondition(
            expression=expression,
            parameters=parameters,
        )