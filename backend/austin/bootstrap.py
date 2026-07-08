"""
Austin Bootstrap

Initializes Austin during application startup.

This module connects every Austin subsystem together.
"""

from __future__ import annotations

from .logger import logger
from .personality import personality
from .registry import registry
from .startup import startup
from engines.property.engine import PropertyEngine
from engines.engineering.engine import EngineeringEngine
from engines.verification.engine import VerificationEngine
from engines.architecture.engine import ArchitectureEngine

def initialize():

    logger.info("")
    logger.info("=" * 70)
    logger.info("Initializing Austin Core")
    logger.info("=" * 70)

    loaded = personality.load()

    logger.info(
        "Loaded %s doctrine documents.",
        loaded,
    )

    ENGINES = [
        PropertyEngine,
        EngineeringEngine,
        ArchitectureEngine,
        VerificationEngine,
    ]

    for engine in ENGINES:
        registry.register(engine())

    startup()

    logger.info("Austin Bootstrap Complete.")

    return True