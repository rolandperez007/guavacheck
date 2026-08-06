from app.austin.runtime.context import SessionContext



def test_session_context():


    session = SessionContext(

        project="World OS",

        phase="Austin Cognitive Runtime",

        domain="property intelligence",

    )


    assert (
        session.get("project")
        ==
        "World OS"
    )


    assert (
        session.get("phase")
        ==
        "Austin Cognitive Runtime"
    )


    session.remember_action(
        "created intent normalizer"
    )


    assert (
        session.get("last_action")
        ==
        "created intent normalizer"
    )


    snapshot = session.snapshot()


    assert (
        snapshot["domain"]
        ==
        "property intelligence"
    )