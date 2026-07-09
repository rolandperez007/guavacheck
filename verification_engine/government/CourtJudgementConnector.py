"""
Court Judgement Connector

Checks litigation records.
"""


class CourtJudgementConnector:

    async def search(

        self,

        property_id: str,

    ) -> dict:

        return {

            "litigation": False,

            "status": "NOT_CONNECTED",

        }
