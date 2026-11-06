"""
================================================================================
LECTURE 54: While Loop & While-Else in Python (#lec50)
LECTURE 55: Break, Continue, Pass - Loop Control Statements (#lec51)
LECTURE 56: Indentation in Python (PEP 8 Standards) (#lec52)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. While Loop:
   - Condition-controlled loop: Jab tak condition `True` hai, tab tak loop chalta rahega.
   - For Loop vs While Loop:
     * For Loop: Jab pata ho kitni baar chalana hai (known iterations / sequence).
     * While Loop: Jab tak koi specific condition satisfy na ho (unknown iterations, e.g. game loop jab tak user quit na kare).
   - Loop variable update karna zaroori hai, warna Infinite Loop ban jayega!

2. Loop Control Statements:
   - `break`: Loop ko turant terminate (exit) karke bahar nikal deta hai.
   - `continue`: Current iteration ko skip karke agle iteration par jump kar deta hai.
   - `pass`: Null statement (place-holder). Kuch nahi karta, sirf syntax error se bachane ke liye likha jata hai jab function ya loop ki body abhi likhni baki ho.

3. Indentation in Python:
   - C/Java ki tarah curly braces `{}` nahi hote.
   - Blocks (Scope) define karne ke liye INDENTATION (whitespace) use hoti hai.
   - PEP 8 Standard: Hamesha **4 spaces** use karo, TAB nahi.
   - Tabs aur spaces ko mix karne par `TabError: inconsistent use of tabs and spaces` aata hai.
"""

# --- 1. While Loop & While-Else ---
count = 1
print("While loop counting 1 to 5:")
while count <= 5:
    print(count, end=" ")
    count += 1
else:
    print("-> Loop successfully completed (Else block)")

# While-Else with break:
num = 1
while num <= 5:
    if num == 3:
        print("\nBreaking at 3!")
        break
    num += 1
else:
    print("This will NOT execute because of break!")


# --- 2. Break, Continue, Pass Demo ---
print("\n--- continue statement demo (Skip even numbers) ---")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Even numbers skip ho jayenge
    print(i, end=" ")
print()

print("\n--- break statement demo (Stop when target found) ---")
for i in range(1, 10):
    if i == 5:
        print(f"Target {i} reached! Exiting.")
        break
    print(i, end=" ")
print()

print("\n--- pass statement demo (Placeholder) ---")
def future_function():
    pass  # To be implemented later, prevents IndentationError

class EmptyClassForNow:
    pass

for x in [1, 2, 3]:
    pass  # Kuch nahi karega, just valid syntax
print("pass executed with 0 errors.")


# --- 3. LECTURE 56: Indentation Rules Demo ---
# Correct PEP 8 Indentation (4 spaces):
def check_indentation(val):
    if val > 0:
        print(f"{val} is positive")
        if val > 100:
            print(f"{val} is also greater than 100")
    else:
        print(f"{val} is zero or negative")

check_indentation(150)
