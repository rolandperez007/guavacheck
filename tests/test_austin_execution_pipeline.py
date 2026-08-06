from app.austin.engines import BaseEngine
from app.austin.runtime import AustinOrchestrator
from app.austin.runtime.router import EngineRegistry


class PropertyEngine(BaseEngine):

    @property
    def name(self):
        return "property"

    def execute(
        self,
        request,
    ):
        return {
            "message": f"Property engine executed: {request}"
        }


class MockRegistry:

    countries = {
        "Nigeria": {
            "name": "Nigeria",
        }
    }

    districts = {}


def test_austin_execution_pipeline():

    engine_registry = EngineRegistry()

    engine_registry.register(
        "property",
        PropertyEngine(),
    )

    orchestrator = AustinOrchestrator(
        registry=MockRegistry(),
    )

    # Inject the runtime engine registry
    orchestrator.router.registry = engine_registry

    result = orchestrator.process(
        "load nigeria",
        location="Nigeria",
    )

    assert result["status"] == "success"

    assert result["intent"]["intent"] == "load"

    assert result["world"]["entity"] == "Nigeria"

    assert result["execution"]["success"]

    assert (
        result["execution"]["result"]["message"]
        == "Property engine executed: load nigeria"
    )