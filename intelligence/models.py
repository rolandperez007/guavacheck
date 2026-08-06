from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    event_name: str

    session_id: str | None

    user_id: str | None

    page: str | None

    category: str | None

    source: str | None

    metadata: dict

    created_at: datetime
