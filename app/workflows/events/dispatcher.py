from .publisher import EventPublisher


class EventDispatcher:
    """
    High-level dispatcher.
    """

    def __init__(
        self,
        publisher: EventPublisher,
    ):
        self.publisher = publisher

    def dispatch(
        self,
        event,
    ):
        self.publisher.publish(
            event,
        )