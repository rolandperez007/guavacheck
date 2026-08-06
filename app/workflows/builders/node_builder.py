from app.workflows.schemas import WorkflowNode


class NodeBuilder:
    """
    Builder for workflow nodes.
    """

    def create(
        self,
        name: str,
        node_type: str,
    ):
        return WorkflowNode(
            id=name.lower().replace(" ", "_"),
            name=name,
            type=node_type,
        )