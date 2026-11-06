"""
================================================================================
LECTURE 92: Coding Exercise #26 - Circle Class (Area & Circumference) (#lec88)
Bonus OOP Exercise: BankAccount Class Implementation
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Circle Class Design:
   - Attribute: `radius` (Default value = 1.0)
   - Class Attribute: `pi = 3.14159`
   - Method 1: `get_circumference()` -> Formula: `2 * pi * radius`
   - Method 2: `get_area()` -> Formula: `pi * (radius ** 2)`

2. BankAccount Class Design:
   - Real-world encapsulation example:
   - Attributes: `account_holder`, `balance`
   - Methods: `deposit(amount)`, `withdraw(amount)`, `check_balance()`
   - Checks: Negative amounts not allowed, withdrawal amount cannot exceed current balance.
"""

import math

# --- LECTURE 92: Exercise #26 - Circle Class ---
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius=1.0):
        self.radius = radius

    def get_circumference(self):
        """Circumference = 2 * pi * r"""
        return 2 * Circle.pi * self.radius

    def get_area(self):
        """Area = pi * r^2"""
        return Circle.pi * (self.radius ** 2)


# --- Bonus OOP Real-World Practice: Bank Account Class ---
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account opened for {self.account_holder} with Initial Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"Deposited: ${amount:.2f} | New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print(f"Insufficient Funds! Attempted to withdraw ${amount:.2f}, but Balance is ${self.balance:.2f}")
            return False
        self.balance -= amount
        print(f"Withdrawn: ${amount:.2f} | Remaining Balance: ${self.balance:.2f}")
        return True

    def get_balance(self):
        return self.balance


# --- Verification & Testing ---
if __name__ == "__main__":
    print("--- Testing Exercise #26: Circle Class ---")
    c1 = Circle(radius=5)
    print(f"Circle Radius        : {c1.radius}")
    print(f"Circle Circumference : {c1.get_circumference():.2f}")
    print(f"Circle Area          : {c1.get_area():.2f}")

    c2 = Circle(radius=10)
    print(f"\nCircle 2 Radius     : {c2.radius}")
    print(f"Circle 2 Area       : {c2.get_area():.2f}")

    print("\n--- Testing BankAccount Class ---")
    acc = BankAccount("Sachin", 500.0)
    acc.deposit(250.0)
    acc.withdraw(100.0)
    acc.withdraw(1000.0)  # Should trigger Insufficient Funds
