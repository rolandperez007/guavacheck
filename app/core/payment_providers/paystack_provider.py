class PaystackProvider:
    def charge(self, amount, currency, user):
        return {
            "provider": "paystack",
            "status": "initialized",
            "amount": amount,
            "currency": currency,
            "user": user,
            "checkout_url": "https://paystack.co/checkout/mock",
        }
