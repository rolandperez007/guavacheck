"""
Health API

Platform health endpoints.
"""

from fastapi import APIRouter

from backend.austin.business_monitor import monitor
from backend.austin.event_store import store
from backend.austin.events import events
from backend.austin.incident_manager import manager
from backend.austin.queue import queue
from backend.austin.recommendations import AustinRecommendations
from backend.austin.status import status
from backend.austin.trust import TrustMonitor

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def platform_health():

    return {
        "platform": "guavacheck",
        "status": "healthy" if status.healthy else "degraded",
        "austin": status.online,
        "registered_engines": status.registered_engines,
        "message": status.message,
    }


@router.get("/live")
async def live():

    return {"alive": True}


@router.get("/ready")
async def ready():

    return {"ready": status.startup_complete}


@router.get("/metrics")
async def metrics():
    recommendation_engine = AustinRecommendations()
    recommendation = recommendation_engine.explain(
        queue_depth=queue.summary()["queued"],
        active_workers=3,
        wait_time_ms=820,
    )
    return {
        "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        "cpu": 48,
        "memory": 62,
        "requests": 128,
        "engines": [
            {
                "name": "intent",
                "status": "active",
                "load": 72,
                "requests": 84,
                "responseTime": 131,
            },
            {
                "name": "planner",
                "status": "active",
                "load": 53,
                "requests": 42,
                "responseTime": 118,
            },
            {
                "name": "reasoning",
                "status": "active",
                "load": 64,
                "requests": 57,
                "responseTime": 143,
            },
        ],
        "queue": {
            **queue.summary(),
            "active_workers": 3,
            "average_wait_time_ms": 820,
            "average_processing_time_ms": 142,
            "retry_count": 4,
            "failed_jobs": queue.summary()["failed"],
            "dead_letter_queue": 0,
            "worker_utilization": 78,
        },
        "memoryStats": {
            "total": 16,
            "used": 9,
            "free": 7,
        },
        "events": events.registered_events(),
        "recommendation": recommendation,
        "business_workflows": monitor.snapshot(),
        "incidents": [incident.__dict__ for incident in manager.list()],
        "trust": TrustMonitor().snapshot(),
        "event_store": store.summary(),
    }


@router.get("/events")
async def events_history(
    window: str = "1h",
    engine: str | None = None,
    severity: str | None = None,
    category: str | None = None,
    correlation_id: str | None = None,
):
    return {
        "window": window,
        "events": [
            {
                "event_id": event.event_id,
                "timestamp": event.timestamp.isoformat(),
                "correlation_id": event.correlation_id,
                "event_type": event.event_type,
                "source_service": event.source_service,
                "engine": event.engine,
                "severity": event.severity,
                "category": event.category,
                "message": event.message,
                "metadata": event.metadata,
            }
            for event in store.list(
                window=window,
                engine=engine,
                severity=severity,
                category=category,
                correlation_id=correlation_id,
            )
        ],
    }


@router.post("/incidents")
async def create_incident(payload: dict):
    incident = manager.create_incident(
        severity=payload.get("severity", "medium"),
        affected_services=payload.get("affected_services", []),
        affected_customers=payload.get("affected_customers", 0),
        estimated_revenue_impact=payload.get("estimated_revenue_impact", 0.0),
        likely_root_cause=payload.get("likely_root_cause", "unknown"),
        recovery_status=payload.get("recovery_status", "investigating"),
        recommendation=payload.get("recommendation", "Investigate immediately"),
    )
    return incident.__dict__
