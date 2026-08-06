from app.world.loader import CountryLoader
from app.world.countries import CountryGenerator
from app.world.registry import WorldRegistry
from app.world.templates import TemplateEngine



def test_country_loader_pipeline():


    registry = WorldRegistry()


    generator = CountryGenerator(
        TemplateEngine()
    )


    loader = CountryLoader(

        generator,

        registry,

    )


    country = loader.load(

        "Nigeria",

        {
            "currency": "GLOBAL",
            "verification": True,
        },

        {
            "currency": "NGN",
        },

    )


    assert country.name == "Nigeria"


    stored = registry.get_country(
        "Nigeria"
    )


    assert (
        stored["currency"]
        ==
        "NGN"
    )


    assert (
        stored["verification"]
        is True
    )