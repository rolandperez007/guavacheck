from pydantic import BaseModel


class WorkflowTrigger(BaseModel):
    """
    Workflow trigger.
    """

    event: str

    source: str

    enabled: bool = True