class FlutterwaveProvider:
    def charge(self, amount, currency, user):
        return {
            "provider": "flutterwave",
            "status": "initialized",
            "amount": amount,
            "currency": currency,
            "user": user,
            "checkout_url": "https://flutterwave.com/pay/mock",
        }
