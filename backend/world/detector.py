"""
World Detector

Determines the user's global profile.
"""

from __future__ import annotations

from .profile import WorldProfile


class WorldDetector:
    DEFAULT = WorldProfile(
        country="Nigeria",
        language="en",
        currency="NGN",
        timezone="Africa/Lagos",
        unit_system="metric",
        locale="en-NG",
        region="Africa",
    )

    def detect(
        self,
        session_id: str | None = None,
    ) -> WorldProfile:

        #
        # Future sources:
        #
        # Browser locale
        # GPS
        # User profile
        # Austin Memory
        # IP geolocation
        #

        return self.DEFAULT


world_detector = WorldDetector()
