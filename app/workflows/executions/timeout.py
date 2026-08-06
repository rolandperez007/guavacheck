from datetime import timedelta


class TimeoutPolicy:
    """
    Execution timeout.
    """

    def __init__(
        self,
        seconds: int = 300,
    ):

        self.timeout = timedelta(
            seconds=seconds,
        )