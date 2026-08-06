from app.world.geography import (
    LocationNode,
    GeographyRegistry,
    GeographyResolver,
)



def test_geography_resolution():


    registry = GeographyRegistry()


    world = LocationNode(
        name="World",
        level="planet",
    )


    nigeria = LocationNode(
        name="Nigeria",
        level="country",
        parent="World",
    )


    lagos = LocationNode(
        name="Lagos",
        level="state",
        parent="Nigeria",
    )


    victoria_island = LocationNode(
        name="Victoria Island",
        level="district",
        parent="Lagos",
    )


    registry.add(world)

    registry.add(nigeria)

    registry.add(lagos)

    registry.add(victoria_island)


    resolver = GeographyResolver(
        registry
    )


    path = resolver.resolve_path(
        "Victoria Island"
    )


    assert path == [
        "World",
        "Nigeria",
        "Lagos",
        "Victoria Island",
    ]