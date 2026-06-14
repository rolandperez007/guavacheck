from dataclasses import dataclass
from typing import Optional


@dataclass
class PolicyResult:
    allow: bool
    reason: Optional[str] = None
    score: int = 0
    critical: bool = False
