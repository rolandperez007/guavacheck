"""
Austin Runtime Executor
"""

from __future__ import annotations

import time

from .result_builder import result_builder
from .validator import validator


class RuntimeExecutor:
    def execute(
        self,
        *,
        engine,
        context,
    ):

        start = time.perf_counter()

        if hasattr(engine, "before_execute"):
            engine.before_execute(context)

        raw = engine.execute(context)

        if hasattr(engine, "after_execute"):
            engine.after_execute(raw)

        duration = (time.perf_counter() - start) * 1000

        response = result_builder.build(
            engine=engine.name,
            result=raw,
            duration_ms=duration,
            correlation_id=context.correlation_id,
            trace_id=context.trace_id,
        )

        validator.validate(response)

        return response


executor = RuntimeExecutor()
