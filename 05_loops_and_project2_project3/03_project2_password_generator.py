"""
================================================================================
LECTURE 53: Python Project 2 - PyPassword Generator (#lec49)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Concept:
- Strong passwords me mix of Uppercase + Lowercase letters, Digits, aur Special Symbols hote hain.
- Two levels of Password Generator:
  1. Easy Level: Letters, fir Numbers, fir Symbols sequential order me aate hain (Predictable pattern).
  2. Hard Level: Sabhi characters ko ek list me daalkar `random.shuffle()` se thoroughly mix kar dete hain (Unbreakable random password).
"""

import random
import string

# Character pools
letters = list(string.ascii_letters)  # a-z + A-Z
numbers = list(string.digits)         # 0-9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters=4, nr_symbols=2, nr_numbers=3):
    print("==========================================")
    print("      PYPASSWORD GENERATOR PROJECT        ")
    print("==========================================")
    print(f"Required: {nr_letters} Letters, {nr_symbols} Symbols, {nr_numbers} Numbers")

    # --- EASY LEVEL (Sequential Order) ---
    easy_password = ""
    for _ in range(nr_letters):
        easy_password += random.choice(letters)

    for _ in range(nr_symbols):
        easy_password += random.choice(symbols)

    for _ in range(nr_numbers):
        easy_password += random.choice(numbers)

    print(f"\n[Easy Level Password (Sequential)]: {easy_password}")

    # --- HARD LEVEL (Randomly Shuffled Order) ---
    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # In-place random shuffle
    random.shuffle(password_list)

    # Join list into final string
    hard_password = "".join(password_list)

    print(f"[Hard Level Password (Shuffled)]  : {hard_password}")
    return hard_password

if __name__ == "__main__":
    generate_password(nr_letters=5, nr_symbols=3, nr_numbers=4)
