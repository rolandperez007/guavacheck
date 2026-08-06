class CheckpointManager:
    """
    Saves execution checkpoints.
    """

    def __init__(self):

        self._points = {}

    def save(
        self,
        execution_id: str,
        state,
    ):

        self._points[
            execution_id
        ] = state

    def restore(
        self,
        execution_id: str,
    ):

        return self._points.get(
            execution_id,
        )