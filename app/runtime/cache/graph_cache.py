from typing import Dict

from app.property.schemas.graph import PropertyGraph


class PropertyGraphCache:

    """
    Simple in-memory cache.

    Replace with Redis later.
    """

    def __init__(self):

        self._cache: Dict[str, PropertyGraph] = {}

    def get(self, property_id: str):

        return self._cache.get(property_id)

    def set(
        self,
        property_id: str,
        graph: PropertyGraph,
    ):

        self._cache[property_id] = graph

    def invalidate(
        self,
        property_id: str,
    ):

        self._cache.pop(
            property_id,
            None,
        )