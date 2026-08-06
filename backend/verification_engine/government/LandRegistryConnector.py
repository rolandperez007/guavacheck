"""
Land Registry Connector

Responsible for communicating with
government land registry databases.
"""

from __future__ import annotations


class LandRegistryConnector:
    def __init__(self):

        self.provider = "Government Land Registry"

    async def lookup_property(
        self,
        title_number: str,
    ):
        """
        Future:

        Query State Land Registry API
        """

        return {
            "found": False,
            "provider": self.provider,
            "title_number": title_number,
            "status": "NOT_IMPLEMENTED",
        }

    async def verify_owner(
        self,
        title_number: str,
        owner_name: str,
    ):

        return {"verified": False, "owner": owner_name, "status": "NOT_IMPLEMENTED"}
