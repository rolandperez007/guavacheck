from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class WorkflowEvent:
    """
    Base event shared by every module.
    """

    name: str

    payload: dict

    event_id: str = ""

    timestamp: datetime | None = None

    def __post_init__(self):

        if not self.event_id:
            self.event_id = str(uuid4())

        if self.timestamp is None:
            self.timestamp = datetime.utcnow()