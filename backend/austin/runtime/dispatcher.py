"""
Austin Runtime Dispatcher

The dispatcher is responsible for resolving an execution plan into one or
more executable Austin engines.

Responsibilities

• Validate execution plans
• Resolve engines from the registry
• Verify engine health
• Apply fallbacks
• Support multi-engine execution
• Provide execution diagnostics
• Remain independent from execution logic

The dispatcher NEVER executes engines.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from backend.austin.registry.registry import registry


# ---------------------------------------------------------------------
# Dispatch Result
# ---------------------------------------------------------------------


@dataclass(slots=True)
class DispatchResult:

    success: bool

    engine_name: str

    engine: Any | None

    fallback_used: bool = False

    diagnostics: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(default_factory=datetime.utcnow)


# ---------------------------------------------------------------------
# Runtime Dispatcher
# ---------------------------------------------------------------------


class RuntimeDispatcher:

    def __init__(self):

        self.default_engine = "conversation"

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    def dispatch(self, execution_plan) -> DispatchResult:
        """
        Resolve an execution plan into a runnable engine.
        """

        self._validate_plan(execution_plan)

        requested_engine = execution_plan.engine

        engine = self._resolve(requested_engine)

        fallback = False

        if engine is None:

            fallback = True

            engine = self._resolve(self.default_engine)

        if engine is None:

            return DispatchResult(

                success=False,

                engine_name=requested_engine,

                engine=None,

                fallback_used=fallback,

                diagnostics={

                    "reason": "No registered execution engine.",

                    "requested_engine": requested_engine,

                },

            )

        diagnostics = {

            "requested_engine": requested_engine,

            "resolved_engine": self.default_engine
            if fallback
            else requested_engine,

            "registry_size": self._registry_size(),

            "fallback": fallback,

        }

        return DispatchResult(

            success=True,

            engine_name=requested_engine,

            engine=engine,

            fallback_used=fallback,

            diagnostics=diagnostics,

        )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _resolve(self, name: str):

        try:

            return registry.get(name)

        except Exception:

            return None

    def _validate_plan(self, plan):

        if plan is None:

            raise RuntimeError(

                "Execution plan cannot be None."

            )

        if not hasattr(plan, "engine"):

            raise RuntimeError(

                "Execution plan is missing an engine."

            )

        if not plan.engine:

            raise RuntimeError(

                "Execution plan specifies an empty engine."

            )

    def _registry_size(self):

        try:

            return len(registry.list())

        except Exception:

            return 0

    # ---------------------------------------------------------
    # Diagnostics
    # ---------------------------------------------------------

    def available_engines(self):

        try:

            return registry.list()

        except Exception:

            return []

    def has_engine(self, name: str):

        return self._resolve(name) is not None

    def health(self):

        return {

            "dispatcher": "healthy",

            "default_engine": self.default_engine,

            "available_engines": len(

                self.available_engines()

            ),

        }


dispatcher = RuntimeDispatcher()