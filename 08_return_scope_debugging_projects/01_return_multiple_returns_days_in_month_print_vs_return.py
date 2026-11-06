"""
================================================================================
LECTURE 77: Functions with Return Statement (#lec73)
LECTURE 78: Return Multiple Values & Multiple Return Statements (#lec74)
LECTURE 79: Coding Exercise #25 - Days in Month (with Leap Year) (#lec75)
LECTURE 80: print() vs return in Python - Complete Difference (#lec76)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. return Statement:
   - Function ka execution terminate karta hai aur result ko CALLER ke paas wapas bhejta hai.
   - Code execution jaise hi `return` par aata hai, function turant exit ho jata hai. Uske neeche ka code execute nahi hota.
   - Agar kisi function me explicit `return` na ho, toh Python by default `None` return karta hai.

2. Multiple Return Values:
   - Python multiple values return karne ki capability deta hai: `return a, b, c`.
   - Python internally inhe ek **TUPLE** bana kar return karta hai!
   - Caller side par ise direct unpack kiya ja sakta hai: `x, y, z = func()`.

3. print() vs return (Very Common Fresher Confusion):
   - `print()`: Sirf console/screen par user ko display karta hai. Value ko memory me store karke aage use nahi kar sakte.
   - `return`: Value ko caller variable ko deliver karta hai taaki aage calculations me use ho sake.

4. Exercise #25 - Days in Month:
   - List of month days: `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.
   - Agar month == 2 (February) hai AUR year leap year hai, toh 29 return karega, warna 28.
"""

# --- 1. Basic return vs Default None ---
def add(a, b):
    return a + b

def no_return_func():
    x = 10  # No return statement

result = add(5, 7)
default_val = no_return_func()

print("Result of add(5, 7)   :", result)       # 12
print("no_return_func returns:", default_val)  # None


# --- 2. Multiple Return Values (Tuple Packaging) ---
def get_user_stats():
    name = "Jenny"
    age = 28
    score = 99.5
    return name, age, score  # Returns tuple: ("Jenny", 28, 99.5)

stats = get_user_stats()
print("\nStats returned as tuple:", stats, "Type:", type(stats))

# Unpacking multiple return values:
user_name, user_age, user_score = get_user_stats()
print(f"Unpacked -> Name: {user_name}, Age: {user_age}, Score: {user_score}")


# --- 3. Multiple Return Statements (Early Exit) ---
def format_name(first, last):
    # Guard clauses (Early exit)
    if not first or not last:
        return "Invalid input: Name cannot be empty!"
    return f"{first.title()} {last.title()}"

print(format_name("rahul", "sharma"))
print(format_name("", "verma"))


# --- 4. LECTURE 79: Exercise #25 - Days in Month (with Leap Year) ---
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return "Invalid month index! Must be between 1 and 12."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]

print("\n--- Exercise #25: Days in Month ---")
print(f"Feb 2024 (Leap Year)     : {days_in_month(2024, 2)} days")
print(f"Feb 2023 (Non-Leap Year) : {days_in_month(2023, 2)} days")
print(f"July 2024                : {days_in_month(2024, 7)} days")
