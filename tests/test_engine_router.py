from app.austin.runtime.router import (
    EngineRegistry,
    EngineRouter,
)


class PropertyEngine:
    pass


class ConstructionEngine:
    pass


def test_engine_router():

    registry = EngineRegistry()

    registry.register(
        "property",
        PropertyEngine(),
    )

    registry.register(
        "construction",
        ConstructionEngine(),
    )

    router = EngineRouter(
        registry
    )

    property_engine = router.route(
        "property_search"
    )

    assert isinstance(
        property_engine,
        PropertyEngine,
    )

    construction_engine = router.route(
        "construction_estimate"
    )

    assert isinstance(
        construction_engine,
        ConstructionEngine,
    )