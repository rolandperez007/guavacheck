from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeMetrics:
    """
    Runtime execution metrics.
    """

    executions: int = 0

    completed: int = 0

    failed: int = 0

    average_runtime_ms: float = 0.0

    cache_hits: int = 0

    cache_misses: int = 0