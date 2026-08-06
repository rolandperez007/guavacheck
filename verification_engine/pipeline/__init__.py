"""
Verification Pipeline

Executes every verification stage in sequence
before handing results to the Intelligence Engine.
"""

from .CertificateStage import CertificateStage
from .DocumentStage import DocumentStage
from .FraudStage import FraudStage
from .GeospatialStage import GeospatialStage
from .OCRStage import OCRStage
from .PersistenceStage import PersistenceStage
from .RegistryStage import RegistryStage
from .RuleStage import RuleStage
from .TimelineStage import TimelineStage
from .TrustStage import TrustStage

__all__ = [
    "CertificateStage",
    "DocumentStage",
    "FraudStage",
    "GeospatialStage",
    "OCRStage",
    "PersistenceStage",
    "RegistryStage",
    "RuleStage",
    "TimelineStage",
    "TrustStage",
]
