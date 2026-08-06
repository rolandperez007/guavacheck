from app.workflows.models import WorkflowExecution

from .base import BaseRepository


class ExecutionRepository(BaseRepository):
    """
    Repository for workflow executions.
    """

    model = WorkflowExecution

    def running(self):
        return (
            self.session.query(self.model)
            .filter_by(status="running")
            .all()
        )