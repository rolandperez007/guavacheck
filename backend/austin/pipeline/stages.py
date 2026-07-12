"""
Austin Pipeline Stages

Each stage represents one step in Austin's
request execution lifecycle.
"""

from __future__ import annotations

from enum import Enum


class PipelineStage(str, Enum):

    RECEIVE = "receive"

    LOAD_MEMORY = "load_memory"

    BUILD_SUMMARY = "build_summary"

    BUILD_WORLD = "build_world"

    BUILD_CONTEXT = "build_context"

    PLAN = "plan"

    SELECT_ENGINE = "select_engine"

    EXECUTE = "execute"

    LOCALIZE = "localize"

    RESPOND = "respond"