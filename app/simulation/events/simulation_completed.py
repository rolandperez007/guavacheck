from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class SimulationCompleted:
    simulation_id: UUID
    execution_id: UUID