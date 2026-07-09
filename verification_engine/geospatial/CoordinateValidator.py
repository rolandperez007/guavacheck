"""
Coordinate Validator
"""


class CoordinateValidator:

    async def validate(

        self,

        latitude: float,

        longitude: float,

    ) -> dict:

        valid = (

            -90 <= latitude <= 90

            and

            -180 <= longitude <= 180

        )

        return {

            "valid": valid,

            "latitude": latitude,

            "longitude": longitude,

        }
