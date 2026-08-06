class RetryPolicy:
    """
    Retry configuration.
    """

    def __init__(
        self,
        attempts: int = 3,
    ):

        self.attempts = attempts

    def should_retry(
        self,
        retries: int,
    ) -> bool:

        return retries < self.attempts