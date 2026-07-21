"""
Verification Result

Final output returned by the
Verification Engine.
"""

from dataclasses import dataclass
from dataclasses import field

from typing import Any
from typing import Dict


@dataclass
class VerificationResult:

    verified: bool

    decision: str

    confidence: float

    evidence: Dict[str, Any] = field(
        default_factory=dict
    )

    explanation: Dict[str, Any] = field(
        default_factory=dict
    )