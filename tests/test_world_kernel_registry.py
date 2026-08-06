from app.world.kernel.world_kernel import WorldKernel
from app.world.registry import WorldRegistry



def test_kernel_registry_connection():


    registry = WorldRegistry()


    registry.register_country(
        "Kenya",
        {
            "currency": "KES",
        },
    )


    registry.register_district(
        "Nairobi",
        {
            "category": "commercial",
        },
    )


    kernel = WorldKernel(
        registry=registry
    )


    result = kernel.resolve_location(
        "Kenya",
        "Nairobi",
    )


    assert (
        result["country_data"]["currency"]
        ==
        "KES"
    )


    assert (
        result["district_data"]["category"]
        ==
        "commercial"
    )