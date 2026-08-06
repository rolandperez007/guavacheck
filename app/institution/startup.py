from app.institution.bootstrap import (
    register_events,
)


def initialize() -> None:
    """
    Initializes the Institution Platform.
    """

    register_events()

    print(
        "Institution Platform initialized."
    )