"""
================================================================================
LECTURE 106: Polymorphism in Python (#lec102)
LECTURE 107: Duck Typing in Python (#lec103)
LECTURE 108: Operator Overloading in Python (#lec104)
LECTURE 109: Method Overloading vs Method Overriding in Python (#lec105)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Polymorphism kya hai?
   - "Poly" (Many) + "Morphs" (Forms) = Ek hi function/method alag-alag objects ke saath alag-alag behavior show karta hai.
   - Built-in example: `len()` function string me characters ginta hai, list me elements ginta hai, dict me keys ginta hai!

2. Duck Typing Philosophy (Python Core Feature):
   - "If it walks like a duck, and it quacks like a duck, then it is a duck."
   - Python object ke TYPE ya CLASS ko nahi dekhta; balki yeh dekhta hai ki kya us object ke paas required METHOD / BEHAVIOR hai ya nahi!

3. Method Overloading vs Method Overriding:
   - Method Overriding: Child class Parent class ke method ko completely naye behavior ke saath re-define karti hai (Fully supported).
   - Method Overloading: Same method name with different parameter count/types.
     * C++/Java me natively allow hota hai.
     * PYTHON DOES NOT SUPPORT TRADITIONAL METHOD OVERLOADING! Agar aap same name se doosra method define karoge, toh wo pehle wale ko OVERWRITE kar dega!
     * Python me overloading achieve karne ke liye: Default parameters (`arg=None`) ya `*args` use karte hain.

4. Operator Overloading:
   - Operators (`+`, `-`, `*`, `>`, `==`) ko user-defined classes ke objects ke saath kaam karne layak banana.
   - Yeh Magic/Dunder methods implement karke hota hai:
     * `+` -> `__add__(self, other)`
     * `-` -> `__sub__(self, other)`
     * `*` -> `__mul__(self, other)`
     * `>` -> `__gt__(self, other)`
     * `==` -> `__eq__(self, other)`
"""

# =====================================================================
# 1. DUCK TYPING DEMO
# =====================================================================
class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I am impersonating a duck: Quack!")

class Dog:
    def bark(self):
        print("Woof!")

def make_it_quack(entity):
    # Duck Typing: Type check nahi karta, sirf .quack() method call karta hai
    entity.quack()


# =====================================================================
# 2. METHOD OVERRIDING DEMO
# =====================================================================
class Bird:
    def fly(self):
        print("Most birds can fly.")

class Penguin(Bird):
    def fly(self):
        # Overrides parent's fly() method
        print("Penguins cannot fly; they swim!")


# =====================================================================
# 3. METHOD OVERLOADING (Pythonic Approach using Default Args & *args)
# =====================================================================
class Calculator:
    # Python me multiple add() methods nahi bana sakte.
    # We use default arguments or *args to simulate overloading:
    def add(self, *args):
        if len(args) == 0:
            return 0
        total = 0
        for n in args:
            total += n
        return total


# =====================================================================
# 4. OPERATOR OVERLOADING DEMO (Complex Number / Point)
# =====================================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading '+' operator: p1 + p2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading '>' operator: p1 > p2
    def __gt__(self, other):
        # Distance from origin comparison
        dist_self = (self.x ** 2 + self.y ** 2) ** 0.5
        dist_other = (other.x ** 2 + other.y ** 2) ** 0.5
        return dist_self > dist_other

    # Overloading '==' operator: p1 == p2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # String representation for printing
    def __str__(self):
        return f"Point({self.x}, {self.y})"


# --- Verification Code ---
if __name__ == "__main__":
    print("--- 1. Testing Duck Typing ---")
    make_it_quack(Duck())
    make_it_quack(Person())  # Works because Person also has quack()!

    print("\n--- 2. Testing Method Overriding ---")
    b = Bird()
    p = Penguin()
    b.fly()
    p.fly()

    print("\n--- 3. Testing Pythonic Method Overloading ---")
    calc = Calculator()
    print("add() with 2 args:", calc.add(10, 20))
    print("add() with 4 args:", calc.add(1, 2, 3, 4))

    print("\n--- 4. Testing Operator Overloading ---")
    pt1 = Point(2, 3)
    pt2 = Point(4, 5)

    # '+' operator calls pt1.__add__(pt2)
    pt3 = pt1 + pt2
    print(f"{pt1} + {pt2} = {pt3}")

    # '>' operator calls pt1.__gt__(pt2)
    print(f"Is {pt2} > {pt1}? {pt2 > pt1}")

    # '==' operator calls pt1.__eq__(Point(2, 3))
    print(f"Is {pt1} == Point(2, 3)? {pt1 == Point(2, 3)}")
