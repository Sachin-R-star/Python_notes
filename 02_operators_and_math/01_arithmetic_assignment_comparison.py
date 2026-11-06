"""
================================================================================
LECTURE 15: Arithmetic Operators in Python (#lec14)
LECTURE 16: Assignment and Comparison Operators (#lec15)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Arithmetic Operators:
   - `+` Addition, `-` Subtraction, `*` Multiplication
   - `/` Normal Division: ALWAYS returns `float` (e.g. 4/2 = 2.0).
   - `//` Floor Division: Decimals ko drop karke integer deta hai (downward rounding). e.g., 5 // 2 = 2, -5 // 2 = -3!
   - `%` Modulo: Division ka remainder deta hai (e.g. 5 % 2 = 1).
   - `**` Exponent / Power: `2 ** 3` matlab 2^3 = 8.

2. Operator Precedence (BODMAS / PEMDAS):
   - () Parentheses (Highest priority)
   - ** Exponent (Right-to-Left associativity: 2**3**2 = 2**(3**2) = 512, NOT 64!)
   - *, /, //, % (Left-to-Right)
   - +, - (Left-to-Right)

3. Assignment Operators:
   - `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
   - `a += 5` ka matlab hota hai `a = a + 5`.

4. Comparison / Relational Operators:
   - `==` Equal to, `!=` Not equal to
   - `>`, `<`, `>=`, `<=`
   - Output hamesha `True` ya `False` (boolean) hota hai.
   - Chained comparison support karta hai: `1 < x < 10` is valid in Python!
"""

# --- 1. Arithmetic Operators Demo ---
a = 15
b = 4

print("a + b =", a + b)       # 19
print("a - b =", a - b)       # 11
print("a * b =", a * b)       # 60
print("a / b =", a / b)       # 3.75 (Always float)
print("a // b =", a // b)     # 3 (Floor division - integer part)
print("a % b =", a % b)       # 3 (Remainder)
print("a ** b =", a ** b)     # 15^4 = 50625

# Negative Floor Division (Interview Trap):
# -5 // 2 gives -3, NOT -2 (hamesha smaller integer ki taraf round hota hai)
print("-5 // 2 =", -5 // 2)

# Exponent Right-to-Left Associativity:
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)  # Evaluates 3**2=9 first, then 2**9 = 512


# --- 2. Assignment Operators Demo ---
x = 10
x += 5     # x = x + 5 = 15
x *= 2     # x = x * 2 = 30
x //= 4    # x = x // 4 = 7
print("Final value of x after compound assignments:", x)


# --- 3. Comparison / Relational Operators Demo ---
p = 20
q = 30

print("p == q:", p == q)   # False
print("p != q:", p != q)   # True
print("p < q :", p < q)    # True
print("p >= q:", p >= q)   # False

# Chained Comparison (Python Exclusive Feature):
age = 22
print("18 <= age <= 60 (Chained comparison):", 18 <= age <= 60)  # True
# Baaki languages me `age >= 18 && age <= 60` likhna padta hai
