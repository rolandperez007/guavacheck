"""
Austin Response Builder
"""

from __future__ import annotations

from dataclasses import asdict

from backend.austin.models.engine_result import EngineResult


class ResponseBuilder:
    def build(self, result: EngineResult):

        return asdict(result)


response_builder = ResponseBuilder()
