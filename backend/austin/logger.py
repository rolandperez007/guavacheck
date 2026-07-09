"""
Austin Logger

Central logging configuration.

Every Austin subsystem uses this logger.
"""

import logging
import json
from datetime import datetime, timezone


LOGGER_NAME = "Austin"


def get_logger() -> logging.Logger:

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | level=%(levelname)s | service=austin | event=%(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def structured_log(*, message: str, correlation_id: str | None = None, trace_id: str | None = None, engine: str = "austin", duration_ms: int | None = None, outcome: str = "ok", severity: str = "info", service: str = "austin") -> None:
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "trace_id": trace_id,
        "correlation_id": correlation_id,
        "engine": engine,
        "duration_ms": duration_ms,
        "outcome": outcome,
        "severity": severity,
        "service": service,
        "message": message,
    }
    logger.info(json.dumps(payload))


logger = get_logger()