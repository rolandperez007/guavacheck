from datetime import datetime

from pydantic import BaseModel


class WorkflowExecution(BaseModel):
    """
    Workflow execution record.
    """

    execution_id: str

    workflow: str

    status: str

    started_at: datetime

    completed_at: datetime | None = None