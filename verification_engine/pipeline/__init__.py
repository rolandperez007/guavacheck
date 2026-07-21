"""
Verification Pipeline

Executes every verification stage in sequence
before handing results to the Intelligence Engine.
"""

from .OCRStage import OCRStage
from .DocumentStage import DocumentStage
from .GeospatialStage import GeospatialStage
from .RegistryStage import RegistryStage
from .RuleStage import RuleStage
from .FraudStage import FraudStage
from .TimelineStage import TimelineStage
from .TrustStage import TrustStage
from .CertificateStage import CertificateStage
from .PersistenceStage import PersistenceStage

__all__ = [
    "OCRStage",
    "DocumentStage",
    "GeospatialStage",
    "RegistryStage",
    "RuleStage",
    "FraudStage",
    "TimelineStage",
    "TrustStage",
    "CertificateStage",
    "PersistenceStage",
]