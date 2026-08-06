"""
Certificate of Occupancy /
Title Verification
"""

from __future__ import annotations


class TitleRegistryConnector:
    async def verify_title(
        self,
        title_number: str,
    ):

        return {"title": title_number, "valid": False, "status": "NOT_IMPLEMENTED"}
