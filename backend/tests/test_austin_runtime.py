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
    assert result.job_id
    assert result.correlation_id
    assert status.online is True or status.startup_complete is True


def test_austin_router_enqueues_background_job_for_chat():
    result = router.route("session-2", "please analyze this property")

    job = router.queue.get_job(result.job_id)

    assert job is not None
    assert job.status in {"queued", "running", "completed"}
    assert job.correlation_id == result.correlation_id
