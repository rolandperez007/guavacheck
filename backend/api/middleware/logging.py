"""
Request Logging Middleware
"""

import time

from starlette.middleware.base import BaseHTTPMiddleware

from backend.austin.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.time()

        response = await call_next(request)

        duration = round(
            time.time() - start,
            3,
        )

        logger.info(
            "%s %s (%ss)",
            request.method,
            request.url.path,
            duration,
        )

        return response
