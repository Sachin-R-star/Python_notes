"""
================================================================================
LECTURE 41: Tuples in Python (#lec40)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Tuples kya hain?
   - Ordered collection of items, round brackets `()` me define hote hain.
   - IMMUTABLE hote hain: Ek baar tuple ban gaya toh uske elements change, add ya remove NAHI kiye ja sakte!
   - Duplicate elements allow karta hai.

2. Single Item Tuple Quirk (Interviewer's Favourite):
   - `t = (10)` integer ban jata hai, tuple nahi!
   - Tuple banane ke liye TRAILING COMMA lagana zaroori hai: `t = (10,)`.

3. Tuple Packing & Unpacking:
   - Packing: Multiple values ko bina brackets ya brackets me tuple banana: `t = 1, 2, 3`.
   - Unpacking: Tuple ke elements ko individual variables me extract karna: `a, b, c = t`.
   - Extended unpacking: `a, *b, c = (1, 2, 3, 4, 5)` (*b rest elements ki list le leta hai).

4. List vs Tuple (Top Interview Comparison):
   - List Mutable hai -> Slow & zyada memory leti hai.
   - Tuple Immutable hai -> Fast, lightweight, aur Dictionary KEYS ke roop me use ho sakti hai (hashable hoti hai).
"""

import sys

# --- 1. Tuple Creation & Single-Item Quirk ---
t1 = (1, 2, 3, 4, 5)
print("t1:", t1, "Type:", type(t1))

not_a_tuple = ("Jenny")
print("not_a_tuple type:", type(not_a_tuple))  # <class 'str'>

valid_single_tuple = ("Jenny",)
print("valid_single_tuple type:", type(valid_single_tuple))  # <class 'tuple'>


# --- 2. Immutability Demo ---
# t1[0] = 100  # TypeError: 'tuple' object does not support item assignment

# Mutable object inside a tuple:
# Tuple khud immutable hai, lekin agar uske andar koi mutable object (jaise list) hai, toh list modify ho sakti hai!
special_tuple = (1, 2, [10, 20])
special_tuple[2].append(30)
print("Tuple with mutable list modified:", special_tuple)


# --- 3. Tuple Packing & Unpacking ---
# Packing:
coordinates = 28.6139, 77.2090  # New Delhi (Lat, Long)
print("Packed tuple:", coordinates)

# Unpacking:
lat, long = coordinates
print(f"Latitude: {lat}, Longitude: {long}")

# Extended Unpacking with Asterisk (*):
scores = (95, 88, 76, 65, 54, 99)
first, second, *middle, last = scores
print(f"First: {first}, Second: {second}, Middle: {middle}, Last: {last}")


# --- 4. Tuple Methods ---
sample_tuple = (10, 20, 30, 20, 40, 20)
print("Count of 20:", sample_tuple.count(20))   # 3
print("Index of 30:", sample_tuple.index(30))   # 2


# --- 5. Memory & Performance Comparison (Interview Demo) ---
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
demo_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Size of list in bytes :", sys.getsizeof(demo_list))
print("Size of tuple in bytes:", sys.getsizeof(demo_tuple))  # Tuple uses significantly less memory!
