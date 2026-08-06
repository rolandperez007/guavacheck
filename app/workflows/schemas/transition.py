from pydantic import BaseModel


class WorkflowTransition(BaseModel):
    """
    State transition.
    """

    from_node: str

    to_node: str

    condition: str | None = None