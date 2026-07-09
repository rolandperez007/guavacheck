from __future__ import annotations

from typing import Any


class AustinRecommendations:
    def explain(self, *, queue_depth: int, active_workers: int, wait_time_ms: int | None = None) -> dict[str, Any]:
        if queue_depth > 100 and active_workers < 3:
            return {
                "title": "Scale worker capacity",
                "message": "Verification demand increased significantly. Recommend starting one additional worker to prevent queue saturation.",
                "confidence": 0.95,
            }
        if wait_time_ms and wait_time_ms > 1000:
            return {
                "title": "Reduce processing latency",
                "message": "Queue wait time is above target. Austin recommends warming caches and reducing backlog.",
                "confidence": 0.88,
            }
        return {
            "title": "Capacity stable",
            "message": "Queue depth is within a healthy range and no scaling action is required right now.",
            "confidence": 0.82,
        }
