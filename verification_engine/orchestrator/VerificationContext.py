"""
Verification Context

Shared state that travels through the
verification pipeline.

Every pipeline stage reads and updates
this object.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class VerificationContext:
    property_id: str

    property_data: dict[str, Any] = field(default_factory=dict)

    documents: list[Any] = field(default_factory=list)

    evidence: list[dict[str, Any]] = field(default_factory=list)

    stages: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    government_result: dict[str, Any] = field(default_factory=dict)

    trust_score: float = 0.0

    certificate: dict[str, Any] = field(default_factory=dict)

    current_stage: str = ""

    completed_stages: list[str] = field(default_factory=list)

    pipeline_version: str = ""

    pipeline_name: str = ""

    started_at: datetime | None = None

    completed_at: datetime | None = None

    duration_seconds: float = 0.0
