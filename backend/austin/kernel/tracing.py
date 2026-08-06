from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SpanContext:
    trace_id: str
    span_id: str
    parent_span_id: str | None = None


class TraceExporter:
    def export(self, span: dict[str, Any]) -> None:
        return None


class OpenTelemetryAdapter:
    def __init__(self, exporter: TraceExporter | None = None) -> None:
        self.exporter = exporter or TraceExporter()

    def start_span(
        self,
        *,
        name: str,
        trace_id: str | None = None,
        parent_span_id: str | None = None,
    ) -> dict[str, Any]:
        return {"name": name, "trace_id": trace_id, "parent_span_id": parent_span_id}

    def end_span(self, span: dict[str, Any]) -> None:
        self.exporter.export(span)
