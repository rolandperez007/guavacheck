"""
Shared database constants.

These values are reused across ORM models to maintain
consistency throughout the platform.
"""

# UUID

UUID_LENGTH = 36

# Common string lengths

SHORT_CODE_LENGTH = 20
PHONE_LENGTH = 25
EMAIL_LENGTH = 320
URL_LENGTH = 500

# Names

MAX_NAME_LENGTH = 255
MAX_TITLE_LENGTH = 255

# Text

DESCRIPTION_LENGTH = 5000
SHORT_DESCRIPTION_LENGTH = 1000

# Status

STATUS_LENGTH = 30

# Country / Location

COUNTRY_CODE_LENGTH = 2
STATE_LENGTH = 100
CITY_LENGTH = 100
POSTAL_CODE_LENGTH = 20

# Colors

COLOR_LENGTH = 20

# API

API_KEY_LENGTH = 128

# Pagination

DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100

# Versioning

DEFAULT_VERSION = 1