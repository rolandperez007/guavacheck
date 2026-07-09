"""
Governor Consent Verification
"""


class GovernorConsentConnector:

    async def verify(

        self,

        consent_number: str,

    ) -> dict:

        return {

            "verified": False,

            "consent_number": consent_number,

            "status": "NOT_CONNECTED",

        }
