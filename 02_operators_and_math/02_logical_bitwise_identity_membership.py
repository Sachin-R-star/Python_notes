"""
================================================================================
LECTURE 17: Logical Operators (and, or, not) (#lec16)
LECTURE 18: Bitwise Operators (&, |, ^, ~, <<, >>) (#lec17)
LECTURE 19: Identity Operators (is, is not) (#lec18)
LECTURE 20: Membership Operators (in, not in) (#lec19)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Logical Operators:
   - `and`: Dono true honge tabhi True dega.
   - `or`: Dono me se koi ek bhi true ho toh True dega.
   - `not`: True ko False aur False ko True bana deta hai.
   - Short-Circuit Evaluation:
     * `A and B`: Agar A False hai toh Python B ko check hi nahi karta (Direct False).
     * `A or B`: Agar A True hai toh Python B ko check hi nahi karta (Direct True).

2. Bitwise Operators (Operate on binary bits 0 & 1):
   - `&` (Bitwise AND): Dono bits 1 honge toh 1, warna 0.
   - `|` (Bitwise OR): Koi ek bit 1 hogi toh 1, warna 0.
   - `^` (Bitwise XOR): Different bits pe 1, Same bits pe 0.
   - `~` (Bitwise NOT): Inverts bits (~x = -(x + 1)). e.g., ~5 = -6.
   - `<<` (Bitwise Left Shift): Bits ko left shift karta hai (`a << n` approx equals `a * (2^n)`).
   - `>>` (Bitwise Right Shift): Bits ko right shift karta hai (`a >> n` approx equals `a // (2^n)`).

3. Identity Operators (`is`, `is not`):
   - Check karta hai ki kya dono variables SAME MEMORY LOCATION (same object id) ko point kar rahe hain.
   - Interview Question: `==` vs `is`
     * `==`: Values / Content compare karta hai.
     * `is`: Memory address (identity / id()) compare karta hai.

4. Membership Operators (`in`, `not in`):
   - Check karta hai ki koi element kisi sequence (string, list, tuple, set, dict) me maujood hai ya nahi.
"""

# --- 1. Logical Operators & Short Circuit ---
a = 10
b = 20

print("a > 5 and b > 15:", a > 5 and b > 15)  # True
print("a > 15 or b > 15 :", a > 15 or b > 15)   # True
print("not(a == 10)     :", not(a == 10))        # False

# Short-circuiting demo:
# Agar pehla expression True hai to 'or' me aage ka code evaluate nahi hota
def check_func():
    print("Function called!")
    return True

print("Short-circuit OR demo:")
res = True or check_func()  # function call nahi hoga!


# --- 2. Bitwise Operators Demo ---
x = 5  # Binary: 0101
y = 4  # Binary: 0100

print(f"x & y (5 & 4)   : {x & y}")    # 0101 & 0100 = 0100 (4)
print(f"x | y (5 | 4)   : {x | y}")    # 0101 | 0100 = 0101 (5)
print(f"x ^ y (5 ^ 4)   : {x ^ y}")    # 0101 ^ 0100 = 0001 (1)
print(f"~x (~5)         : {~x}")       # Formula: -(5+1) = -6
print(f"x << 2 (5 << 2) : {x << 2}")   # 5 * 2^2 = 20
print(f"x >> 1 (5 >> 1) : {x >> 1}")   # 5 // 2^1 = 2


# --- 3. Identity Operators (is vs ==) - INTERVIEW HOT TOPIC ---
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2)  # True (Values barabar hain)
print("list1 is list2 :", list1 is list2)  # False (Memory address alag hain)
print("list1 is list3 :", list1 is list3)  # True (Same object reference hai)
print("id(list1):", id(list1))
print("id(list2):", id(list2))
print("id(list3):", id(list3))


# --- 4. Membership Operators (in, not in) ---
msg = "Welcome to Jenny's Python Course"
numbers = [10, 20, 30, 40]

print("'Jenny' in msg       :", "Jenny" in msg)          # True
print("'Java' not in msg     :", "Java" not in msg)        # True
print("20 in numbers         :", 20 in numbers)            # True
print("50 not in numbers     :", 50 not in numbers)        # True

# Dict me membership hamesha KEYS par check hoti hai:
student = {"name": "Aman", "age": 22}
print("'name' in student     :", "name" in student)        # True
print("'Aman' in student     :", "Aman" in student)        # False (Kyunki 'Aman' value hai, key nahi)
print("'Aman' in student.values():", "Aman" in student.values())  # True
