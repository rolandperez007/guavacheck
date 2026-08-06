from app.world.loader import WorldLoader
from app.world.registry import WorldRegistry
from app.world.kernel.world_kernel import WorldKernel



def test_world_loader_pipeline():


    registry = WorldRegistry()


    loader = WorldLoader(
        registry
    )


    loader.load_country(
        "Nigeria",
        {
            "currency": "NGN",
            "continent": "Africa",
        },
    )


    loader.load_district(
        "Lagos Island",
        {
            "type": "commercial",
            "sector": "real_estate",
        },
    )


    kernel = WorldKernel(
        registry=registry
    )


    result = kernel.resolve_location(
        "Nigeria",
        "Lagos Island",
    )


    assert (
        result["country_data"]["currency"]
        ==
        "NGN"
    )


    assert (
        result["district_data"]["sector"]
        ==
        "real_estate"
    )