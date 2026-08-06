from app.workflows.models import WorkflowApprovalModel

from .base import BaseRepository


class ApprovalRepository(BaseRepository):
    """
    Repository for workflow approvals.
    """

    model = WorkflowApprovalModel

    def pending(self):
        return (
            self.session.query(self.model)
            .filter_by(approved=False)
            .all()
        )