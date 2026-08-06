from app.workflows.schemas import WorkflowAction


class ActionBuilder:
    """
    Builder for executable actions.
    """

    def create(
        self,
        name: str,
        **parameters,
    ):
        return WorkflowAction(
            name=name,
            parameters=parameters,
        )