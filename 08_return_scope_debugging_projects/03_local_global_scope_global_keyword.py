"""
================================================================================
LECTURE 82: Local and Global Scope in Python (LEGB Rule) (#lec78)
LECTURE 83: global Keyword - Modifying Global Variables (#lec79)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Variable Scope kya hota hai?
   - Ek variable program ke kis hisse me accessible / visible hai, use variable ka Scope kehte hain.

2. Python LEGB Rule (Interviewers' Favorite Concept):
   Python variables ko is hierarchy me search karta hai:
   - L -> Local: Function ke andar define kiya gaya variable.
   - E -> Enclosing: Outer function (nested function ke case me).
   - G -> Global: Module / file ke top-level par define kiya gaya variable.
   - B -> Built-in: Python ke built-in names (e.g., `print`, `len`, `range`).

3. Python does NOT have Block Scope!
   - C++/Java me `if` ya `for` loop ke andar banaya gaya variable bahar nahi milta.
   - Par Python mein `if`, `while`, `for` loop ke andar banaya gaya variable BAHAR BHI ACCESSIBLE hota hai! Sirf FUNCTIONS aur CLASSES alag scope banate hain.

4. global Keyword & UnboundLocalError:
   - Function ke andar se global variable ko READ toh direct kar sakte hain.
   - Lekin agar function ke andar use MODIFY (`x += 1`) karne ki koshish karoge bina `global x` likhe, toh Python use naya Local variable maan leta hai aur `UnboundLocalError: local variable 'x' referenced before assignment` phenk deta hai!
   - Modify karne ke liye `global x` likhna zaroori hai.
   - Enclosing function ke variable ko modify karne ke liye `nonlocal` use hota hai.
"""

# --- 1. Local vs Global Scope Demo ---
global_var = "I am Global"

def my_function():
    local_var = "I am Local"
    print("Inside function:")
    print("  Can access global:", global_var)
    print("  Can access local :", local_var)

my_function()
# print(local_var) # NameError: name 'local_var' is not defined (Bahar nahi milega)


# --- 2. Python has NO Block Scope ---
if True:
    created_inside_if = "Python block scope nahi rakhta!"

for i in range(3):
    last_loop_val = i

print("Created inside if  :", created_inside_if)  # Perfectly accessible!
print("Last loop iteration:", last_loop_val)        # Perfectly accessible!


# --- 3. global Keyword & Modifying Global Variables ---
counter = 10

def increment_counter():
    global counter  # Python ko bataya ki module-level counter ko update karna hai
    counter += 1
    print("Counter inside function:", counter)

print(f"\nBefore increment_counter(): {counter}")
increment_counter()
print(f"After increment_counter() : {counter}")


# --- 4. nonlocal Keyword (Nested Functions / Closures) ---
def outer_function():
    msg = "Outer message"

    def inner_function():
        nonlocal msg  # Enclosing scope variable ko modify karta hai
        msg = "Modified by inner function!"

    inner_function()
    print("Inside outer after inner call:", msg)

outer_function()
