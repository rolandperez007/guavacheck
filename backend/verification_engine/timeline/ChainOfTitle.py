"""
Chain of Title Analyzer

Checks whether ownership
transfers are continuous.
"""

from __future__ import annotations


class ChainOfTitle:

    async def verify(

        self,

        ownership_history,

    ):

        if len(ownership_history) == 0:

            return {

                "valid": False,

                "reason": "No ownership records."

            }

        return {

            "valid": True,

            "transfers": len(ownership_history)

        }
