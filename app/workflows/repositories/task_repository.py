from app.workflows.models import WorkflowTaskModel

from .base import BaseRepository


class TaskRepository(BaseRepository):
    """
    Repository for workflow tasks.
    """

    model = WorkflowTaskModel

    def enabled(self):
        return (
            self.session.query(self.model)
            .filter_by(enabled=True)
            .all()
        )