"""
Austin Bootstrap

Initializes Austin during application startup.
"""

from __future__ import annotations

from .logger import logger
from .personality import personality
from .realtime import subscribe_to_events
from .registry import registry
from .startup import startup


def bootstrap_austin() -> bool:
    """
    Initialize Austin.
    """

    logger.info("=" * 70)
    logger.info("Initializing Austin Core")
    logger.info("=" * 70)

    # Load doctrine/personality
    loaded = personality.load()

    logger.info(
        "Loaded %s doctrine documents.",
        loaded,
    )

    # Boot manifest-driven registry
    registry.boot()

    logger.info(
        "Austin Registry Booted"
    )

    logger.info(
        registry.health()
    )

    # Startup hooks
    startup()

    logger.info("=" * 70)
    logger.info("Austin Bootstrap Complete")
    logger.info("=" * 70)

    return True


async def startup_async() -> None:
    """
    Start realtime services.
    """

    logger.info(
        "Starting Austin realtime services..."
    )

    await subscribe_to_events()

    logger.info(
        "Austin realtime services online."
    )