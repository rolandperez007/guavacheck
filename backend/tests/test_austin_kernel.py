import asyncio

from engines.base import BaseEngine
from engines.property.engine import PropertyEngine
from austin.kernel import AustinKernel, RequestContext, build_request_context


class FailingEngine(BaseEngine):
    name = "failing"

    async def _execute_business_logic(self, request: dict):
        raise RuntimeError("boom")


def test_engine_receives_kernel_services():
    kernel = AustinKernel()
    engine = PropertyEngine(kernel=kernel)

    assert engine.kernel is kernel
    assert engine.event_publisher is not None
    assert engine.queue is not None
    assert engine.logger is not None
    assert engine.incident_reporter is not None


def test_request_context_includes_trace_and_correlation_ids():
    context = build_request_context(
        trace_id="trace-123",
        correlation_id="corr-123",
        user_context={"id": "u-1"},
        engine_context={"engine": "property"},
    )

    assert context.trace_id == "trace-123"
    assert context.correlation_id == "corr-123"
    assert context.user_context["id"] == "u-1"
    assert context.engine_context["engine"] == "property"


def test_engine_execute_emits_kernel_observability_and_queue_work():
    kernel = AustinKernel()
    engine = PropertyEngine(kernel=kernel)

    result = asyncio.run(engine.execute({"correlation_id": "corr-456", "trace_id": "trace-456"}))

    assert result["engine"] == "property"
    assert kernel.queue_service.summary()["total"] >= 1
    assert kernel.event_store.list(correlation_id="corr-456")


def test_engine_failure_creates_incident_and_health_signal():
    kernel = AustinKernel()
    engine = FailingEngine(kernel=kernel)

    try:
        asyncio.run(engine.execute({"correlation_id": "corr-fail", "trace_id": "trace-fail"}))
    except RuntimeError:
        pass

    incidents = kernel.incident_reporter.list()
    assert incidents
    assert incidents[-1].severity == "high"
    assert kernel.event_store.list(correlation_id="corr-fail")
