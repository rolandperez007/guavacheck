from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class WorkflowStage:
    name: str
    status: str


class BusinessMonitor:
    def __init__(self) -> None:
        self._workflows: dict[str, list[WorkflowStage]] = {
            "payment": [
                WorkflowStage("Started", "ok"),
                WorkflowStage("Confirmed", "ok"),
                WorkflowStage("Recorded", "ok"),
                WorkflowStage("Receipt Sent", "ok"),
                WorkflowStage("Access Granted", "ok"),
            ],
            "verification": [
                WorkflowStage("Requested", "ok"),
                WorkflowStage("Documents Uploaded", "ok"),
                WorkflowStage("AI Completed", "ok"),
                WorkflowStage("Trust Score Generated", "ok"),
                WorkflowStage("Report Delivered", "ok"),
            ],
        }

    def snapshot(self) -> dict[str, Any]:
        return {
            "workflows": {
                name: [stage.__dict__ for stage in stages]
                for name, stages in self._workflows.items()
            },
            "failed_workflows": [
                name
                for name, stages in self._workflows.items()
                if any(stage.status == "failed" for stage in stages)
            ],
        }


monitor = BusinessMonitor()
