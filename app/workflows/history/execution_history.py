from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ExecutionHistory:
    """
    Permanent record of a workflow execution.
    """

    execution_id: str

    workflow_id: str

    started_at: datetime

    completed_at: datetime | None = None

    status: str = "running"

    duration_ms: int = 0

    initiated_by: str | None = None