"""
Property Search

Search utilities for properties.
"""

from __future__ import annotations

from typing import List


class PropertySearch:

    def search(

        self,

        request: dict,

    ):

        #
        # Future:
        # Supabase Search
        # Geo Search
        # AI Ranking
        #

        return {

            "query": request,

            "results": [],

            "count": 0,

            "message": "Search completed.",

        }

    def recommend(

        self,

        user_id: str,

    ):

        return []

    def similar(

        self,

        property_id: str,

    ):

        return []


property_search = PropertySearch()