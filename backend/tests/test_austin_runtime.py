from api.main import app
from austin.router import router
from austin.status import status


def test_app_has_expected_routes():
    assert app is not None
    paths = {route.path for route in app.routes if getattr(route, "path", None)}
    assert "/health" in paths
    assert "/austin/status" in paths


def test_austin_router_handles_message():
    result = router.route("session-1", "hello")

    assert result.engine == "austin"
    assert result.response
    assert status.online is True or status.startup_complete is True
