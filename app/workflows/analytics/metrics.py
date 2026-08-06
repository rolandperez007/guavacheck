from dataclasses import dataclass


@dataclass(slots=True)
class WorkflowMetrics:
    """
    Core workflow metrics.
    """

    total_workflows: int = 0

    running: int = 0

    completed: int = 0

    failed: int = 0

    cancelled: int = 0

    average_duration_ms: float = 0.0

    success_rate: float = 0.0

    retry_rate: float = 0.0