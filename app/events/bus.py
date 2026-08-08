from typing import Callable


class EventBus:

    def __init__(self):

        self.handlers = {}


    def subscribe(
        self,
        event_name: str,
        handler: Callable
    ):

        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(handler)


    def publish(
        self,
        event_name: str,
        payload: dict
    ):

        handlers = self.handlers.get(
            event_name,
            []
        )

        for handler in handlers:

            handler(payload)



event_bus = EventBus()