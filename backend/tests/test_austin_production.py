from austin.event_store import store
from austin.models import AustinEvent
from austin.router import router


def test_structured_event_is_stored_and_queryable():
    event = AustinEvent.create(
        event_type="AustinChatReceived",
        source_service="austin.router",
        engine="austin",
        severity="info",
        category="conversation",
        message="hello",
        correlation_id="corr-test",
        metadata={"intent": "chat"},
    )
    store.append(event)
    results = store.list(window="24h", correlation_id="corr-test")
    assert results
    assert results[0].correlation_id == "corr-test"


def test_router_emits_structured_event_with_correlation_id():
    result = router.route("session-3", "status")
    assert result.correlation_id
    assert result.trace_id
