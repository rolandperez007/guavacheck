from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ApprovalHistory:
    """
    Records approval decisions.
    """

    execution_id: str

    approver: str

    decision: str

    comments: str | None = None

    approved_at: datetime | None = None