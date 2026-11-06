"""
================================================================================
LECTURE 60: Functions in Python - Introduction (#lec56)
LECTURE 61: Coding Exercise #18 - Simple Function (#lec57)
LECTURE 62: Coding Exercise #19 - Function Practice (#lec58)
LECTURE 63: Coding Exercise #20 - Paint Area / Can Calculator (#lec59)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Functions kya hote hain?
   - Reusable block of code jo tabhi execute hota hai jab use CALL (invoke) kiya jaye.
   - Code redundancy (duplication) ko khatam karta hai (DRY Principle - Don't Repeat Yourself).
   - Syntax:
     `def function_name():`
         `# code body`
     `function_name()`  # Calling function

2. Exercise #20 - Paint Area Calculator Problem:
   - Instructions: Ek wall ko paint karna hai.
   - 1 can of paint 7 square meters cover karta hai (Coverage = 7).
   - Wall ki height aur width di hai.
   - Number of cans = (Height * Width) / Coverage
   - IMP TRICK: Paint cans fractional nahi khareed sakte! E.g. agar 2.3 cans aaye toh shopkeeper se 3 cans lene padenge!
   - Isliye `math.ceil()` (Ceiling function) use karna zaroori hai.
"""

import math

# --- 1. LECTURE 60 & 61: Basic Function Definition & Calling ---
def greet():
    print("Namaste! Welcome to Python Functions.")

greet()  # Function calling


# --- 2. LECTURE 62: Function with Simple Logic ---
def welcome_user(name):
    print(f"Hello {name}, welcome to Jenny's Python Course!")

welcome_user("Sachin")


# --- 3. LECTURE 63: Exercise #20 - Paint Can Calculator ---
def paint_calc(height, width, cover=7):
    # Area of wall
    area = height * width
    # Fractional cans round UP to nearest integer
    num_of_cans = math.ceil(area / cover)
    print(f"\n--- Exercise #20: Paint Can Calculator ---")
    print(f"Wall Dimensions : {height}m height x {width}m width")
    print(f"Total Area      : {area} sq meters")
    print(f"Coverage per can: {cover} sq meters")
    print(f"You will need {num_of_cans} cans of paint.")
    return num_of_cans

# Test run: Height = 3m, Width = 9m -> Area = 27 -> 27 / 7 = 3.85 -> 4 cans
paint_calc(height=3, width=9, cover=7)
