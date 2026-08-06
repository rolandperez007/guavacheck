from .bus import EventBus


class EventSubscriber:
    """
    Registers event handlers.
    """

    def __init__(
        self,
        bus: EventBus,
    ):
        self.bus = bus

    def subscribe(
        self,
        event_name: str,
        handler,
    ):

        self.bus.subscribe(
            event_name,
            handler,
        )