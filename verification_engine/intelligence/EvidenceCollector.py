"""
Evidence Collector

Collects, normalizes and stores evidence
generated throughout the verification pipeline.
"""

from datetime import datetime


class EvidenceCollector:
    """
    Central repository for all verification
    evidence produced by pipeline stages.
    """

    def __init__(self):

        self._evidence: list[dict] = []

    def add(
        self,
        category: str,
        source: str,
        data: dict,
        confidence: float = 1.0,
    ) -> None:

        self._evidence.append(
            {
                "category": category,
                "source": source,
                "data": data,
                "confidence": confidence,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

    def all(self) -> list[dict]:

        return self._evidence

    def by_category(
        self,
        category: str,
    ) -> list[dict]:

        return [item for item in self._evidence if item["category"] == category]

    def by_source(
        self,
        source: str,
    ) -> list[dict]:

        return [item for item in self._evidence if item["source"] == source]

    def summary(self) -> dict:

        categories = {}

        for item in self._evidence:
            category = item["category"]

            categories[category] = categories.get(category, 0) + 1

        return {
            "total_evidence": len(self._evidence),
            "categories": categories,
        }

    def clear(self) -> None:

        self._evidence.clear()
