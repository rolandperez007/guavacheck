"""
Austin Knowledge Entities

Every object Austin understands is an Entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Entity:
    id: str

    entity_type: str

    name: str

    description: str = ""

    aliases: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)


class EntityRegistry:
    def __init__(self):

        self._entities: dict[str, Entity] = {}

    def register(self, entity: Entity):

        self._entities[entity.id] = entity

    def get(self, entity_id: str):

        return self._entities.get(entity_id)

    def all(self):

        return list(self._entities.values())

    def count(self):

        return len(self._entities)


registry = EntityRegistry()
