"""
Austin Bootstrap

Initializes Austin during application startup.

This module connects every Austin subsystem together.
"""

from __future__ import annotations
from .registry.loader import register_defaults
from .logger import logger
from .personality import personality
from .realtime import subscribe_to_events
from .registry import registry
from .startup import startup
from backend.engines.property.engine import PropertyEngine
from backend.engines.engineering.engine import EngineeringEngine
from backend.engines.verification.engine import VerificationEngine
from backend.engines.architecture.engine import ArchitectureEngine

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

    startup(register_defaults)

    logger.info("Austin Bootstrap Complete.")

    return True
import asyncio

async def startup_async():

    logger.info("Starting Austin event subscriptions...")

    await subscribe_to_events()

    logger.info("Austin realtime services online.")