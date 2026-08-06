from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class EventHistory:
    """
    Published workflow events.
    """

    event_name: str

    execution_id: str

    timestamp: datetime

    payload: dict