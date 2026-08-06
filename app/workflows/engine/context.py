from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class WorkflowContext:
    """
    Shared execution context.
    """

    execution_id: UUID

    workflow_id: UUID

    started_at: datetime

    actor_id: UUID | None = None

    institution_id: UUID | None = None

    correlation_id: UUID | None = None