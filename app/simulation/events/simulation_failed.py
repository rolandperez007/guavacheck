from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class SimulationFailed:
    simulation_id: UUID
    execution_id: UUID
    reason: str