"""
Austin Executor

Future home of parallel execution.
"""

from __future__ import annotations


class Executor:
    def execute(
        self,
        func,
        *args,
        **kwargs,
    ):

        return func(*args, **kwargs)


executor = Executor()
