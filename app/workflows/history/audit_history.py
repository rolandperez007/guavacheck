from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class AuditHistory:
    """
    Immutable audit record.
    """

    timestamp: datetime

    actor: str

    action: str

    resource: str

    metadata: dict