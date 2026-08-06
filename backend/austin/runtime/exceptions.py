"""
Austin Runtime Exceptions
"""

from __future__ import annotations


class AustinRuntimeError(Exception):
    """Base runtime exception."""


class PlannerError(AustinRuntimeError):
    pass


class DispatchError(AustinRuntimeError):
    pass


class EngineExecutionError(AustinRuntimeError):
    pass


class ValidationError(AustinRuntimeError):
    pass


class ContextError(AustinRuntimeError):
    pass


class EngineNotFoundError(AustinRuntimeError):
    pass
