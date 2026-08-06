from app.workflows.models import Workflow

from .base import BaseRepository


class WorkflowRepository(BaseRepository):
    """
    Repository for workflow definitions.
    """

    model = Workflow

    def find_by_name(
        self,
        name: str,
    ):
        return (
            self.session.query(self.model)
            .filter_by(name=name)
            .first()
        )