from enum import Enum


class SimulationState(str, Enum):
    """
    Runtime state machine.
    """

    CREATED = "created"

    QUEUED = "queued"

    RUNNING = "running"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"