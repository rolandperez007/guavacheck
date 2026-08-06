from app.world.countries import CountryGenerator
from app.world.templates import TemplateEngine



def test_country_generation():


    template = {

        "currency": "GLOBAL",

        "construction": "standard",

        "verification": True,

    }


    nigeria = {

        "currency": "NGN",

        "construction": "Nigerian standards",

    }


    generator = CountryGenerator(
        TemplateEngine()
    )


    country = generator.create(

        "Nigeria",

        template,

        nigeria,

    )


    assert country.name == "Nigeria"


    assert (
        country.data["currency"]
        ==
        "NGN"
    )


    assert (
        country.data["verification"]
        is True
    )