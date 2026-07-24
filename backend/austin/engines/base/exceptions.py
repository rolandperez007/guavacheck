"""
Austin Engine Exceptions
"""


class AustinEngineError(Exception):
    """
    Base Austin engine exception.
    """
    pass


class EngineExecutionError(AustinEngineError):
    """
    Raised when an engine execution fails.
    """
    pass


class EngineValidationError(AustinEngineError):
    """
    Raised when engine input validation fails.
    """
    pass
