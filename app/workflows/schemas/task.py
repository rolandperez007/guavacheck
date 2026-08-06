from pydantic import BaseModel


class WorkflowTask(BaseModel):
    """
    Individual workflow task.
    """

    name: str

    action: str

    required: bool = True