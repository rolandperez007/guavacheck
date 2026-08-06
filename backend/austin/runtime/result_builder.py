"""
Austin Result Builder
"""

from __future__ import annotations


class ResultBuilder:
    def build(
        self,
        *,
        engine,
        result,
    ):

        return {
            "engine": engine,
            "message": result.get(
                "message",
                "",
            ),
            "data": result,
            "status": "success",
        }


result_builder = ResultBuilder()
