"""
OpenStreetMap Provider
"""


class OpenStreetMapProvider:
    async def reverse_geocode(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:

        return {
            "provider": "OpenStreetMap",
            "address": None,
            "latitude": latitude,
            "longitude": longitude,
            "status": "NOT_CONNECTED",
        }
