"""
Surveyor General Connector
"""


class SurveyorGeneralConnector:

    async def verify_survey(

        self,

        survey_number: str,

    ) -> dict:

        return {

            "verified": False,

            "survey_number": survey_number,

            "status": "NOT_CONNECTED",

        }
