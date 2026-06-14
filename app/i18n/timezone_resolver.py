class TimezoneResolver:
    ZONES = {
        "NG": "Africa/Lagos",
        "US": "America/New_York",
        "GB": "Europe/London",
        "AE": "Asia/Dubai",
        "IN": "Asia/Kolkata",
        "CA": "America/Toronto",
    }

    @staticmethod
    def resolve(country: str):
        return TimezoneResolver.ZONES.get(country, "UTC")
