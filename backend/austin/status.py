"""
Austin Status

Maintains Austin's current operational state.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AustinStatus:
    online: bool = False

    startup_complete: bool = False

    healthy: bool = False

    registered_engines: int = 0

    last_health_check: datetime | None = None

    last_backup: str | None = None

    message: str = "Austin Offline"

    metadata: dict = field(default_factory=dict)


status = AustinStatus()
