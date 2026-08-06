from app.world.registry import WorldGraphRegistry
from app.world.geography import LocationNode



def test_world_graph_registry():


    registry = WorldGraphRegistry()


    registry.register_country(

        "Nigeria",

        {
            "currency": "NGN",
        }

    )


    registry.register_district(

        "Victoria Island",

        {
            "type": "commercial",
        }

    )


    lagos = LocationNode(

        name="Lagos",

        level="state",

        parent="Nigeria",

    )


    registry.register_location(
        lagos
    )


    assert (
        registry.get_country(
            "Nigeria"
        )["currency"]
        ==
        "NGN"
    )


    assert (
        registry.get_district(
            "Victoria Island"
        )["type"]
        ==
        "commercial"
    )


    assert (
        registry.get_location(
            "Lagos"
        ).level
        ==
        "state"
    )


    assert (
        registry.summary()
        ==
        {
            "countries": 1,
            "districts": 1,
            "locations": 1,
        }
    )