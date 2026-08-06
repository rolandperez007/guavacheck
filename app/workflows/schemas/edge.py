from pydantic import BaseModel


class WorkflowEdge(BaseModel):
    """
    Connects two workflow nodes.
    """

    source: str

    target: str