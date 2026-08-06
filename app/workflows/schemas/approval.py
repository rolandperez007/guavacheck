from pydantic import BaseModel


class WorkflowApproval(BaseModel):
    """
    Human approval requirement.
    """

    role: str

    required: bool = True

    timeout_hours: int = 24