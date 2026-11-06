"""
================================================================================
LECTURE 21: Coding Exercise #4 - BMI Calculator (#lec20)
LECTURE 22: round() Function & Banker's Rounding (#lec21)
LECTURE 23: f-Strings (Formatted String Literals) (#lec22)
LECTURE 24: Coding Exercise #5 - Life in Weeks (#lec23)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. round(number, ndigits):
   - Decimal numbers ko round-off karne ke liye.
   - Python uses "Banker's Rounding" (Round half to even):
     Agar fractional part exactly .5 hai, toh nearest EVEN number par round hoga!
     e.g., `round(2.5)` gives `2`, par `round(3.5)` gives `4`! (Interviewers love this question!).

2. f-Strings (Introduced in Python 3.6):
   - Strings format karne ka sabse fast aur clean tareeqa: `f"My name is {name} and age is {age}"`.
   - Curly braces `{}` ke andar koi bhi valid Python expression, function call, ya formatting likh sakte hain.
   - Decimal formatting: `{num:.2f}` (2 decimal places tak show karega).

3. Exercise #4 - BMI Calculator Formula:
   - BMI = Weight (in kg) / (Height in meters)^2

4. Exercise #5 - Life in Weeks Formula:
   - Assume lifespan = 90 years.
   - Total days = 90 * 365, Total weeks = 90 * 52, Total months = 90 * 12.
   - Remaining time = Total - (Current Age * factor).
"""

# --- 1. round() Function & Banker's Rounding Demo ---
print("--- Banker's Rounding in Python ---")
print("round(7.65)      :", round(7.65))        # 8
print("round(7.45)      :", round(7.45))        # 7
print("round(2.5)       :", round(2.5))         # 2 (Even integer)
print("round(3.5)       :", round(3.5))         # 4 (Even integer)
print("round(2.675, 2)  :", round(2.675, 2))   # Float precision quirk in Python: 2.67

# Negative ndigits: Tens, Hundreds etc. pe round karta hai
print("round(674, -1)   :", round(674, -1))     # 670 (Nearest 10)
print("round(674, -2)   :", round(674, -2))     # 700 (Nearest 100)


# --- 2. f-Strings Demo ---
name = "Sachin"
score = 98.4567
rank = 1

# Expressions inside f-string:
print(f"Candidate: {name.upper()} | Rank: #{rank} | Score: {score:.2f}")
print(f"Next year rank goal: {rank} (calculation: {rank * 1})")

# Padding & Alignment in f-string:
val = 42
print(f"Padded with zeros : {val:05d}")       # 00042
print(f"Left aligned (width 10): {name:<10}!")
print(f"Right aligned (width 10): {name:>10}!")
print(f"Center aligned (width 10): {name:^10}!")


# --- 3. LECTURE 21: Exercise #4 - BMI Calculator ---
weight_kg = 72
height_m = 1.75  # 175 cm = 1.75 meters

bmi = weight_kg / (height_m ** 2)
print(f"\n--- Exercise #4: BMI Calculator ---")
print(f"Weight: {weight_kg} kg, Height: {height_m} m")
print(f"Calculated BMI (Exact)   : {bmi}")
print(f"Calculated BMI (Integer) : {int(bmi)}")
print(f"Calculated BMI (Round 2) : {round(bmi, 2)}")


# --- 4. LECTURE 24: Exercise #5 - Life in Weeks ---
# Task: User ki age lekar calculate karo 90 saal tak kitne days, weeks, months bache hain.
current_age = 25
years_remaining = 90 - current_age

days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

print(f"\n--- Exercise #5: Life in Weeks (Assuming 90 years life) ---")
print(f"Current Age: {current_age}")
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
