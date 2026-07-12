"""
Austin Knowledge Graph
"""

from __future__ import annotations

from .entities import registry
from .relationships import relationships


class KnowledgeGraph:

    def entity(self, entity_id: str):

        return registry.get(entity_id)

    def neighbours(self, entity_id: str):

        results = []

        for relation in relationships.outgoing(entity_id):

            entity = registry.get(relation.target)

            if entity:

                results.append(

                    {
                        "relationship": relation.relation,

                        "entity": entity,
                    }

                )

        return results

    def statistics(self):

        return {

            "entities": registry.count(),

            "relationships": len(

                relationships.all()

            ),

        }


graph = KnowledgeGraph()