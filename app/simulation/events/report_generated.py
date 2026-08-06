from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class ReportGenerated:
    simulation_id: UUID
    report_id: UUID