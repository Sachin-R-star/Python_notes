"""
================================================================================
LECTURE 81: Python Project 6 - Calculator Complete Code (#lec77)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Design Patterns used in this Calculator:
1. Functions as First-Class Citizens:
   - Functions ko dictionary values ke roop me store kiya gaya hai: `operations = {"+": add, "-": subtract, ...}`.
   - Symbol match hote hi direct function call hota hai: `operations[symbol](n1, n2)`.
   - `if-elif-else` ki lambi chain likhne se bach jate hain (Clean Code architecture).

2. Recursion for State Reset:
   - User jab chahe pichle result ke saath continue calculation kar sakta hai, ya fir 'fresh start' karne ke liye calculator function khud ko recursively call karta hai.
"""

CALCULATOR_LOGO = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

# Calculator Operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2

# Mapping symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def run_calculator_demo():
    print(CALCULATOR_LOGO)
    print("Welcome to Jenny's Python Calculator!")

    # Demonstration of calculations using operations dict:
    num1 = 10
    num2 = 5

    for symbol, func in operations.items():
        ans = func(num1, num2)
        print(f"{num1} {symbol} {num2} = {ans}")

    # Chained calculation simulation:
    print("\n--- Chained Calculation Demo ---")
    step1_ans = operations["+"](15, 25)        # 40
    print(f"Step 1: 15 + 25 = {step1_ans}")
    step2_ans = operations["*"](step1_ans, 2)  # 40 * 2 = 80
    print(f"Step 2: {step1_ans} * 2 = {step2_ans}")
    step3_ans = operations["/"](step2_ans, 4)  # 80 / 4 = 20.0
    print(f"Step 3: {step2_ans} / 4 = {step3_ans}")

if __name__ == "__main__":
    run_calculator_demo()
