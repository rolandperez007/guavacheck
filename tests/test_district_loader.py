from app.world.loader import DistrictLoader
from app.world.districts import DistrictGenerator
from app.world.registry import WorldRegistry
from app.world.templates import TemplateEngine



def test_district_loader_pipeline():


    registry = WorldRegistry()


    generator = DistrictGenerator(
        TemplateEngine()
    )


    loader = DistrictLoader(

        generator,

        registry,

    )


    district = loader.load(

        "Victoria Island",

        "Nigeria",

        {
            "type": "district",
            "security": "standard",
        },

        {
            "type": "commercial",
            "market": "premium_real_estate",
        },

    )


    assert district.name == "Victoria Island"


    assert district.country == "Nigeria"


    stored = registry.get_district(
        "Victoria Island"
    )


    assert (
        stored["type"]
        ==
        "commercial"
    )


    assert (
        stored["market"]
        ==
        "premium_real_estate"
    )