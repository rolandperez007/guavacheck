from app.workflows.engine.runtime import WorkflowRuntime
from app.workflows.repositories import WorkflowRepository


class WorkflowService:
    """
    Primary service for workflow lifecycle management.
    """

    def __init__(
        self,
        repository: WorkflowRepository,
        runtime: WorkflowRuntime,
    ) -> None:
        self.repository = repository
        self.runtime = runtime

    def create(
        self,
        workflow,
    ):
        self.repository.add(workflow)
        self.repository.commit()
        return workflow

    def execute(
        self,
        workflow_name: str,
    ):
        return self.runtime.pipeline.execute(
            workflow_name,
        )

    def list(self):
        return self.repository.list()

    def get(
        self,
        workflow_id,
    ):
        return self.repository.get(
            workflow_id,
        )