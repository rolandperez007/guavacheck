from collections import defaultdict
from datetime import datetime


class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)
        self.events = []

    def emit(self, event_type: str, payload: dict):
        event = {
            "event_type": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat(),
        }

        self.events.append(event)

        for callback in self.listeners[event_type]:
            callback(event)

        return event

    def on(self, event_type: str, callback):
        self.listeners[event_type].append(callback)

    def get_events(self):
        return self.events
