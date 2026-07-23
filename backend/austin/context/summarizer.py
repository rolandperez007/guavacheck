"""
Austin Context Summarizer
"""

from __future__ import annotations

from backend.austin.memory import MemoryRecord


class ContextSummarizer:

    def summarize(
        self,
        history: list[MemoryRecord],
    ) -> str:

        if not history:
            return ""

        recent = history[-5:]

        lines = []

        for item in recent:

            if isinstance(item, dict):
                title = item.get("title", "message")
                value = item.get("value", "")
            else:
                title = getattr(item, "title", "message")
                value = getattr(item, "value", "")

            lines.append(f"{title}: {value}")

        return "\n".join(lines)


summarizer = ContextSummarizer()