"""
Austin Health Monitor

Provides continuous health visibility for the platform.

Every subsystem should expose a health check.

Austin aggregates them into one operational view.
"""

from datetime import datetime

from .status import status
from .logger import logger


class HealthMonitor:

    def __init__(self):

        self.services = {}

    def register(self, name, callback):

        self.services[name] = callback

    def run(self):

        results = {}

        healthy = True

        for name, callback in self.services.items():

            try:

                results[name] = callback()

            except Exception as exc:

                results[name] = {

                    "healthy": False,

                    "error": str(exc),

                }

                healthy = False

        status.last_health_check = datetime.utcnow()

        status.healthy = healthy

        status.metadata["health"] = results

        return results

    def summary(self):

        total = len(self.services)

        healthy = sum(

            1

            for r in status.metadata.get(
                "health",
                {},
            ).values()

            if r.get("healthy")

        )

        return {

            "healthy": healthy,

            "total": total,

        }


health = HealthMonitor()


def heartbeat():

    logger.info("Austin heartbeat...")

    return health.run()