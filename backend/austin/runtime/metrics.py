"""
Austin Runtime Metrics
"""

from time import perf_counter


class Stopwatch:
    def __init__(self):

        self.started = perf_counter()

    def elapsed_ms(self):

        return round(
            (perf_counter() - self.started) * 1000,
            2,
        )
