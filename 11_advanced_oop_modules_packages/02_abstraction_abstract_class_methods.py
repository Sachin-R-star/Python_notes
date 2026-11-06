"""
================================================================================
LECTURE 102: Abstraction in Python - OOP Concept (#lec98)
LECTURE 103: Abstract Classes & Abstract Methods in Python (#lec99)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Abstraction kya hai?
   - Internal complex implementation details ko chupana aur user ko sirf essential features/interface provide karna.
   - Real-world example: Car ka accelerator dabane par car tez bhagti hai, par internal combustion engine aur fuel injection ka complex mechanism driver se hidden rehta hai.

2. Abstract Class & Abstract Method in Python:
   - Python by default abstract classes provide nahi karta; iske liye built-in module `abc` (Abstract Base Classes) use karna padta hai:
     `from abc import ABC, abstractmethod`
   - Abstract Class: Wo class jo `ABC` se inherit karti hai aur jisme kam se kam ek `@abstractmethod` hota hai.
   - RULE 1: Abstract class ka DIRECT OBJECT (INSTANCE) NAHI banaya ja sakta! (`TypeError` aayega).
   - RULE 2: Agar kisi Child class ne Parent ke sabhi abstract methods ko override (implement) nahi kiya, toh Child class ka bhi object nahi ban sakta!
   - Partial Abstraction: Abstract class me abstract methods ke saath-saath regular (concrete) methods bhi ho sakte hain.
"""

from abc import ABC, abstractmethod

# --- Abstract Base Class ---
class PaymentGateway(ABC):
    def __init__(self, merchant_name):
        self.merchant_name = merchant_name

    # Concrete Method (Shared implementation)
    def print_receipt(self, transaction_id, amount):
        print(f"[{self.merchant_name}] Receipt #{transaction_id}: Paid ${amount:.2f} successfully.")

    # Abstract Method (Child classes MUST implement this)
    @abstractmethod
    def process_payment(self, amount):
        """Every payment provider must implement its own payment mechanism"""
        pass

    @abstractmethod
    def refund(self, transaction_id, amount):
        """Every payment provider must implement its own refund mechanism"""
        pass


# --- Concrete Child Class 1: PayPal ---
class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount:.2f} via PayPal API with buyer protection...")
        return "TXN_PAYPAL_9876"

    def refund(self, transaction_id, amount):
        print(f"Refunding ${amount:.2f} back to PayPal wallet for {transaction_id}...")


# --- Concrete Child Class 2: Stripe / Credit Card ---
class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount:.2f} via Stripe Credit Card gateway...")
        return "TXN_STRIPE_1234"

    def refund(self, transaction_id, amount):
        print(f"Refunding ${amount:.2f} back to Credit Card for {transaction_id}...")


# --- Verification & Interview Tests ---
if __name__ == "__main__":
    print("==========================================")
    print("      ABSTRACTION IN PYTHON (abc MODULE)  ")
    print("==========================================")

    # 1. Test Abstract Class Instantiation (Should Fail)
    try:
        # Abstract class ka direct instance banane ki koshish:
        bad_obj = PaymentGateway("Generic Store")
    except TypeError as e:
        print(f"Test 1 Passed: Cannot instantiate abstract class directly!\nError: {e}\n")

    # 2. Test Concrete Implementations
    paypal = PayPal("Amazon Store")
    txn1 = paypal.process_payment(150.0)
    paypal.print_receipt(txn1, 150.0)
    paypal.refund(txn1, 50.0)

    print()
    stripe = Stripe("Flipkart Store")
    txn2 = stripe.process_payment(300.0)
    stripe.print_receipt(txn2, 300.0)
    stripe.refund(txn2, 300.0)
