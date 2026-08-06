"""
Government Connectors

External government systems used by
guavacheck Verification Engine.
"""

"""
Government verification connectors.

Each connector is responsible for communicating with one official
government registry or authority.

The RegistryAggregator orchestrates all connectors.
"""

from .CACConnector import CACConnector
from .CourtJudgementConnector import CourtJudgementConnector
from .GovernorConsentConnector import GovernorConsentConnector
from .LandRegistryConnector import LandRegistryConnector
from .RegistryAggregator import RegistryAggregator
from .SurveyorGeneralConnector import SurveyorGeneralConnector

__all__ = [
    "CACConnector",
    "CourtJudgementConnector",
    "GovernorConsentConnector",
    "LandRegistryConnector",
    "RegistryAggregator",
    "SurveyorGeneralConnector",
]
