"""
Knowledge Index

Initial knowledge loaded at startup.
"""

from .entities import Entity, registry
from .relationships import Relationship, relationships


def build_index():

    registry.register(
        Entity(
            id="guavacheck",
            entity_type="platform",
            name="GuavaCheck",
            aliases=["guava ai"],
            description="Global AI Property Intelligence Platform",
        )
    )

    registry.register(
        Entity(
            id="austin",
            entity_type="assistant",
            name="Austin",
            description="AI orchestration engine",
        )
    )

    relationships.add(
        Relationship(
            source="austin",
            relation="powers",
            target="guavacheck",
        )
    )
