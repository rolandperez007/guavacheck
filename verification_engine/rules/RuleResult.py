"""
Result of a single verification rule.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class RuleResult:

    name: str

    passed: bool

    score: int

    reason: str

    evidence: Any = None
