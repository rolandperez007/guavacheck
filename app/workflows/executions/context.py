from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared runtime context passed
    throughout workflow execution.
    """

    workflow_id: str

    execution_id: str

    variables: dict = field(
        default_factory=dict,
    )

    metadata: dict = field(
        default_factory=dict,
    )

    current_step: str | None = None