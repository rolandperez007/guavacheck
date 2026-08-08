from app.austin.engines import BaseEngine
from app.austin.engines.loader import EngineLoader


class DemoEngine(BaseEngine):

    @property
    def name(self):
        return "demo"

    def execute(
        self,
        request,
    ):
        return {
            "ok": True,
        }


def test_engine_loader():

    loader = EngineLoader()

    loader.register(
        DemoEngine(),
    )

    registry = loader.get_registry()

    assert registry.get(
        "demo"
    ) is not None

    summary = loader.registry_summary()

    assert (
        summary["engines"]
        ==
        1
    )