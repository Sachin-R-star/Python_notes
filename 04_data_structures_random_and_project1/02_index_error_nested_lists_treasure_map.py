"""
================================================================================
LECTURE 37: Fix Python IndexError: List Index Out of Range (#lec36)
LECTURE 38: Nested Lists in Python (Matrices / 2D Lists) (#lec37)
LECTURE 39: Coding Exercise #13 - Treasure Map (#lec38)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. IndexError: list index out of range:
   - Yeh error tab aata hai jab hum kisi aise index ko access karte hain jo list ki range se bahar hai.
   - Example: Agar list ki length `n` hai, toh valid indices `0` se `n-1` tak hi hote hain. `list[n]` par IndexError aayega!
   - Negative index mein `-len(list)` se `-1` tak hi valid hota hai.

2. Nested Lists (2D Arrays / Matrices):
   - Jab ek list ke andar doosri list ho: `matrix = [[1, 2], [3, 4]]`.
   - Access karne ka syntax: `matrix[row][col]`.

3. Exercise #13 - Treasure Map:
   - 3x3 grid / matrix banate hain emojis se.
   - User 2-digit position deta hai (e.g., column=2, row=3).
   - Specified row and column par 'X' mark karna hota hai.
"""

# --- 1. LECTURE 37: IndexError Demo & Prevention ---
fruits = ["Apple", "Peach", "Pear"]
total_items = len(fruits)

print(f"Total fruits: {total_items}")
# fruits[3] -> IndexError: list index out of range (Kyunki last valid index 2 hai)

# Safe access pattern:
index_to_access = 2
if 0 <= index_to_access < len(fruits):
    print(f"Item at index {index_to_access}: {fruits[index_to_access]}")
else:
    print("Index out of bounds!")


# --- 2. LECTURE 38: Nested Lists Demo ---
dirty_dozen_fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples"]
dirty_dozen_veggies = ["Tomatoes", "Celery", "Potatoes"]

nested_list = [dirty_dozen_fruits, dirty_dozen_veggies]
print("\nNested 2D List:")
print(nested_list)

# Accessing elements:
# nested_list[0] gives fruits list, nested_list[0][1] gives "Spinach"
print("Row 0, Col 1 element:", nested_list[0][1])


# --- 3. LECTURE 39: Exercise #13 - Treasure Map ---
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]

print("\n--- Exercise #13: Treasure Map ---")
print("Initial Map:")
print(f"{row1}\n{row2}\n{row3}")

# Simulating user input: "23" -> Column 2, Row 3
position = "23"

# Column and Row extraction (convert to 0-based index)
col = int(position[0]) - 1  # 2 - 1 = 1
row = int(position[1]) - 1  # 3 - 1 = 2

# Place treasure mark 'X'
treasure_map[row][col] = " X "

print(f"\nAfter placing treasure at position {position} (Col {col+1}, Row {row+1}):")
print(f"{row1}\n{row2}\n{row3}")
