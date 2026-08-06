class EventRegistry:
    """
    Registry of event subscribers.
    """

    def __init__(self):

        self._events: dict[str, list] = {}

    def register(
        self,
        event_name: str,
        handler,
    ):

        self._events.setdefault(
            event_name,
            [],
        ).append(handler)

    def subscribers(
        self,
        event_name: str,
    ):

        return self._events.get(
            event_name,
            [],
        )

    def list(self):

        return sorted(
            self._events.keys(),
        )