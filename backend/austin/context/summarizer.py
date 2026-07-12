"""
Austin Context Summarizer
"""

from __future__ import annotations


class ContextSummarizer:

    def summarize(
        self,
        history: list[dict],
    ) -> str:

        if not history:
            return ""

        recent = history[-5:]

        return "\n".join(
            f"{item['role']}: {item['message']}"
            for item in recent
        )


summarizer = ContextSummarizer()