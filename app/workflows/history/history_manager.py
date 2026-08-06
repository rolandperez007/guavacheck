from app.workflows.history.history_repository import (
    HistoryRepository,
)


class HistoryManager:
    """
    Coordinates workflow history.
    """

    def __init__(self):

        self.repository = HistoryRepository()

    def record(
        self,
        history,
    ):

        self.repository.save(history)

    def execution(
        self,
        execution_id: str,
    ):

        return self.repository.by_execution(
            execution_id,
        )

    def all(self):

        return self.repository.list()