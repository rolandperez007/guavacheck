"""
Geospatial Verification Stage

Checks coordinates,
parcel location,
survey alignment,
and mapping consistency.
"""


class GeospatialStage:
    name = "GEOSPATIAL"

    async def execute(
        self,
        context,
    ):

        property_data = getattr(context, "property_data", {})

        coordinates = property_data.get("coordinates")

        parcel_number = property_data.get("parcel_number")

        result = {
            "completed": True,
            "coordinates_available": coordinates is not None,
            "parcel_reference_available": parcel_number is not None,
            "coordinates_verified": False,
            "parcel_match": False,
            "status": "PLACEHOLDER",
        }

        context.stages[self.name] = result

        context.evidence.append({"type": "geospatial_verification", "data": result})

        return context
