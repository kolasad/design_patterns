

class PaymentService:
    def pay(self, amount):
        pass


class DeliveryService:
    def deliver(self, address):
        pass


class OrderFacade:
    def __init__(self, delivery_service, payment_service):
        self._delivery_service = delivery_service
        self._payment_service = payment_service

    def place_order(self, amount, address):
        self._payment_service.pay(amount)
        self._delivery_service.deliver(address)


class Facade:
    def __init__(self, delivery_service, payment_service):
        self._delivery_service = delivery_service
        self._payment_service = payment_service

    def pay_with_default_payment_service(self, amount):
        self._payment_service.pay(amount)

    def deliver_with_default_delivery_service(self, address):
        self._delivery_service.deliver(address)
