class WorkflowTimeline:
    """
    Chronological workflow timeline.
    """

    def __init__(self):

        self.events = []

    def add(
        self,
        event,
    ):

        self.events.append(event)

    def ordered(self):

        return sorted(
            self.events,
            key=lambda e: e.timestamp,
        )