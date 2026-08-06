from app.austin.runtime.world import WorldResolver



class MockRegistry:


    countries = {

        "Nigeria": {

            "name": "Nigeria"

        }

    }


    districts = {

        "Victoria Island": {

            "name": "Victoria Island"

        }

    }



def test_world_resolver():


    resolver = WorldResolver(

        registry=MockRegistry()

    )


    country = resolver.resolve(
        "Nigeria"
    )


    assert (
        country["type"]
        ==
        "country"
    )


    district = resolver.resolve(
        "Victoria Island"
    )


    assert (
        district["type"]
        ==
        "district"
    )