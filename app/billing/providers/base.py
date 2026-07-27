from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def create_checkout(self, payment):
        pass

    @abstractmethod
    def verify_webhook(self, payload, sig):
        pass