"""
================================================================================
LECTURE 46: For Loop in Python (#lec42)
LECTURE 47: For-Else Statement in Python (#lec43)
LECTURE 48: Coding Exercise #14 - Average Height (without len() or sum()) (#lec44)
LECTURE 49: Coding Exercise #15 - Maximum Score (without max()) (#lec45)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. For Loop:
   - Sequence (List, Tuple, String, Range, etc.) ke elements par one-by-one iterate (traverse) karne ke liye.
   - Syntax: `for item in sequence:`

2. For-Else Block (Interview Favourite):
   - Python mein loops ke saath bhi `else` block lag sakta hai!
   - Rule: Loop ka `else` block TABHI execute hota hai jab loop COMPLETELY finish ho jaye (bina kisi `break` statement ke hit hue).
   - Agar loop ke andar `break` execute hua, toh `else` block SKIP ho jata hai.
   - Use case: Search algorithm - agar item mil gaya toh break karo, agar pura loop khatam ho gaya aur item nahi mila toh else block bolega "Item Not Found".

3. Exercise #14 & #15 Constraints:
   - Built-in functions `len()`, `sum()`, `max()` ko bina use kiye manually logic build karna loop ke through (Interviews test this foundational thinking).
"""

# --- 1. For Loop Basics ---
fruits = ["Apple", "Mango", "Banana"]
print("Iterating over list:")
for fruit in fruits:
    print(f"- {fruit}")

print("\nIterating over characters of a string:")
for ch in "Python":
    print(ch, end=" ")
print()


# --- 2. LECTURE 47: For-Else Concept & Search Algorithm Demo ---
target = 30
numbers = [10, 20, 30, 40, 50]

print("\n--- For-Else Demo (Item Found) ---")
for num in numbers:
    if num == target:
        print(f"Target {target} found! Breaking loop.")
        break
else:
    print("Target NOT found in the list.")  # Break hua toh yeh execute nahi hoga!

target_missing = 99
print("\n--- For-Else Demo (Item Not Found) ---")
for num in numbers:
    if num == target_missing:
        print(f"Target {target_missing} found!")
        break
else:
    print(f"Target {target_missing} was NOT found in list! (Else block executed)")


# --- 3. LECTURE 48: Exercise #14 - Average Height without len() or sum() ---
# Input: list of student heights
heights = [150, 165, 172, 180, 158, 169]

total_height = 0
number_of_students = 0

for h in heights:
    total_height += h
    number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"\n--- Exercise #14: Average Height ---")
print(f"Heights: {heights}")
print(f"Total Height: {total_height}")
print(f"Number of Students: {number_of_students}")
print(f"Average Height: {average_height} cm")


# --- 4. LECTURE 49: Exercise #15 - Find Max Score without max() ---
# Input: student scores
scores = [78, 65, 89, 86, 55, 91, 64, 89]

max_score = scores[0]  # Pehle score ko initially maximum maan lete hain

for score in scores:
    if score > max_score:
        max_score = score

print(f"\n--- Exercise #15: Maximum Score ---")
print(f"Scores: {scores}")
print(f"The highest score in the class is: {max_score}")
