from dataclasses import dataclass


@dataclass(slots=True)
class WorkflowMetrics:

    executions: int = 0

    completed: int = 0

    failed: int = 0

    running: int = 0

    average_runtime_ms: float = 0.0