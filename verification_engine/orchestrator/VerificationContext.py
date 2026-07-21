"""
Verification Context

Shared state that travels through the
verification pipeline.

Every pipeline stage reads and updates
this object.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List
from datetime import datetime


@dataclass
class VerificationContext:

    property_id: str

    property_data: Dict[str, Any] = field(
        default_factory=dict
    )

    documents: List[Any] = field(
        default_factory=list
    )

    evidence: List[Dict[str, Any]] = field(
        default_factory=list
    )

    stages: Dict[str, Any] = field(
        default_factory=dict
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    government_result: Dict[str, Any] = field(
        default_factory=dict
    )

    trust_score: float = 0.0

    certificate: Dict[str, Any] = field(
        default_factory=dict
    )

    current_stage: str = ""

    completed_stages: List[str] = field(
        default_factory=list
    )

    pipeline_version: str = ""

    pipeline_name: str = ""

    started_at: datetime | None = None

    completed_at: datetime | None = None

    duration_seconds: float = 0.0