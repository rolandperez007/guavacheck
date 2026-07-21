"""
Austin Registry Loader

Registers all default Austin engines.
"""

from backend.engines.property.engine import PropertyEngine
from backend.engines.engineering.engine import EngineeringEngine
from backend.engines.architecture.engine import ArchitectureEngine
from backend.engines.verification.engine import VerificationEngine

from .registry import registry


def register_defaults() -> None:
    """
    Register all built-in engines.
    """

    registry.register(PropertyEngine())
    registry.register(EngineeringEngine())
    registry.register(ArchitectureEngine())
    registry.register(VerificationEngine())