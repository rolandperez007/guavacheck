from datetime import datetime

from .models import Event

class EventCollector:

    async def collect(self, payload):

        return Event(
            event_name=payload.event_name,
            session_id=payload.session_id,
            user_id=payload.user_id,
            page=payload.page,
            category=payload.category,
            source=payload.source,
            metadata=payload.metadata,
            created_at=datetime.utcnow(),
        )

collector = EventCollector()