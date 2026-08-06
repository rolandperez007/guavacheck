from app.austin.runtime import AustinOrchestrator



class MockRegistry:


    countries = {

        "Nigeria": {

            "name": "Nigeria"

        }

    }


    districts = {}



def test_austin_world_orchestrator():


    austin = AustinOrchestrator(

        registry=MockRegistry()

    )


    result = austin.process(

        "load nigeria",

        location="Nigeria",

    )


    assert (
        result["intent"]["intent"]
        ==
        "load"
    )


    assert (
        result["world"]["type"]
        ==
        "country"
    )


    assert (
        result["world"]["entity"]
        ==
        "Nigeria"
    )


    assert (
        result["plan"]["action"]
        ==
        "load_world_context"
    )