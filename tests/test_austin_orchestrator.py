from app.austin.runtime import AustinOrchestrator



def test_austin_orchestrator():


    austin = AustinOrchestrator()


    result = austin.process(

        "ok loasd nigeria"

    )


    assert (
        result["intent"]["normalized"]
        ==
        "ok load nigeria"
    )


    assert (
        result["intent"]["intent"]
        ==
        "load"
    )


    assert (
        result["plan"]["action"]
        ==
        "load_world_context"
    )


    assert (
        result["context"]["last_action"]
        ==
        "load_world_context"
    )