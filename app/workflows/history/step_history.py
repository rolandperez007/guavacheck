from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class StepHistory:
    """
    History of an individual workflow step.
    """

    execution_id: str

    step_name: str

    status: str

    started_at: datetime

    completed_at: datetime | None = None

    retries: int = 0