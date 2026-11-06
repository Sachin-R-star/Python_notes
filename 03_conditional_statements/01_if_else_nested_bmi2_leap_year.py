"""
================================================================================
LECTURE 25: If & If-Else Conditional Statements (#lec24)
LECTURE 26: Coding Exercise #6 - Odd or Even Program (#lec25)
LECTURE 27: Nested If-Else & elif Statements (#lec26)
LECTURE 28: Coding Exercise #7 - BMI 2.0 with Categories (#P_27)
LECTURE 29: Coding Exercise #8 - Leap Year Checker (#P_28)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Conditional Statements:
   - Decision-making ke liye use hote hain: "Agar yeh condition true hai, toh yeh code chalao, warna wo".
   - Python mein brackets `{}` nahi hote, INDENTATION (4 spaces) block define karti hai.

2. Syntax Structure:
   - `if condition:`
   - `elif another_condition:` (Else If)
   - `else:` (Jab koi bhi condition match na kare)

3. Nested If-Else:
   - Ek `if` ke andar doosra `if-else` likhna.

4. Leap Year Algorithm (Classic Interview Question):
   - Year 4 se divisible hona chahiye AND
   - Century year (divisible by 100) NAHI hona chahiye, UNLESS wo 400 se divisible ho!
   - Conditions:
     1. Divisible by 4?
        - No -> Not a leap year
        - Yes -> Divisible by 100?
                 - No -> Leap year
                 - Yes -> Divisible by 400?
                          - Yes -> Leap year
                          - No -> Not a leap year
"""

# --- 1. LECTURE 25 & 26: Exercise #6 - Odd or Even Program ---
num = 14
print("--- Exercise #6: Odd or Even ---")
if num % 2 == 0:
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")


# --- 2. LECTURE 27 & 28: Exercise #7 - BMI 2.0 with Health Interpretations ---
# Health ranges:
# BMI < 18.5         : Underweight
# 18.5 <= BMI < 25   : Normal weight
# 25 <= BMI < 30     : Overweight
# 30 <= BMI < 35     : Obese
# BMI >= 35          : Clinically Obese

weight = 75
height = 1.72  # in meters
bmi_val = round(weight / (height ** 2), 1)

print(f"\n--- Exercise #7: BMI 2.0 (BMI = {bmi_val}) ---")
if bmi_val < 18.5:
    print(f"Your BMI is {bmi_val}, you are Underweight.")
elif bmi_val < 25:
    print(f"Your BMI is {bmi_val}, you have a Normal weight.")
elif bmi_val < 30:
    print(f"Your BMI is {bmi_val}, you are Overweight.")
elif bmi_val < 35:
    print(f"Your BMI is {bmi_val}, you are Obese.")
else:
    print(f"Your BMI is {bmi_val}, you are Clinically Obese.")


# --- 3. LECTURE 29: Exercise #8 - Leap Year Checker ---
# Tested with years: 2000 (Leap), 2100 (Not Leap), 2024 (Leap), 2023 (Not Leap)
year = 2024

print(f"\n--- Exercise #8: Leap Year Checker for {year} ---")

# Method 1: Nested If-Else (Jenny's lecture flowchart implementation)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"(Nested If) {year} is a Leap Year!")
        else:
            print(f"(Nested If) {year} is NOT a Leap Year.")
    else:
        print(f"(Nested If) {year} is a Leap Year!")
else:
    print(f"(Nested If) {year} is NOT a Leap Year.")

# Method 2: One-liner logical condition (Interview standard)
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"(One-Liner Condition) Is {year} leap? {is_leap}")
