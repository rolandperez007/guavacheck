class DashboardMetrics:
    """
    Dashboard-ready metrics.
    """

    def __init__(self):

        self.cards = {}

    def add(
        self,
        title: str,
        value,
    ):

        self.cards[title] = value

    def export(self):

        return self.cards