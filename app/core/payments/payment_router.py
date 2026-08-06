from app.core.payment_providers.flutterwave_provider import FlutterwaveProvider
from app.core.payment_providers.paystack_provider import PaystackProvider
from app.core.payment_providers.stripe_provider import StripeProvider


class PaymentRouter:
    def __init__(self):
        self.providers = {
            "paystack": PaystackProvider(),
            "flutterwave": FlutterwaveProvider(),
            "stripe": StripeProvider(),
        }

    # 🌍 GLOBAL SMART ROUTING
    def select_provider(self, currency: str, country: str = None):
        currency = currency.upper() if currency else "USD"

        # Africa-first logic
        if currency == "NGN":
            return "paystack"

        # Global cards
        if currency in ["USD", "EUR", "GBP", "CAD"]:
            return "stripe"

        # fallback global processor
        return "flutterwave"

    def charge(self, amount: float, currency: str, user: dict):
        provider_name = self.select_provider(currency, user.get("country"))

        provider = self.providers[provider_name]

        return provider.charge(amount=amount, currency=currency, user=user)
