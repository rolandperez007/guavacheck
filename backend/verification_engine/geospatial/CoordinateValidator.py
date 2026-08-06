"""
Coordinate Validator

Verifies GPS coordinates.
"""

from math import fabs


class CoordinateValidator:
    def validate(
        self,
        latitude: float,
        longitude: float,
    ):

        if fabs(latitude) > 90:
            return False

        if fabs(longitude) > 180:
            return False

        return True
