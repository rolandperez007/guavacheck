"""
Austin Worker

The Austin Worker is the runtime coordinator responsible for processing
background jobs from the Austin queue.

Execution Lifecycle

Queued Job
    │
    ▼
Mark Running
    │
    ▼
Resolve Execution Plan
    │
    ▼
Dispatch Engine
    │
    ▼
Execute Engine
    │
    ▼
Validate Response
    │
    ▼
Build Final Result
    │
    ▼
Persist Result
    │
    ▼
Complete Queue Job
"""

from __future__ import annotations

import traceback
import time
from time import perf_counter

from backend.austin.queue import queue

from backend.austin.runtime.dispatcher import dispatcher
from backend.austin.runtime.executor import executor
from backend.austin.runtime.result_builder import result_builder
from backend.austin.runtime.validator import validator


class AustinWorker:
    """
    Austin Runtime Worker.
    """

    POLL_INTERVAL = 0.25

    # ---------------------------------------------------------
    # Main Job Processing
    # ---------------------------------------------------------

    def process(self, job):

        queue.mark_running(job.job_id)

        started = perf_counter()

        print("=" * 70)
        print("AUSTIN EXECUTION")
        print("=" * 70)
        print(f"Job ID        : {job.job_id}")
        print(f"Correlation   : {job.correlation_id}")
        print()

        try:

            context = job.payload.get("context", {})

            execution_plan = context.get("plan")

            #
            # Temporary compatibility until planner is fully integrated.
            #

            if execution_plan is None:

                class DefaultPlan:

                    engine = "conversation"

                execution_plan = DefaultPlan()

            #
            # Dispatch
            #

            dispatch = dispatcher.dispatch(
                execution_plan
            )

            if not dispatch.success:

                raise RuntimeError(
                    dispatch.diagnostics["reason"]
                )

            print(
                f"Requested Engine : {dispatch.requested_engine}"
            )

            print(
                f"Resolved Engine  : {dispatch.resolved_engine}"
            )

            print(
                f"Fallback         : {dispatch.fallback_used}"
            )

            print()

            #
            # Execute Engine
            #

            engine_result = executor.execute(
                dispatch.engine,
                context,
            )

            #
            # Build Response
            #

            response = result_builder.build(
                engine=dispatch.resolved_engine,
                result=engine_result,
            )

            #
            # Validate
            #

            validator.validate(response)

            #
            # Persist
            #

            job.payload["response"] = response

            elapsed = int(
                (perf_counter() - started) * 1000
            )

            queue.complete(
                job.job_id,
                execution_time_ms=elapsed,
            )

            print()
            print("Execution Successful")
            print(f"Duration : {elapsed} ms")
            print("=" * 70)

        except Exception as exc:

            traceback.print_exc()

            queue.fail(
                job.job_id,
                str(exc),
            )

            print()
            print("Execution Failed")
            print(str(exc))
            print("=" * 70)

    # ---------------------------------------------------------
    # Continuous Runtime Loop
    # ---------------------------------------------------------

    def run(self):

        print("=" * 70)
        print("Austin Runtime Worker")
        print("Status : ONLINE")
        print("=" * 70)

        while True:

            job = queue.next()

            if job is None:

                time.sleep(self.POLL_INTERVAL)

                continue

            self.process(job)


worker = AustinWorker()