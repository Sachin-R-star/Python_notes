"""
================================================================================
LECTURE 30: Multiple If Statements in Python (#P_29)
LECTURE 31: Coding Exercise #9 - Pizza Order Program (#P_30)
LECTURE 32: Coding Exercise #10 - Love Calculator (#P_31)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Multiple If vs Elif (Very Important Conceptual Difference):
   - `if - elif - else`: Mutually exclusive hota hai. Jaise hi koi ek condition True hui, baaki sab skip ho jaate hain.
   - Multiple `if` statements: Har ek `if` independent hota hai. Chahe pehla true ho ya na ho, sabhi conditions check hongi!
   - Use Case: Jab user ek se zyada options select kar sakta hai (jaise Pizza me extra cheese AND extra pepperoni dono add karna).

2. Exercise #9 - Pizza Order Rates:
   - Small Pizza (S): $15
   - Medium Pizza (M): $20
   - Large Pizza (L): $25
   - Pepperoni for Small: +$2, for Medium/Large: +$3
   - Extra cheese for any size: +$1

3. Exercise #10 - Love Calculator Logic:
   - Do names lo, combine karo, aur lowercase me convert karo.
   - Count karo "TRUE" letters kitni baar aaye -> first digit.
   - Count karo "LOVE" letters kitni baar aaye -> second digit.
   - Dono digits combine karke percentage banao aur message print karo.
"""

# --- 1. LECTURE 30 & 31: Exercise #9 - Pizza Order Program ---
# Multiple independent if statements ka practical example
size = "M"          # Options: 'S', 'M', 'L'
add_pepperoni = "Y" # Options: 'Y', 'N'
extra_cheese = "Y"  # Options: 'Y', 'N'

bill = 0

# Base price calculation (using if-elif-else)
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid Pizza Size selected!")

# Additional toppings (using independent multiple if statements)
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print("--- Exercise #9: Pizza Order Bill ---")
print(f"Order: Size={size}, Pepperoni={add_pepperoni}, Extra Cheese={extra_cheese}")
print(f"Your final bill is: ${bill}")


# --- 2. LECTURE 32: Exercise #10 - Love Calculator ---
name1 = "David Beckham"
name2 = "Victoria Beckham"

combined_names = (name1 + name2).lower()

# Count occurrences for "TRUE"
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
true_count = t + r + u + e

# Count occurrences for "LOVE"
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e_love = combined_names.count("e")
love_count = l + o + v + e_love

# Two digit string combination
love_score_str = str(true_count) + str(love_count)
love_score = int(love_score_str)

print(f"\n--- Exercise #10: Love Calculator ---")
print(f"Names: {name1} & {name2}")
print(f"T={t}, R={r}, U={u}, E={e} -> Total = {true_count}")
print(f"L={l}, O={o}, V={v}, E={e_love} -> Total = {love_count}")
print(f"Love Score: {love_score}%")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}%, you are alright together.")
else:
    print(f"Your score is {love_score}%.")
