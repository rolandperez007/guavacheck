from app.workflows.builders.workflow_builder import WorkflowBuilder


class PipelineBuilder:
    """
    High-level builder for complete pipelines.
    """

    def __init__(
        self,
        name: str,
    ):
        self.builder = WorkflowBuilder(name)

    def workflow(self):
        return self.builder

    def build(self):
        return self.builder.build()