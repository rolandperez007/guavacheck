class GeoResolver:
    # -----------------------------
    # GLOBAL LOCATION DATABASE (v1)
    # lightweight but scalable
    # -----------------------------
    LOCATIONS = {
        # 🇳🇬 Nigeria
        "lekki": {
            "city": "Lagos",
            "state": "Lagos",
            "country": "Nigeria",
            "currency": "NGN",
            "tier": "emerging_luxury",
        },
        "ajah": {
            "city": "Lagos",
            "state": "Lagos",
            "country": "Nigeria",
            "currency": "NGN",
            "tier": "emerging",
        },
        "ikoyi": {
            "city": "Lagos",
            "state": "Lagos",
            "country": "Nigeria",
            "currency": "NGN",
            "tier": "luxury",
        },
        "victoria island": {
            "city": "Lagos",
            "state": "Lagos",
            "country": "Nigeria",
            "currency": "NGN",
            "tier": "luxury",
        },
        # 🇦🇪 UAE
        "dubai marina": {
            "city": "Dubai",
            "state": "Dubai",
            "country": "UAE",
            "currency": "AED",
            "tier": "global_luxury",
        },
        "downtown dubai": {
            "city": "Dubai",
            "state": "Dubai",
            "country": "UAE",
            "currency": "AED",
            "tier": "global_luxury",
        },
        # 🇬🇧 UK
        "canary wharf": {
            "city": "London",
            "state": "England",
            "country": "United Kingdom",
            "currency": "GBP",
            "tier": "global_luxury",
        },
        # 🇺🇸 USA
        "manhattan": {
            "city": "New York",
            "state": "New York",
            "country": "United States",
            "currency": "USD",
            "tier": "global_luxury",
        },
        "brooklyn": {
            "city": "New York",
            "state": "New York",
            "country": "United States",
            "currency": "USD",
            "tier": "developed",
        },
    }

    @staticmethod
    def resolve(location_text: str | None):
        if not location_text:
            return {"raw": None, "resolved": None}

        key = location_text.lower().strip()

        # direct match
        if key in GeoResolver.LOCATIONS:
            data = GeoResolver.LOCATIONS[key]

            return {"raw": location_text, "resolved": {"district": key.title(), **data}}

        # partial match fallback
        for loc_key, data in GeoResolver.LOCATIONS.items():
            if loc_key in key:
                return {
                    "raw": location_text,
                    "resolved": {"district": loc_key.title(), **data},
                }

        # unknown location (still global-ready)
        return {
            "raw": location_text,
            "resolved": {
                "district": location_text,
                "city": None,
                "state": None,
                "country": None,
                "currency": None,
                "tier": "unknown",
            },
        }
