"""
Registry Aggregator

Queries every registry and
combines results.
"""

from verification_engine.government.LandRegistryConnector import (
    LandRegistryConnector,
)

from verification_engine.government.SurveyorGeneralConnector import (
    SurveyorGeneralConnector,
)

from verification_engine.government.GovernorConsentConnector import (
    GovernorConsentConnector,
)

from verification_engine.government.CACConnector import (
    CACConnector,
)

from verification_engine.government.CourtJudgementConnector import (
    CourtJudgementConnector,
)


class RegistryAggregator:

    def __init__(self):

        self.land = LandRegistryConnector()

        self.survey = SurveyorGeneralConnector()

        self.consent = GovernorConsentConnector()

        self.cac = CACConnector()

        self.court = CourtJudgementConnector()

    async def verify(

        self,

        property_data: dict,

    ) -> dict:

        return {

            "land_registry": {},

            "survey": {},

            "governor_consent": {},

            "company": {},

            "court": {},

            "overall_status": "NOT_CONNECTED",

        }
