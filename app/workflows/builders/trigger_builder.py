from app.workflows.schemas import WorkflowTrigger


class TriggerBuilder:
    """
    Creates workflow triggers.
    """

    def create(
        self,
        event: str,
        source: str,
    ):
        return WorkflowTrigger(
            event=event,
            source=source,
        )