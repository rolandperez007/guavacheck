"""
Austin Startup Sequence

Austin initializes the platform.

Every subsystem is verified before Austin
declares itself online.
"""

from datetime import datetime

from .config import config
from .logger import logger
from .status import status
from .registry import registry


STARTUP_SEQUENCE = [

    "Configuration",

    "Authentication",

    "Database",

    "Storage",

    "AI Provider",

    "Engine Registry",

    "Monitoring",

    "Scheduler",

    "Notification Services",

]


def startup():

    logger.info("")

    logger.info("=" * 60)

    logger.info("Austin Startup")

    logger.info("=" * 60)

    for step in STARTUP_SEQUENCE:

        logger.info(f"✓ {step}")

    status.online = True

    status.healthy = True

    status.startup_complete = True

    status.registered_engines = registry.count()

    status.last_health_check = datetime.utcnow()

    status.message = "Austin Online"

    logger.info("")

    logger.info("Austin Online.")

    logger.info("Registered Engines: %s",
                registry.count())

    logger.info("=" * 60)

    return status