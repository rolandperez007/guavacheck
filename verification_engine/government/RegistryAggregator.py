"""
Registry Aggregator

Coordinates all government registry connectors and
returns a unified verification result.
"""

from verification_engine.government.CACConnector import (
    CACConnector,
)
from verification_engine.government.CourtJudgementConnector import (
    CourtJudgementConnector,
)
from verification_engine.government.GovernorConsentConnector import (
    GovernorConsentConnector,
)
from verification_engine.government.LandRegistryConnector import (
    LandRegistryConnector,
)
from verification_engine.government.SurveyorGeneralConnector import (
    SurveyorGeneralConnector,
)


class RegistryAggregator:
    """
    Central coordinator for all government verification
    connectors used by the Verification Engine.
    """

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
        """
        Runs all government verification stages.

        NOTE:
        Connectors currently return placeholder responses.
        They will later integrate with live government APIs.
        """

        land = {}
        survey = {}
        consent = {}
        company = {}
        court = {}

        return {
            "land_registry": land,
            "survey": survey,
            "governor_consent": consent,
            "company": company,
            "court": court,
            "overall_status": "NOT_CONNECTED",
            "confidence": 0.0,
            "verified_sources": 0,
            "available_sources": 5,
            "warnings": [
                "Government registry connectors are currently running in offline mode."
            ],
            "next_stage": "INTELLIGENCE_ENGINE",
        }
