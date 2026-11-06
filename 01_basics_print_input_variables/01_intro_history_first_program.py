"""
================================================================================
LECTURE 01 & 02: Introduction to Python & Features (#lec1)
LECTURE 03: History of Python (#lec2)
LECTURE 04: Download & Install Python & PyCharm (#lec3)
LECTURE 05: Writing First Python Program (#lec4)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Python kya hai?
   - Python ek High-Level, General Purpose, Interpreted aur Dynamically-Typed language hai.
   - Guido van Rossum ne develop kiya tha, release February 1991 mein hua.
   - Naam Monty Python's Flying Circus (British comedy show) se liya gaya tha, saanp (snake) se nahi!

2. Key Features (Interview Questions):
   - Simple & Easy to learn: English jaisa syntax hota hai.
   - Interpreted: Code line-by-line execute hota hai. (Pehele source code bytecode (.pyc) mein convert hota hai, fir Python Virtual Machine (PVM) use execute karti hai).
   - Dynamically Typed: Variable ka data type pehle se declare nahi karna padta (e.g. `x = 10` likho, `int x = 10` nahi).
   - Cross-Platform / Portable: Windows, Mac, Linux sab par chalta hai.
   - Extensive Libraries: Data Science, Web, AI/ML sabke liye built-in aur 3rd party packages hain.

3. First Program:
   - Python mein print karne ke liye simple `print("Hello World")` function use hota hai.
"""

# --- LECTURE 01 & 02: Python Features Demo ---
# Dynamically Typed Nature:
# Variable ka type runtime par decide hota hai aur change bhi ho sakta hai
x = 10                  # Abhi integer hai
print(f"x ki value: {x}, type: {type(x)}")

x = "Ab main String hu" # Same variable ab string ban gaya, koi error nahi
print(f"x ki value: {x}, type: {type(x)}")


# --- LECTURE 03: Python History Facts ---
# Python 2 vs Python 3:
# Python 2 ka support Jan 1, 2020 ko officially band ho chuka hai.
# Python 3 backwards-compatible nahi tha (e.g., Python 2 mein `print "hi"`, Python 3 mein `print("hi")`).


# --- LECTURE 04: Installation & Execution ---
# Python script run karne ke do tareeqe hote hain:
# 1. Interactive Mode: Terminal pe `python` type karke direct commands chalana (REPL - Read Eval Print Loop).
# 2. Script Mode: `.py` file bana kar terminal se run karna: `python filename.py`.


# --- LECTURE 05: First Python Program ---
print("Hello, World!")
print("Welcome to Python Full Course for Interview 2026!")

# Basic calculations console par direct print ho sakti hain:
print(5 + 3)
print(10 * 2)
