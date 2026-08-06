"""
Austin Execution Pipeline
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..context import context_builder
from .stages import PipelineStage


@dataclass(slots=True)
class PipelineResult:
    stage: PipelineStage

    context: Any


class AustinPipeline:
    def execute(
        self,
        session_id: str,
    ) -> PipelineResult:

        context = context_builder.build(session_id)

        return PipelineResult(
            stage=PipelineStage.BUILD_CONTEXT,
            context=context,
        )


pipeline = AustinPipeline()
