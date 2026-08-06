"""
Austin Engine Exceptions
"""


class AustinEngineError(Exception):
    """
    Base Austin engine exception.
    """


class EngineExecutionError(AustinEngineError):
    """
    Raised when an engine execution fails.
    """


class EngineValidationError(AustinEngineError):
    """
    Raised when engine input validation fails.
    """
