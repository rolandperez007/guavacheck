from app.workflows.engine.runtime import WorkflowRuntime


class RuntimeService:
    """
    High-level interface to the workflow runtime.
    """

    def __init__(
        self,
        runtime: WorkflowRuntime,
    ):
        self.runtime = runtime

    def execute(
        self,
        workflow_name: str,
    ):
        return self.runtime.pipeline.execute(
            workflow_name,
        )

    def register(
        self,
        name: str,
        workflow,
    ):
        self.runtime.registry.register(
            name,
            workflow,
        )