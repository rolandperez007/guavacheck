from app.world.data import WorldSeeder
from app.world.registry import WorldGraphRegistry



def test_geography_seeder():


    registry = WorldGraphRegistry()


    seeder = WorldSeeder(
        registry
    )


    result = seeder.seed()


    assert (
        result["countries"]
        >=
        1
    )


    assert (
        result["districts"]
        >=
        1
    )


    nigeria = registry.get_country(
        "Nigeria"
    )


    assert nigeria is not None


    victoria = registry.get_district(
        "Victoria Island"
    )


    assert victoria is not None