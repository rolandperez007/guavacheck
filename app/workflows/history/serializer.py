class HistorySerializer:
    """
    Converts history records
    into JSON-ready dictionaries.
    """

    @staticmethod
    def serialize(
        history,
    ):

        return history.__dict__