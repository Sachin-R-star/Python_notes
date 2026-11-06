"""
================================================================================
LECTURE 33: Lists in Python & List Functions / Methods (#P_32)
LECTURE 34: Random Module in Python (#P_33)
LECTURE 35: Coding Exercise #11 - Heads or Tails (#P_34)
LECTURE 36: Coding Exercise #12 - Banker Roulette (Who will pay bill) (#lec35)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Lists in Python:
   - Ordered, Mutable (changeable), and allows duplicate elements.
   - Square brackets `[]` me define hoti hain. Heterogeneous data (int, str, float, etc.) store kar sakti hain.
   - Positive Indexing: `0` se start hoti hai (Left to Right).
   - Negative Indexing: `-1` se start hoti hai (Right to Left - last element is `-1`).
   - Slicing: `list[start:stop:step]` (stop index exclude hota hai).

2. Important List Methods:
   - `append(x)`: List ke end me ek element add karta hai.
   - `insert(index, x)`: Specified index par element insert karta hai.
   - `extend(iterable)`: Doosri list ke sabhi elements ko unpack karke add karta hai.
   - `remove(x)`: Pehla occurrence match hone par remove karta hai.
   - `pop(index)`: Specified index (default last) ka element nikal kar return karta hai.
   - `sort()`: In-place ascending order sort karta hai (`sort(reverse=True)` for descending).
   - `reverse()`: List ke elements ko ulta kar deta hai.
   - `count(x)`: Batata hai x kitni baar list me aaya hai.

3. random Module:
   - Pseudo-random number generator.
   - `random.randint(a, b)`: a aur b dono inclusive integer return karta hai.
   - `random.random()`: 0.0 aur 1.0 ke beech float return karta hai [0.0, 1.0).
   - `random.choice(seq)`: Sequence me se ek random element chunta hai.
   - `random.shuffle(list)`: List ko in-place shuffle kar deta hai.
"""

import random

# --- 1. List Basics, Indexing & Slicing ---
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

print("Original fruits list:", fruits)
print("First fruit (index 0) :", fruits[0])
print("Last fruit (index -1) :", fruits[-1])
print("Slicing [1:4]         :", fruits[1:4])       # Banana, Cherry, Mango
print("Reversed via slicing  :", fruits[::-1])

# Lists are mutable (modify in-place):
fruits[1] = "Blueberry"
print("After modification    :", fruits)


# --- 2. List Methods Demo ---
numbers = [10, 20, 30]

numbers.append(40)              # [10, 20, 30, 40]
numbers.insert(1, 15)           # [10, 15, 20, 30, 40]
numbers.extend([50, 60])        # [10, 15, 20, 30, 40, 50, 60]
print("After append, insert, extend:", numbers)

popped_item = numbers.pop()     # 60 removed and returned
print("Popped item:", popped_item)
numbers.remove(15)              # Removes 15
print("After removing 15:", numbers)

unsorted_nums = [45, 12, 89, 23, 7]
unsorted_nums.sort()            # In-place ascending sort
print("Sorted list:", unsorted_nums)
unsorted_nums.reverse()         # In-place reverse
print("Reversed list:", unsorted_nums)


# --- 3. LECTURE 34 & 35: Random Module & Exercise #11 - Heads or Tails ---
# random.randint(0, 1) -> 1: Heads, 0: Tails
coin_toss = random.randint(0, 1)

print("\n--- Exercise #11: Heads or Tails ---")
if coin_toss == 1:
    print(f"Coin Toss Result: {coin_toss} -> Heads!")
else:
    print(f"Coin Toss Result: {coin_toss} -> Tails!")


# --- 4. LECTURE 36: Exercise #12 - Banker Roulette ---
# Task: Group of friends me se ek random person bill pay karega.
names_str = "Angela, Ben, Jenny, Michael, Chloe"
names = names_str.split(", ")

# Method 1: Using random.randint() and len()
random_index = random.randint(0, len(names) - 1)
selected_person_1 = names[random_index]

# Method 2: Using random.choice() (Direct Pythonic Way)
selected_person_2 = random.choice(names)

print(f"\n--- Exercise #12: Banker Roulette ---")
print(f"Friends list: {names}")
print(f"(Method 1) {selected_person_1} is going to buy the meal today!")
print(f"(Method 2) {selected_person_2} is going to buy the meal today!")
