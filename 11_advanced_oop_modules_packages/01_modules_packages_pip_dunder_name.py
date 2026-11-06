"""
================================================================================
LECTURE 101: Modules in Python (#lec97)
LECTURE 112: pip & PyPI in Python (#lec108)
LECTURE 113: Packages in Python & __init__.py (#lec109)
LECTURE 114: if __name__ == '__main__' Explained Deeply (#lec110)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Module kya hai?
   - Ek simple Python file jisme functions, classes aur variables hote hain (`.py` file).
   - Module ko reuse karne ke 3 tareeqe:
     * `import math` -> `math.sqrt(16)`
     * `from math import sqrt, pi` -> `sqrt(16)`
     * `import math as m` (Aliasing) -> `m.sqrt(16)`

2. Package kya hai?
   - Modules ka collection (folder).
   - Ek folder ko Python package tab maanta hai jab uske andar `__init__.py` file maujood ho (Python 3.3+ me optional hai par best practice hai).
   - Sub-packages bhi ho sakte hain (`import package.subpackage.module`).

3. pip & PyPI:
   - PyPI (Python Package Index): Python community ka central cloud repository jahan lakho 3rd party packages hosted hain (e.g. numpy, pandas, requests).
   - `pip` (Package Installer for Python): Command-line tool jo PyPI se packages install, upgrade aur manage karta hai (`pip install package_name`).

4. if __name__ == '__main__' (Top 3 Most Asked Python Interview Questions):
   - Har Python module ka ek internal built-in variable hota hai jiska naam `__name__` hota hai.
   - CASE 1: Agar file ko DIRECTLY run kiya gaya (e.g., `python myfile.py`), toh Python `__name__` ki value `"__main__"` set karta hai.
   - CASE 2: Agar file ko kisi doosri file me IMPORT kiya gaya (e.g., `import myfile`), toh `__name__` ki value us module ka actual naam ban jati hai (`"myfile"`).
   - Benefit: Is block ke andar ka code tabhi chalta hai jab file directly execute ho; import karne par automatically run nahi hota (prevents unintended execution).
"""

import sys
import math

# --- 1. Module Import Variations ---
print("Square root of 25 using math:", math.sqrt(25))
print("Pi constant value           :", math.pi)

# Built-in module search path:
print("Python module search path (sys.path) sample:")
for p in sys.path[:3]:
    print(f"  {p}")


# --- 2. Custom Module Simulation ---
def calculate_tax(income, tax_rate=0.18):
    """Calculates tax on given income"""
    return income * tax_rate

def generate_invoice(customer, amount):
    tax = calculate_tax(amount)
    total = amount + tax
    return f"Invoice for {customer}: Amount=${amount}, Tax=${tax}, Total=${total}"


# --- 3. LECTURE 114: if __name__ == '__main__' Deep Demo ---
print(f"\nCurrent module's __name__ value is: '{__name__}'")

if __name__ == "__main__":
    print("\n[DIRECT EXECUTION MODE]")
    print("This block runs ONLY because this script is executed directly, NOT imported.")
    print("Testing invoice generator:")
    sample_invoice = generate_invoice("Sachin", 1000)
    print(sample_invoice)
else:
    print("\n[IMPORTED MODE]")
    print("This script has been imported into another script as a library!")
