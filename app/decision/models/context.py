from dataclasses import dataclass
from typing import Any


@dataclass
class DecisionContext:
    """
    Complete context supplied to the Decision Engine.

    Every engine contributes information to this object.
    """

    property: Any | None = None

    passport: Any | None = None

    twin: Any | None = None

    vision: Any | None = None

    valuation: Any | None = None

    marketplace: Any | None = None

    mortgage: Any | None = None

    insurance: Any | None = None

    construction: Any | None = None

    investment: Any | None = None

    analytics: Any | None = None

    user: Any | None = None
