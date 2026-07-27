from app.billing.providers.stripe import StripeProvider


provider = StripeProvider()


def create_checkout(payment):
    return provider.create_checkout(payment)