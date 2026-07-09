"""
Corporate Affairs Commission Connector

Used when property owner
is a company.
"""


class CACConnector:

    async def lookup(

        self,

        rc_number: str,

    ) -> dict:

        return {

            "exists": False,

            "rc_number": rc_number,

            "status": "NOT_CONNECTED",

        }
