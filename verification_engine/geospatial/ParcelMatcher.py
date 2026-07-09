"""
Parcel Matching Engine
"""


class ParcelMatcher:

    async def match(

        self,

        property_data: dict,

    ) -> dict:

        return {

            "matched": False,

            "confidence": 0,

            "parcel_id": None,

        }
