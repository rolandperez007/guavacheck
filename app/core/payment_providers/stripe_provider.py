class StripeProvider:
    def charge(self, amount, currency, user):
        return {
            "provider": "stripe",
            "status": "initialized",
            "amount": amount,
            "currency": currency,
            "user": user,
            "checkout_url": "https://stripe.com/pay/mock",
        }
