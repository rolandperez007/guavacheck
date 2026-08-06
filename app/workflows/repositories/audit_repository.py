from app.workflows.models import WorkflowAudit

from .base import BaseRepository


class AuditRepository(BaseRepository):
    """
    Repository for workflow audit events.
    """

    model = WorkflowAudit

    def recent(
        self,
        limit: int = 100,
    ):
        return (
            self.session.query(self.model)
            .order_by(self.model.created_at.desc())
            .limit(limit)
            .all()
        )