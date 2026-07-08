"""
Austin Logger

Central logging configuration.

Every Austin subsystem uses this logger.
"""

import logging


LOGGER_NAME = "Austin"


def get_logger() -> logging.Logger:

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s | %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = get_logger()