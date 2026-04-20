from abc import ABC, abstractmethod

# Interfaces
class PaymentGateWay(ABC):
    def process_payment(self,amount: float) -> None:
        pass

class Invoice(ABC):
    def generate_invoice(self) -> None:
        pass


# India Implementation of these interfaces
class RazorpayPG(PaymentGateWay):
    def process_payment(self, amount) -> None:
        print(f"Processing payment of amount {amount} INR using Razorpay")

class CashFreePG(PaymentGateWay):
    def process_payment(self, amount) -> None:
        print(f"Processing payment of amount {amount} INR using Cashfree")

class IndiaInvoice(Invoice):
    def generate_invoice(self):
        print("Generating invoice for India with GST")

# US Implementation of these interfaces
class PayUPG(PaymentGateWay):
    def process_payment(self, amount) -> None:
        print(f"Processing payment of amount {amount} USD using PayU")

class StripePG(PaymentGateWay):
    def process_payment(self, amount) -> None:
        print(f"Processing payment of amount {amount} USD using Stripe")

class USInvoice(Invoice):
    def generate_invoice(self):
        print("Generating invoice for US with VAT")

# Abstract Factory
class RegionFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self, gatewayType: str) -> PaymentGateWay:
        pass

    @abstractmethod
    def create_invoice(self) -> Invoice:
        pass

# Concrete Factories
class IndiaFactory(RegionFactory):
    def create_payment_gateway(self, gatewayType: str) -> PaymentGateWay:
        print(f"Will return the payment gateway object for India: {gatewayType}")
        if gatewayType.lower() == "razor":
            return RazorpayPG()
        elif gatewayType.lower() == "cashfree":
            return CashFreePG()
        else:
            raise ValueError(f"Unsupported gateway for India: {gatewayType}")
        
    def create_invoice(self) -> Invoice:
        return IndiaInvoice()
        
class USFactory(RegionFactory):
    def create_payment_gateway(self, gatewayType: str) -> PaymentGateWay:
        print(f"Will return the payment gateway object for US: {gatewayType}")
        if gatewayType.lower() == "payu":
            return PayUPG()
        elif gatewayType.lower() == "stripe":
            return StripePG()
        else:
            raise ValueError(f"Unsupported gateway for US: {gatewayType}")
        
    def create_invoice(self) -> Invoice:
        return USInvoice()
    

class CheckoutService:
    def __init__(self,region: RegionFactory,gatewayType: str):
        self.paymentGateway = region.create_payment_gateway(gatewayType=gatewayType)
        self.invoice = region.create_invoice()

    def checkout(self,amount: float) -> None:
        self.paymentGateway.process_payment(amount=amount)
        self.invoice.generate_invoice()

if __name__ == "__main__":
    # Supported indian PG
    india_checkout = CheckoutService(IndiaFactory(),"razor")
    india_checkout.checkout(1500)

    india_checkout2 = CheckoutService(IndiaFactory(),"cashfree")
    india_checkout2.checkout(1500)

    # Supported american PG
    us_checkout = CheckoutService(USFactory(),"payu")
    us_checkout.checkout(100)

    us_checkout2 = CheckoutService(USFactory(),"stripe")
    us_checkout2.checkout(200)

    # Unsupported PG
    # india_checkout3 = CheckoutService(IndiaFactory(),"random")
    # india_checkout3.checkout(2000)