"""
================================================================================
LECTURE 08: input() Function in Python
LECTURE 09: Variables in Python & Memory Allocation
LECTURE 10: Coding Exercise #2 - Program to Swap Two Numbers
LECTURE 11: Variable Naming Rules & Keywords in Python
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. input() Function:
   - User se console par data input lene ke liye use hota hai.
   - Sabse important point: `input()` ALWAYS return karta hai STRING data type!
   - Agar number chahiye toh `int()` ya `float()` me typecast karna zaroori hai.

2. Variables in Python:
   - Python mein variables "containers" nahi balki memory objects ke "labels / references" hote hain.
   - `id()` function se variable ka memory address check kar sakte hain.

3. Variable Naming Rules (Identifiers):
   - Naam letter (a-z, A-Z) ya underscore (_) se shuru hona chahiye.
   - Number se start NAHI ho sakta (e.g. `1name` invalid hai).
   - Sirf alphanumeric characters aur underscores allowed hain (a-z, 0-9, _). Special symbols jaise @, $, % not allowed.
   - Case-Sensitive hote hain: `age`, `Age`, aur `AGE` teeno alag variables hain.
   - Python keywords (reserved words jaise if, for, while, class) ko variable name nahi bana sakte.

4. Pythonic Swap:
   - Python me swap karne ke liye 3rd variable ki zaroorat nahi padti: `a, b = b, a` (Tuple unpacking).
"""

# --- 1. input() Function Demo ---
# Example input (Hardcoded demo input to avoid blocking during automated runs):
user_name = "Jenny"  # user_name = input("Apna naam enter karo: ")
print("Hello " + user_name + "!")

# Input length calculate karna:
print("Naam ki length:", len(user_name))


# --- 2. Variables & Memory Reference Demo ---
a = 100
b = 100
# Python integer caching: chote integers (-5 to 256) same memory address share karte hain
print("Address of a:", id(a))
print("Address of b:", id(b))
print("Kya a aur b same memory point kar rahe hain?", a is b)  # True


# --- 3. LECTURE 11: Variable Naming Rules ---
# VALID Variable Names:
my_var = 10
_my_var = 20
myVar3 = 30
MY_CONSTANT = 3.14  # Constants convention: UPPERCASE

# INVALID Variable Names (Uncomment karne par SyntaxError aayega):
# 2var = 50       # Error: Digit se shuru nahi ho sakta
# my-var = 50     # Error: Hyphen not allowed
# my var = 50     # Error: Space not allowed
# for = 50        # Error: Reserved keyword

import keyword
print("Python me total keywords:", len(keyword.kwlist))
print("Keywords list (sample):", keyword.kwlist[:10])


# --- 4. LECTURE 10: Coding Exercise #2 - Swap Two Numbers ---
# Method 1: Using Third / Temporary Variable (Traditional Way)
x = 5
y = 10
print(f"\nBefore Swap (Method 1): x = {x}, y = {y}")

temp = x
x = y
y = temp
print(f"After Swap (Method 1): x = {x}, y = {y}")

# Method 2: Pythonic Way (Tuple Packing & Unpacking - Interview Favourite)
p = 20
q = 50
print(f"Before Swap (Method 2): p = {p}, q = {q}")
p, q = q, p  # Right side tuple banta hai (50, 20), left side unpack hota hai
print(f"After Swap (Method 2): p = {p}, q = {q}")

# Method 3: Without 3rd variable using Arithmetic Operators (+ and -)
m = 15
n = 35
m = m + n  # m = 50
n = m - n  # n = 50 - 35 = 15
m = m - n  # m = 50 - 15 = 35
print(f"After Swap (Method 3 - Math): m = {m}, n = {n}")
