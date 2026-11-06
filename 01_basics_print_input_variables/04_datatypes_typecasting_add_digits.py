"""
================================================================================
LECTURE 12: Data Types in Python (Primitive & Number Formats)
LECTURE 13: Type Checking (type()), Type Error & Type Casting (Conversion)
LECTURE 14: Coding Exercise #3 - Program to Add Digits of a Number
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Python Data Types:
   - Numeric: `int` (integers), `float` (decimals), `complex` (e.g. 2 + 3j).
   - Boolean: `bool` (`True` or `False` - internally True = 1, False = 0).
   - Sequence: `str` (String), `list`, `tuple`.
   - Set: `set`, `frozenset`.
   - Mapping: `dict`.

2. Number Systems:
   - Binary: `0b1010` (Prefix 0b/0B) -> 10
   - Octal: `0o12` (Prefix 0o/0O) -> 10
   - Hexadecimal: `0xA` (Prefix 0x/0X) -> 10

3. Type Casting (Type Conversion):
   - Implicit Conversion: Python automatically convert karta hai (e.g., int + float = float). Data loss nahi hota.
   - Explicit Conversion: Programmer manually function use karke convert karta hai (`int()`, `float()`, `str()`, `bool()`).

4. Boolean Truthy & Falsy Values (Interview Trap):
   - Falsy: `0`, `0.0`, `""` (empty string), `[]`, `()`, `{}`, `None`, `False`.
   - Baaki sab Truthy hain!
"""

# --- 1. Data Types & Number Systems ---
num_int = 42
num_float = 3.14159
num_complex = 3 + 5j
flag = True
message = "Python 2026"

print(f"num_int: {num_int}, Type: {type(num_int)}")
print(f"num_float: {num_float}, Type: {type(num_float)}")
print(f"num_complex: {num_complex}, Real: {num_complex.real}, Imag: {num_complex.imag}")
print(f"flag: {flag}, Type: {type(flag)}")

# Prefix representation:
binary_val = 0b1010  # 10
octal_val = 0o12     # 10
hex_val = 0xA        # 10
print(f"Binary 0b1010: {binary_val}, Octal 0o12: {octal_val}, Hex 0xA: {hex_val}")


# --- 2. Type Checking & Type Error ---
val = "123"
print("Type checking using type():", type(val))
print("Type checking using isinstance():", isinstance(val, str))  # Recommended in production

# Type Error Demo:
# result = "50" + 20  # TypeError: can only concatenate str (not "int") to str


# --- 3. Implicit vs Explicit Type Conversion ---
# Implicit:
n1 = 10     # int
n2 = 5.5    # float
res = n1 + n2  # float ban gaya automatically
print(f"Implicit conversion result: {res}, Type: {type(res)}")

# Explicit:
age_str = "25"
age_int = int(age_str)
print(f"Explicit str to int: {age_int + 5}")

# String representation of float to int direct nahi hota:
# int("3.14") -> ValueError
# Solution: Pehle float mein convert karo, fir int
print("Float string to int:", int(float("3.14")))

# Truthy & Falsy Examples:
print("bool(0):", bool(0))        # False
print("bool(''):", bool(""))      # False
print("bool('False'):", bool("False"))  # True! Non-empty string is always True!


# --- 4. LECTURE 14: Coding Exercise #3 - Add Digits of a Number ---
# Task: Take a two digit number (e.g. 54) and output sum of digits (5 + 4 = 9)

# Method 1: String Indexing Approach (Jenny's lecture approach)
num_input = "54"  # Simulating user input
first_digit = int(num_input[0])
second_digit = int(num_input[1])
sum_of_digits = first_digit + second_digit
print(f"\nExercise #3 (String method): Digits of {num_input} sum = {sum_of_digits}")

# Method 2: Mathematical Approach (Universal for any integer - Best for interviews)
number = 54
digit1 = number // 10   # 54 // 10 = 5 (Quotient / Tens place)
digit2 = number % 10    # 54 % 10 = 4 (Remainder / Units place)
print(f"Exercise #3 (Math method): {digit1} + {digit2} = {digit1 + digit2}")
