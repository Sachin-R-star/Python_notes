"""
================================================================================
LECTURE 104: Access Modifiers in Python - Public, Protected & Private (#lec100)
LECTURE 105: Encapsulation & Getters / Setters (@property) (#lec101)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Encapsulation kya hai?
   - Data (attributes) aur unpar kaam karne wale methods ko ek single unit (class) me wrap karna aur direct unauthorized access se protect karna.
   - Example: Capsule ke andar medicine safe rehti hai.

2. Access Modifiers in Python:
   - Python mein C++/Java jaisa strict `private` keyword nahi hota. Python "Consenting Adults" philosophy par chalta hai.
   - A. Public: `name`
     * Kahin se bhi freely access aur modify ho sakta hai.
   - B. Protected (Single Underscore Convention): `_name`
     * Python syntax level par restrict nahi karta, lekin yeh developer convention hai ki is attribute ko sirf class aur uske subclasses me hi use kiya jaye.
   - C. Private (Double Underscore): `__name`
     * Class ke bahar direct access karne par `AttributeError` aayega.
     * **Name Mangling**: Python internally iska naam badal kar `_ClassName__attributeName` kar deta hai! (Interviewers check this!).

3. Getters & Setters (@property Decorator):
   - Private attributes ko securely read aur modify karne ke liye Pythonic tareeqa:
     * `@property`: Getter method banata hai (bina brackets `obj.age` ki tarah call hota hai).
     * `@attribute.setter`: Setter method banata hai (validation logic lagane ke liye, e.g. age cannot be negative).
     * `@attribute.deleter`: Deleter method banata hai.
"""

# --- 1. Access Modifiers & Name Mangling Demo ---
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public Attribute
        self._salary = salary      # Protected Attribute (Convention)
        self.__ssn = ssn          # Private Attribute (Name Mangled)

    def display_employee(self):
        # Class ke andar sabhi attributes accessible hain
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


# --- 2. Encapsulation with @property (Getters & Setters) ---
class BankCustomer:
    def __init__(self, name, age, balance):
        self.name = name
        self._age = age
        self.__balance = balance  # Strictly private

    # Getter for balance
    @property
    def balance(self):
        """Getter: Safely read private balance"""
        return self.__balance

    # Setter for balance (with validation)
    @balance.setter
    def balance(self, new_balance):
        """Setter: Ensures balance cannot be set to negative directly"""
        if new_balance < 0:
            raise ValueError("Balance cannot be negative! Transaction rejected.")
        self.__balance = new_balance
        print(f"Balance updated successfully to: ${self.__balance:.2f}")

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, val):
        if val < 18 or val > 120:
            raise ValueError("Age must be between 18 and 120!")
        self._age = val


# --- Verification Code ---
if __name__ == "__main__":
    print("--- 1. Testing Access Modifiers & Name Mangling ---")
    emp = Employee("Aman", 75000, "987-65-4321")
    print("Public attribute access      :", emp.name)
    print("Protected attribute access   :", emp._salary)  # Works, but against convention

    # Direct private attribute access fails:
    try:
        print(emp.__ssn)
    except AttributeError as e:
        print(f"Direct private access failed : {e}")

    # Name Mangling Demonstration:
    print("Accessing private via Mangling:", emp._Employee__ssn)  # Python's internal name

    print("\n--- 2. Testing @property Getters & Setters ---")
    cust = BankCustomer("Rahul", 26, 1500.0)

    # Reading balance via getter (looks like attribute access, but executes method)
    print(f"Current Balance: ${cust.balance:.2f}")

    # Updating balance via setter
    cust.balance = 2200.0
    print(f"New Balance    : ${cust.balance:.2f}")

    # Validation check:
    try:
        cust.balance = -500.0
    except ValueError as err:
        print(f"Validation Guard caught bad update: {err}")
