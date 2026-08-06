from app.workflows.registry import WorkflowRegistry


def initialize() -> WorkflowRegistry:
    """
    Bootstrap the workflow platform.
    """
    return WorkflowRegistry()