"""
================================================================================
LECTURE 64: Functions with Arguments (Parameters vs Arguments) (#lec60)
LECTURE 65: Types of Arguments - Positional, Keyword & Default (#lec61)
LECTURE 66: *args & **kwargs in Python (Variable Length Arguments) (#lec62)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Parameter vs Argument (Common Interview Distinction):
   - Parameter: Wo variable jo function DEFINITION ke header me likha hota hai (e.g., `def add(a, b):`).
   - Argument: Wo actual value jo function CALL karte waqt pass ki jaati hai (e.g., `add(5, 10)`).

2. Argument Types:
   - Positional Arguments: Arguments ki position/order match hoti hai. Order galat toh data galat.
   - Keyword Arguments: Argument ka naam explicitly mention karte hain (`func(name="Jenny", age=25)`). Order aage-peeche ho sakti hai.
   - Default Arguments: Parameter ko default value di jati hai. Agar caller koi value na de, toh default use hogi.
     * RULE: Non-default parameters HAMESHA default parameters ke pehle aane chahiye (`def func(a, b=10):` valid hai, `def func(a=10, b):` SyntaxError hai).

3. *args & **kwargs (Arbitrary / Variable-Length Arguments):
   - `*args` (Non-Keyword Arbitrary Arguments):
     * Kitne bhi positional arguments pass karo, yeh unhe ek **TUPLE** me pack kar leta hai.
   - `**kwargs` (Keyword Arbitrary Arguments):
     * Kitne bhi keyword arguments (`key=value`) pass karo, yeh unhe ek **DICTIONARY** me pack kar leta hai.

4. Function Definition Order Rule:
   `standard_arg -> *args -> keyword_only -> **kwargs`
"""

# --- 1. Positional vs Keyword Arguments ---
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional (Order matters):
describe_pet("Dog", "Tommy")

# Keyword (Order does not matter):
describe_pet(pet_name="Bruno", animal_type="Labrador")


# --- 2. Default Arguments ---
def greet_person(name, greeting="Good Morning"):
    print(f"{greeting}, {name}!")

greet_person("Rahul")                     # Default greeting use karega
greet_person("Sneha", "Happy New Year")   # Overrides default greeting


# --- 3. *args (Variable Length Positional Arguments -> Tuple) ---
def sum_all(*numbers):
    print(f"*args received as: {type(numbers)} -> {numbers}")
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum of 3 numbers :", sum_all(10, 20, 30))
print("Sum of 5 numbers :", sum_all(1, 2, 3, 4, 5))


# --- 4. **kwargs (Variable Length Keyword Arguments -> Dict) ---
def display_student_info(name, **details):
    print(f"\nStudent Name: {name}")
    print(f"**kwargs received as: {type(details)} -> {details}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")

display_student_info("Aman", age=21, branch="CSE", cgpa=9.2, city="Delhi")


# --- 5. Combining All Types in One Function (Interview Master Template) ---
def master_function(pos, default_val="Default", *args, kw_only=100, **kwargs):
    print("\n--- Master Function Args Demo ---")
    print("pos        :", pos)
    print("default_val:", default_val)
    print("args       :", args)
    print("kw_only    :", kw_only)
    print("kwargs     :", kwargs)

master_function(1, "CustomDefault", 2, 3, 4, kw_only=500, user="Jenny", course="Python")
