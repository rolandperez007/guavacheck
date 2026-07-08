"""
Governor Consent Verification
"""

from __future__ import annotations


class GovernorConsentChecker:

    async def verify(

        self,

        consent_number: str,

    ):

        return {

            "consent_number": consent_number,

            "verified": False,

            "status": "NOT_IMPLEMENTED"

        }
