from app.workflows.repositories import TaskRepository


class TaskService:
    """
    Task management service.
    """

    def __init__(
        self,
        repository: TaskRepository,
    ):
        self.repository = repository

    def enabled(self):
        return self.repository.enabled()

    def register(
        self,
        task,
    ):
        self.repository.add(task)
        self.repository.commit()
        return task