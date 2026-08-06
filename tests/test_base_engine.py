from app.austin.engines import BaseEngine


class DemoEngine(BaseEngine):

    @property
    def name(self):
        return "demo"

    def execute(
        self,
        request,
    ):
        return {
            "echo": request,
        }


def test_base_engine():

    engine = DemoEngine()

    assert (
        engine.name
        ==
        "demo"
    )

    assert (
        engine.health()["status"]
        ==
        "online"
    )

    assert (
        engine.execute(
            "hello"
        )["echo"]
        ==
        "hello"
    )