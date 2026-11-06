"""
================================================================================
LECTURE 98: The Diamond Problem, MRO & C3 Linearization Algorithm (#lec94)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Diamond Problem kya hai? (Deadly Diamond of Death):
   - Diagram:
           [ A ]
          /     \\
       [ B ]   [ C ]
          \\     /
           [ D ]
   - Class B aur Class C dono Class A se inherit karte hain.
   - Class D dono B aur C se inherit karti hai (`class D(B, C)`).
   - Ab agar Class A me koi method `show()` hai aur B ya C ne use override kiya hai, toh Class D ka object `d.show()` call karne par KISKA method chalega? B ka ya C ka?
   - C++ mein yeh ambiguity create karta hai. Python is problem ko solve karta hai **MRO (Method Resolution Order)** ke through!

2. MRO (Method Resolution Order):
   - Python mein methods kis order me search honge, use MRO kehte hain.
   - Python 2.3+ se **C3 Linearization Algorithm** use hota hai MRO calculate karne ke liye.
   - Rules of C3 Linearization:
     1. Child class hamesha Parent class ke pehle aayegi.
     2. Multiple parents me jo order class header me likha hai (`B` pehle, `C` baad me in `class D(B, C)`), wahi order follow hoga.
     3. Monotonicity: Har class sirf ek hi baar visit hogi (no duplicate exploration).
     4. Base class `object` hamesha sabke last me aayega.

3. MRO check karne ke 2 tareeqe:
   - `ClassName.__mro__` (Returns tuple)
   - `ClassName.mro()` (Returns list)

4. super() in Diamond Hierarchy (Interview Master Secret):
   - Freshers sochte hain `super()` hamesha "immediate parent" ko call karta hai.
   - ACTUAL TRUTH: Python mein `super()` agle class ko call karta hai **MRO SEQUENCE KE HISAAB SE**, na ki syntactic parent ke hisaab se!
"""

# --- Diamond Problem Demo ---
class A:
    def show(self):
        print("Class A show() method")

class B(A):
    def show(self):
        print("Class B show() method (Overrides A)")
        super().show()

class C(A):
    def show(self):
        print("Class C show() method (Overrides A)")
        super().show()

class D(B, C):
    def show(self):
        print("Class D show() method")
        super().show()  # Yeh MRO ke hisaab se next class (B) ko call karega


# --- Verification Code ---
if __name__ == "__main__":
    print("==========================================")
    print("      DIAMOND PROBLEM & MRO IN PYTHON     ")
    print("==========================================")

    # 1. Print MRO of Class D
    print("MRO of Class D (Tuple format):")
    for idx, cls in enumerate(D.__mro__):
        print(f"  {idx + 1}. {cls.__name__}")

    # Expected MRO: D -> B -> C -> A -> object
    print(f"\nDirect D.mro() list:\n{D.mro()}\n")

    # 2. Method Execution Order Demo
    print("--- Executing d.show() ---")
    d = D()
    d.show()

    print("\n--- Notice the Execution Chain ---")
    print("1. D.show() executes -> calls super().show()")
    print("2. Next in MRO is B -> B.show() executes -> calls super().show()")
    print("3. Next in MRO is C (NOT A directly!) -> C.show() executes -> calls super().show()")
    print("4. Next in MRO is A -> A.show() executes.")
    print("This ensures every class is cleanly visited exactly once without conflicts!")
