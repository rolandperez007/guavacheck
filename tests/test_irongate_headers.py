from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_warn_includes_header_and_allows():
    payload = {"payload": {"query": "free money click here buy now unique-test-1"}}
    r = client.post("/irongate/evaluate", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["decision"] == "warn"
    assert data["score"] == 70
    assert r.headers.get("X-IronGate-Decision") == "warn"
    assert r.headers.get("X-IronGate-Score") == "70"


def test_block_includes_header_and_forbids():
    payload = {
        "payload": {"query": "free money click here buy now unique-test-2"},
        "user_id": "test_spam_user",
    }
    r = client.post("/irongate/evaluate", json=payload)
    assert r.status_code == 403
    # The body may be a JSON error; ensure header is set
    assert r.headers.get("X-IronGate-Decision") == "block"
    assert r.headers.get("X-IronGate-Score") is not None
