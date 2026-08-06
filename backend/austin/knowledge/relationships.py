"""
Relationships between entities.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Relationship:
    source: str

    relation: str

    target: str


class RelationshipRegistry:
    def __init__(self):

        self._relationships: list[Relationship] = []

    def add(self, relationship: Relationship):

        self._relationships.append(relationship)

    def all(self):

        return self._relationships

    def outgoing(self, entity_id: str):

        return [r for r in self._relationships if r.source == entity_id]


relationships = RelationshipRegistry()
