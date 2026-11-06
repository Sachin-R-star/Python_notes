"""
================================================================================
LECTURE 85: Debugging in Python & Debugging Tips (#lec81)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Debugging kya hai?
   - Code ke bugs / errors ko identify, trace aur fix karne ke process ko Debugging kehte hain.
   - Grace Hopper ke computer me actual moth (insect) mila tha relay me, tab se "bug" aur "debugging" term shuru hui.

2. Top 10 Common Python Errors (Interview Questions):
   - SyntaxError: Python rules ka violation (e.g. colon `:` chhoot jana).
   - IndentationError: Spaces / Tabs ki gadbadi.
   - NameError: Aisa variable access karna jo exist nahi karta ya pehle define nahi hua.
   - TypeError: Kisi data type par galat operation karna (e.g., `"age: " + 25`).
   - ValueError: Sahi data type par galat value pass karna (e.g., `int("abc")`).
   - IndexError: List ya sequence ki boundary se bahar index access karna.
   - KeyError: Dictionary me jo key nahi hai use access karna.
   - AttributeError: Aisa method ya property call karna jo us object me exist na kare (e.g., `list.lower()`).
   - ZeroDivisionError: Kisi number ko `0` se divide karna.
   - RecursionError: Base condition missing hone par maximum recursion depth exceed hona.

3. Golden Debugging Tips:
   - Stack Trace hamesha BOTTOM (aakhri line) se padhna shuru karo: Sabse neeche exact error aur line number likha hota hai.
   - Python 3.8+ f-string debug trick: `print(f"{x=}")` automatically variable ka naam aur value dono print karta hai!
   - Built-in debugger: `breakpoint()` likhne par terminal interactive pdb session khol deta hai.
"""

# --- 1. Python 3.8+ Debugging Trick: {variable=} ---
user_id = 101
username = "jenny_cs"
account_balance = 5420.75

# Pehle aise likhna padta tha: print("user_id:", user_id, "username:", username)
# Ab direct {var=} se debug print ho jata hai:
print(f"Debug Output: {user_id=} | {username=} | {account_balance=}")


# --- 2. Demonstrating Common Errors with Safe Handling (try-except) ---
print("\n--- Common Errors in Python & How to Identify Them ---")

# A. TypeError:
try:
    bad_sum = "10" + 20
except TypeError as e:
    print(f"1. TypeError caught: {e}")

# B. ValueError:
try:
    bad_conversion = int("hello")
except ValueError as e:
    print(f"2. ValueError caught: {e}")

# C. IndexError:
try:
    items = [1, 2, 3]
    val = items[10]
except IndexError as e:
    print(f"3. IndexError caught: {e}")

# D. KeyError:
try:
    user_dict = {"name": "Aman"}
    email = user_dict["email"]
except KeyError as e:
    print(f"4. KeyError caught: Key {e} not found in dict")

# E. ZeroDivisionError:
try:
    div = 100 / 0
except ZeroDivisionError as e:
    print(f"5. ZeroDivisionError caught: {e}")

# F. AttributeError:
try:
    num = 42
    num.append(5)
except AttributeError as e:
    print(f"6. AttributeError caught: {e}")


# --- 3. Rubber Duck Debugging & Systematic Process ---
"""
Systematic 4-Step Debugging Formula:
1. Replicate: Bug ko consistently recreate karo.
2. Isolate: Error wali specific line aur variables ko isolate karo (print/breakpoint se).
3. Hypothesize & Fix: Socho kyu ho raha hai aur fix apply karo.
4. Regression Test: Test karo ki nayi fix ne koi purana feature toh nahi toda.
"""
print("\nDebugging principles documented successfully.")
