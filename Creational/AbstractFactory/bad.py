from abc import ABC, abstractmethod

# Example of Payment gateway and invoicing

# Interfaces
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self) -> None:
        pass

# Payment GateWay Concrete Class
class RazorPayPG(PaymentGateway):
    def process_payment(self, amount:float) -> None:
        print(f"Processing INR payment via Razorpay: {amount}")

class PayUPG(PaymentGateway):
    def process_payment(self, amount:float) -> None:
        print(f"Processing USD payment via PayU: {amount}")

# Invoice Concrete Class
class IndiaInvoice(Invoice):
    def generate_invoice(self):
        print("Generating invoice for India")


# Checkout Service for payment and invoicing controls both business logic and object creation, this is why this is a bad approach
class CheckoutService:
    def __init__(self, gatewayType):
        self.gatewayType = gatewayType

    def checkout(self,amount: float) -> None:
        if(self.gatewayType == "RAZOR"):
            pgObject = RazorPayPG()
        else:
            pgObject = PayUPG()

        pgObject.process_payment(amount=amount)

        # Always uses IndiaInvoice, even though more types may exist later in the future
        invoice = IndiaInvoice()
        invoice.generate_invoice()


if __name__ == "__main__":
    razorpay_service = CheckoutService("razorpay")
    razorpay_service.checkout(1500.00) # bad thing as invoice would be generated for india in all the cases