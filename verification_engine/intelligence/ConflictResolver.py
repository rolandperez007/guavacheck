"""
Conflict Resolver

Detects and resolves conflicting evidence
produced during the verification process.
"""


class ConflictResolver:
    """
    Identifies evidence conflicts and
    recommends a resolution.
    """

    def __init__(self):

        self.priority = [
            "government_registry",
            "court_records",
            "survey",
            "geospatial",
            "documents",
            "user_submission",
        ]

    def resolve(
        self,
        evidence: dict,
    ) -> dict:

        conflicts = self.detect(evidence)

        return {
            "has_conflicts": len(conflicts) > 0,
            "conflicts": conflicts,
            "recommended_source": self.recommend(conflicts),
        }

    def detect(
        self,
        evidence: dict,
    ) -> list[dict]:

        conflicts = []

        ownership = evidence.get("ownership", [])

        if len(set(ownership)) > 1:
            conflicts.append(
                {
                    "field": "ownership",
                    "values": ownership,
                    "severity": "HIGH",
                }
            )

        coordinates = evidence.get("coordinates", [])

        if len(set(coordinates)) > 1:
            conflicts.append(
                {
                    "field": "coordinates",
                    "values": coordinates,
                    "severity": "HIGH",
                }
            )

        title_numbers = evidence.get("title_numbers", [])

        if len(set(title_numbers)) > 1:
            conflicts.append(
                {
                    "field": "title_number",
                    "values": title_numbers,
                    "severity": "CRITICAL",
                }
            )

        return conflicts

    def recommend(
        self,
        conflicts: list[dict],
    ) -> str:

        if not conflicts:
            return "NO_CONFLICT"

        return self.priority[0]

    def has_critical(
        self,
        conflicts: list[dict],
    ) -> bool:

        return any(item["severity"] == "CRITICAL" for item in conflicts)

    def summary(
        self,
        conflicts: list[dict],
    ) -> str:

        if not conflicts:
            return "No conflicting evidence detected."

        return f"{len(conflicts)} conflict(s) require manual review."
