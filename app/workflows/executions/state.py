from enum import Enum


class ExecutionState(
    str,
    Enum,
):
    CREATED = "created"

    RUNNING = "running"

    WAITING = "waiting"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"

    COMPENSATING = "compensating"

    TIMED_OUT = "timed_out"