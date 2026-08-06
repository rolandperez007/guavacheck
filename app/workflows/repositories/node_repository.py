from app.workflows.models import WorkflowNodeModel

from .base import BaseRepository


class NodeRepository(BaseRepository):
    """
    Repository for workflow nodes.
    """

    model = WorkflowNodeModel

    def by_workflow(
        self,
        workflow_id,
    ):
        return (
            self.session.query(self.model)
            .filter_by(workflow_id=workflow_id)
            .all()
        )