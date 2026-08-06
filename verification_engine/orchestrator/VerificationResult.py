"""
Verification Result

Final output returned by the
Verification Engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class VerificationResult:
    verified: bool

    decision: str

    confidence: float

    evidence: dict[str, Any] = field(default_factory=dict)

    explanation: dict[str, Any] = field(default_factory=dict)
