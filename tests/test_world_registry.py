from app.world.registry import WorldRegistry



def test_world_registry():


    registry = WorldRegistry()


    registry.register_country(
        "Nigeria",
        {
            "currency": "NGN",
            "region": "West Africa",
        },
    )


    registry.register_district(
        "Victoria Island",
        {
            "type": "commercial",
        },
    )


    assert (
        registry.get_country("Nigeria")
        ["currency"]
        ==
        "NGN"
    )


    assert (
        registry.get_district("Victoria Island")
        ["type"]
        ==
        "commercial"
    )