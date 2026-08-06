from app.austin.runtime.execution import EngineExecutor


class MockEngine:

    def execute(
        self,
        request,
    ):
        return {
            "message": f"Executed: {request}"
        }


def test_engine_executor():

    executor = EngineExecutor()

    result = executor.execute(
        MockEngine(),
        "hello world",
    )

    assert result["success"]

    assert (
        result["engine"]
        ==
        "MockEngine"
    )

    assert (
        result["result"]["message"]
        ==
        "Executed: hello world"
    )