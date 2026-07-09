"""
Verification Context

Carries data throughout the verification pipeline.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class VerificationContext:

    property_id: str

    property_data: dict = field(default_factory=dict)

    documents: list = field(default_factory=list)

    evidence: list = field(default_factory=list)

    verification_data: dict = field(default_factory=dict)

    trust_score: int = 0

    certificate: dict | None = None

    metadata: dict[str, Any] = field(default_factory=dict)