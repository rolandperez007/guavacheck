from app.austin.runtime.reasoning import ReasoningPlanner



def test_reasoning_planner():


    planner = ReasoningPlanner()


    result = planner.plan(

        "load",

        {
            "project": "World OS"
        }

    )


    assert (
        result["action"]
        ==
        "load_world_context"
    )


    assert (
        result["context"]["project"]
        ==
        "World OS"
    )