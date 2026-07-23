"""
Austin Execution State
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ExecutionState:

    execution_id: str

    stage: str

    engine: str

    started_at: datetime

    completed_at: datetime | None = None

    status: str = "running"

    metadata: dict = field(default_factory=dict)