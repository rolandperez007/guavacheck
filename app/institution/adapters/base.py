from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowExecutionContext:
    """
    Shared workflow execution context passed to module adapters.
    """

    workflow_id: str
    execution_id: str
    variables: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    current_step: str | None = None


@dataclass(slots=True)
class WorkflowResult:
    """
    Standard result returned by workflow adapters.
    """

    status: str
    event: str
    data: dict[str, Any] = field(default_factory=dict)


class BaseWorkflowAdapter:
    """
    Shared contract for module adapters participating in workflow execution.
    """

    @staticmethod
    def build_result(
        event: str,
        *,
        status: str = "completed",
        data: dict[str, Any] | None = None,
    ) -> WorkflowResult:
        return WorkflowResult(
            status=status,
            event=event,
            data=data or {},
        )
