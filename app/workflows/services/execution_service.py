from app.workflows.repositories import ExecutionRepository


class ExecutionService:
    """
    Handles workflow execution history.
    """

    def __init__(
        self,
        repository: ExecutionRepository,
    ) -> None:
        self.repository = repository

    def running(self):
        return self.repository.running()

    def history(self):
        return self.repository.list()

    def save(
        self,
        execution,
    ):
        self.repository.add(execution)
        self.repository.commit()
        return execution