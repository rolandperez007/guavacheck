from app.austin.runtime.router import EngineRegistry


class MockEngine:

    pass


def test_engine_registry():

    registry = EngineRegistry()

    registry.register(
        "property",
        MockEngine(),
    )

    registry.register(
        "construction",
        MockEngine(),
    )

    assert registry.exists(
        "property"
    )

    assert registry.exists(
        "construction"
    )

    assert (
        registry.summary()["engines"]
        == 2
    )

    assert (
        registry.get("property")
        is not None
    )