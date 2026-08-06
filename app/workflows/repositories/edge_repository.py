from app.workflows.models import WorkflowEdgeModel

from .base import BaseRepository


class EdgeRepository(BaseRepository):
    """
    Repository for workflow edges.
    """

    model = WorkflowEdgeModel

    def by_workflow(
        self,
        workflow_id,
    ):
        return (
            self.session.query(self.model)
            .filter_by(workflow_id=workflow_id)
            .all()
        )