from .registry import EventRegistry


class EventBus:
    """
    Central event bus.
    """

    def __init__(self):

        self.registry = EventRegistry()

    def publish(
        self,
        event,
    ):

        for subscriber in self.registry.subscribers(
            event.name,
        ):
            subscriber(event)

    def subscribe(
        self,
        event_name: str,
        handler,
    ):

        self.registry.register(
            event_name,
            handler,
        )