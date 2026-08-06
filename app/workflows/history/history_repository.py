class HistoryRepository:
    """
    Storage abstraction for workflow history.
    """

    def __init__(self):

        self._records = []

    def save(
        self,
        record,
    ):

        self._records.append(record)

    def list(self):

        return self._records

    def by_execution(
        self,
        execution_id: str,
    ):

        return [
            r
            for r in self._records
            if getattr(
                r,
                "execution_id",
                None,
            )
            == execution_id
        ]