"""
================================================================================
LECTURE 42: Sets in Python - Introduction & Uniqueness (#lec41 Part 1)
LECTURE 43: Sets Methods - Add, Update, Remove, Discard (#lec41 Part 2)
LECTURE 44: Sets Operations - Union, Intersection, Difference (#lec41 Part 3)
LECTURE 45: Sets Operations - Disjoint, Subset, Superset, Frozenset (#lec41 Part 4)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Sets kya hote hain?
   - Curly braces `{}` me define hote hain.
   - UNORDERED: Elements ka koi fixed order nahi hota (indexing ya slicing allowed nahi hai!).
   - UNIQUE: Duplicate elements automatically remove ho jaate hain.
   - Mutable collection hai, lekin elements khud immutable (hashable) hone chahiye (list ya dict set ke andar nahi aa sakti).

2. Empty Set Quirk (Common Trap):
   - `s = {}` se empty SET nahi banta, empty DICT banta hai!
   - Empty set banane ke liye `s = set()` use karte hain.

3. remove() vs discard() (Interview Hot Question):
   - `remove(x)`: Agar x set me nahi hai toh `KeyError` throw karta hai!
   - `discard(x)`: Agar x set me nahi hai toh koi error nahi deta (Safely ignore karta hai).

4. Mathematical Set Operations:
   - Union (`|` ya `union()`): Dono sets ke sabhi unique elements.
   - Intersection (`&` ya `intersection()`): Dono sets ke common elements.
   - Difference (`-` ya `difference()`): Set A ke wo elements jo Set B me nahi hain.
   - Symmetric Difference (`^` ya `symmetric_difference()`): Wo elements jo ya toh A me hain ya B me, par dono ke common NAHI hain.

5. frozenset:
   - Immutable version of set. Ek baar ban gaya to modify nahi ho sakta. Dict key ban sakta hai.
"""

# --- 1. Set Creation & Uniqueness ---
my_set = {1, 2, 3, 2, 1, 4, 5, 5}
print("Original set (duplicates removed automatically):", my_set)

# Empty set trap:
empty_dict = {}
print("type of {}:", type(empty_dict))  # <class 'dict'>

empty_set = set()
print("type of set():", type(empty_set))  # <class 'set'>


# --- 2. Add, Update, Remove, Discard, Pop ---
s = {10, 20, 30}
s.add(40)                  # Single element add karta hai
s.update([50, 60, 20])     # Multiple elements add karta hai
print("After add and update:", s)

# remove vs discard demo:
s.discard(999)             # 999 set me nahi hai, fir bhi koi error nahi
print("s.discard(999) passed safely.")

# s.remove(999)            # Uncomment karne par KeyError aayega!

popped = s.pop()           # Random element pop hota hai (Sets are unordered)
print(f"Popped element: {popped}, Remaining set: {s}")


# --- 3. Set Operations (Union, Intersection, Difference, Symmetric Diff) ---
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\n--- Mathematical Set Operations ---")
print("Set A:", set_a)
print("Set B:", set_b)

# Union (All unique):
print("Union (A | B)                    :", set_a | set_b)

# Intersection (Common elements):
print("Intersection (A & B)             :", set_a & set_b)

# Difference (Only in A):
print("Difference (A - B)               :", set_a - set_b)

# Symmetric Difference (In A or B, but NOT both):
print("Symmetric Difference (A ^ B)     :", set_a ^ set_b)


# --- 4. Disjoint, Subset, Superset ---
x = {1, 2}
y = {1, 2, 3, 4}
z = {5, 6}

print("\n--- Relationship Checks ---")
print("x is subset of y? (x.issubset(y))          :", x.issubset(y))      # True
print("y is superset of x? (y.issuperset(x))      :", y.issuperset(x))    # True
print("x and z are disjoint? (No common elements) :", x.isdisjoint(z))    # True


# --- 5. frozenset Demo ---
fs = frozenset([1, 2, 3, 4])
print("\nfrozenset:", fs, "Type:", type(fs))
# fs.add(5) -> AttributeError: 'frozenset' object has no attribute 'add'
# frozenset can be used as a key in dictionary:
dict_with_set_key = {fs: "Immutable set as dict key works!"}
print("Dict with frozenset key:", dict_with_set_key)
