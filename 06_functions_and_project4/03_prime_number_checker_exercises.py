"""
================================================================================
LECTURE 67: Coding Exercise #21 - Prime Number Checker (#lec63)
LECTURE 68: Coding Exercise #22 - Prime Checker Optimization (#lec64)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Prime Number kya hota hai?
   - Wo number jo 1 se bada ho (`n > 1`) aur jiske sirf 2 hi factors hon: 1 aur wo number khud.
   - Example: 2, 3, 5, 7, 11, 13, 17, 19...
   - Note: 1 prime number NAHI hota!
   - 2 akela aisa prime number hai jo EVEN bhi hai.

2. Brute Force vs Optimized Logic (Interview Standard):
   - Brute Force (O(n)): 2 se lekar `n - 1` tak check karo. Agar kisi se divide ho gaya toh Not Prime.
   - Optimized Method (O(sqrt(n))): Factors hamesha pairs me aate hain (e.g. for 36: 1x36, 2x18, 3x12, 4x9, 6x6).
     Isliye `2` se lekar `int(sqrt(n)) + 1` tak hi check karna kaafi hota hai!
"""

import math

# --- 1. Basic Prime Checker (Jenny's Lecture 63 implementation) ---
def is_prime_basic(num):
    if num <= 1:
        return False
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


# --- 2. Optimized Prime Checker (Lecture 64 - sqrt(n) optimization) ---
def is_prime_optimized(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False  # 2 ke alawa koi bhi even number prime nahi hota

    # Check only odd numbers up to sqrt(num)
    limit = int(math.isqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True


# --- Test Cases & Verification ---
test_numbers = [1, 2, 3, 4, 17, 25, 29, 36, 97, 100]

print("--- Prime Number Checker (Basic vs Optimized) ---")
for n in test_numbers:
    basic_res = is_prime_basic(n)
    opt_res = is_prime_optimized(n)
    status = "PRIME" if opt_res else "NOT PRIME"
    print(f"Number {n:3d} -> {status} (Verified: {basic_res == opt_res})")
