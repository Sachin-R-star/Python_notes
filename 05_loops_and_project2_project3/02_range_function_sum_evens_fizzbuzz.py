"""
================================================================================
LECTURE 50: range() Function in Python (#lec46)
LECTURE 51: Coding Exercise #16 - Sum of Even Numbers from 1 to 100 (#lec47)
LECTURE 52: Coding Exercise #17 - The Legendary FizzBuzz Problem (#lec48)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. range() Function:
   - Numbers ki arithmetic progression generate karta hai (Memory-efficient generator sequence).
   - Syntax: `range(start, stop, step)`
     * `start`: Default 0 (Inclusive).
     * `stop`: Zaroori parameter (EXCLUSIVE - stop value shamil nahi hoti!).
     * `step`: Default 1 (Kitne se increment ya decrement hoga).
   - Negative step: Reverse counting ke liye (`range(10, 0, -1)`).

2. Exercise #16 - Sum of Even Numbers (1 to 100):
   - Method 1: `range(2, 101, 2)` direct even numbers pe jump karke sum karna.
   - Method 2: Normal loop me `if num % 2 == 0` check karke sum karna.

3. Exercise #17 - The FizzBuzz Problem (Top 10 Most Asked Coding Interview Filter):
   - 1 se lekar n tak print karna hai.
   - Agar number 3 se divisible hai: Print "Fizz".
   - Agar number 5 se divisible hai: Print "Buzz".
   - Agar number 3 AUR 5 dono se divisible hai (yaani 15 se): Print "FizzBuzz".
   - Warna number khud print karo.
   - TRICK / TRAP: Pehle `num % 15 == 0` (3 and 5 dono) check karna ZAROORI hai! Agar pehle `num % 3 == 0` check kar loge, toh 15 par sirf "Fizz" print ho jayega aur galat ho jayega!
"""

# --- 1. range() Function Variations ---
print("range(5) (0 to 4)        :", list(range(5)))
print("range(1, 6) (1 to 5)     :", list(range(1, 6)))
print("range(1, 10, 2) (odds)   :", list(range(1, 10, 2)))
print("range(10, 0, -2) (rev)   :", list(range(10, 0, -2)))


# --- 2. LECTURE 51: Exercise #16 - Sum of Even Numbers (1 to 100) ---
# Method 1: Using range step parameter (O(n/2) steps)
total_even_1 = 0
for num in range(2, 101, 2):
    total_even_1 += num

# Method 2: Using modulo operator
total_even_2 = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_even_2 += num

# Method 3: Pythonic one-liner
total_even_3 = sum(range(2, 101, 2))

print(f"\n--- Exercise #16: Sum of Even Numbers (1 to 100) ---")
print(f"Method 1 (range step) : {total_even_1}")
print(f"Method 2 (if % 2 == 0): {total_even_2}")
print(f"Method 3 (sum())      : {total_even_3}")


# --- 3. LECTURE 52: Exercise #17 - FizzBuzz Problem ---
print("\n--- Exercise #17: FizzBuzz (First 20 numbers demo) ---")
for i in range(1, 21):
    # Rule 1: First check 3 AND 5 both (divisible by 15)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
print()
