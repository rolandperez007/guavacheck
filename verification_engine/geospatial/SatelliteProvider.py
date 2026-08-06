"""
Satellite Imagery Provider
"""


class SatelliteProvider:
    async def fetch_image(
        self,
        latitude: float,
        longitude: float,
    ) -> dict:

        return {
            "provider": "Satellite",
            "image": None,
            "resolution": None,
            "status": "NOT_CONNECTED",
        }
