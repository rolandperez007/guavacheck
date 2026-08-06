from app.workflows.repositories import AuditRepository


class AuditService:
    """
    Workflow audit service.
    """

    def __init__(
        self,
        repository: AuditRepository,
    ):
        self.repository = repository

    def log(
        self,
        event,
    ):
        self.repository.add(event)
        self.repository.commit()

    def recent(
        self,
        limit: int = 100,
    ):
        return self.repository.recent(limit)