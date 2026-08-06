from .bus import EventBus


class EventPublisher:
    """
    Publishes workflow events.
    """

    def __init__(
        self,
        bus: EventBus,
    ):
        self.bus = bus

    def publish(
        self,
        event,
    ):

        self.bus.publish(event)