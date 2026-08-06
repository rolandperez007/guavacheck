"""
Knowledge Search
"""

from __future__ import annotations

from .entities import registry


class KnowledgeSearch:
    def search(self, query: str):

        query = query.lower()

        results = []

        for entity in registry.all():
            if query in entity.name.lower():
                results.append(entity)

                continue

            if any(query in alias.lower() for alias in entity.aliases):
                results.append(entity)

        return results


knowledge_search = KnowledgeSearch()
