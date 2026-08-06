from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class SimulationContext:
    """
    Shared execution context passed
    through the simulation runtime.
    """

    execution_id: UUID

    engine: str

    started_at: datetime

    user_id: UUID | None = None

    institution_id: UUID | None = None

    property_id: UUID | None = None