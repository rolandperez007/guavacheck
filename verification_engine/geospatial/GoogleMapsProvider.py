"""
Google Maps Provider
"""


class GoogleMapsProvider:
    async def reverse_geocode(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:

        return {
            "provider": "Google",
            "address": None,
            "latitude": latitude,
            "longitude": longitude,
            "status": "NOT_CONNECTED",
        }
