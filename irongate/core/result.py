from dataclasses import dataclass


@dataclass
class PolicyResult:
    allow: bool
    reason: str | None = None
    score: int = 0
    critical: bool = False
