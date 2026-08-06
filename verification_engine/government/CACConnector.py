"""
Corporate Affairs Commission Connector

Used when property owner
is a company.
"""


class CACConnector:
    """
    Corporate Affairs Commission connector.

    Used for verifying company ownership
    involved in property transactions.
    """

    source = "CAC"

    def verify_company(self, rc_number: str) -> dict:

        return {
            "verified": False,
            "status": "offline",
            "confidence": 0.0,
            "source": self.source,
            "rc_number": rc_number,
            "message": "CAC connector not yet implemented.",
        }
