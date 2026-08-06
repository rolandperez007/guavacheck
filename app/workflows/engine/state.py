from enum import Enum


class WorkflowState(str, Enum):

    CREATED = "created"

    READY = "ready"

    RUNNING = "running"

    WAITING = "waiting"

    APPROVAL = "approval"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"