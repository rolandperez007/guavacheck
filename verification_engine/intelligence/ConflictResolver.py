"""
Conflict Resolver

Detects contradictory evidence.
"""


class ConflictResolver:

    def resolve(

        self,

        evidence: list,

    ) -> dict:

        conflicts = []

        for item in evidence:

            value = item.get("value")

            if isinstance(value, dict):

                if value.get("conflict"):

                    conflicts.append(item)

        return {

            "has_conflicts": len(conflicts) > 0,

            "conflicts": conflicts,

        }
