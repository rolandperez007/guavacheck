import stripe

from app.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeProvider:

    def create_checkout(self, payment):

        session = stripe.checkout.Session.create(

            payment_method_types=["card"],

            mode="payment",

            line_items=[
                {
                    "price_data": {

                        "currency": payment.currency,

                        "product_data": {
                            "name": payment.description
                        },

                        "unit_amount": payment.amount,
                    },

                    "quantity": 1,
                }
            ],

            success_url=f"{settings.FRONTEND_URL}/payment/success",

            cancel_url=f"{settings.FRONTEND_URL}/payment/cancel",
        )

        return {
            "session_id": session.id,
            "checkout_url": session.url,
        }

    def verify_webhook(self, payload, signature):

        return stripe.Webhook.construct_event(
            payload,
            signature,
            settings.STRIPE_WEBHOOK_SECRET,
        )