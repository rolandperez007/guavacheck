from dataclasses import dataclass, field


@dataclass
class DecisionReport:

    score: float = 0.0

    confidence: float = 0.0

    recommendations: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    opportunities: list[str] = field(default_factory=list)

    data: dict = field(default_factory=dict)