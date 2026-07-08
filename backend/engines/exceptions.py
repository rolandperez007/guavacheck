"""
Engine Exceptions
"""


class EngineError(Exception):
    """Base engine exception."""


class EngineNotFound(EngineError):
    """Requested engine does not exist."""


class EngineDisabled(EngineError):
    """Engine is currently disabled."""


class EngineExecutionError(EngineError):
    """Engine failed during execution."""