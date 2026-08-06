"""
Parcel Matching Engine

Matches survey coordinates
to cadastral parcels.
"""


class ParcelMatcher:
    async def match(
        self,
        coordinates,
    ):

        return {"matched": False, "parcel": None}
