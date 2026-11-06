"""
================================================================================
LECTURE 93: Single Inheritance in Python (#lec89)
LECTURE 94: Multiple Inheritance in Python (#lec90)
LECTURE 95: Multilevel Inheritance in Python (#lec91)
LECTURE 96: Hierarchical Inheritance in Python (#lec92)
LECTURE 97: Hybrid Inheritance in Python (#lec93)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Inheritance kya hai?
   - Ek Parent/Base class ki properties aur methods ko Child/Derived class me reuse aur extend karna.
   - Syntax: `class Child(Parent):`
   - `super()`: Parent class ke constructor aur methods ko call karne ke liye use hota hai.

2. Types of Inheritance in Python:
   - 1. Single Inheritance: Ek Parent, ek Child (`A -> B`).
   - 2. Multilevel Inheritance: Chained hierarchy (`A -> B -> C`). e.g., Grandparent -> Parent -> Child.
   - 3. Multiple Inheritance: Ek Child ke DO ya zyada Parents hote hain (`A, B -> C`). Note: Java multiple inheritance allow nahi karta classes me, par Python fully support karta hai!
   - 4. Hierarchical Inheritance: Ek Parent ke multiple Children hote hain (`A -> B` aur `A -> C`).
   - 5. Hybrid Inheritance: Do ya do se zyada types ka combination (e.g. Hierarchical + Multiple).
"""

# =====================================================================
# 1. SINGLE INHERITANCE (One Parent -> One Child)
# =====================================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating food.")

class Dog(Animal):
    def __init__(self, name, breed):
        # super() se parent ka __init__ call karte hain
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")


# =====================================================================
# 2. MULTILEVEL INHERITANCE (Grandparent -> Parent -> Child)
# =====================================================================
class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle.")

class Car(Vehicle):
    def car_info(self):
        print("Car has 4 wheels.")

class ElectricCar(Car):
    def battery_info(self):
        print("ElectricCar runs on Lithium-ion battery.")


# =====================================================================
# 3. MULTIPLE INHERITANCE (Multiple Parents -> Single Child)
# =====================================================================
class Father:
    def parenting_style(self):
        print("Father: Hardworking & Disciplined.")

class Mother:
    def culinary_skills(self):
        print("Mother: Fantastic cooking skills.")

class Child(Father, Mother):
    def hobbies(self):
        print("Child: Plays football and codes in Python.")


# =====================================================================
# 4. HIERARCHICAL INHERITANCE (One Parent -> Multiple Children)
# =====================================================================
class Shape:
    def draw(self):
        print("Drawing a generic Shape.")

class Square(Shape):
    def area(self, side):
        return side * side

class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


# =====================================================================
# 5. HYBRID INHERITANCE (Combination of multiple types)
# =====================================================================
class University:
    def uni_info(self):
        print("University: Top Central University")

class Course(University):
    def course_info(self):
        print("Course: Computer Science & Engineering")

class Sports:
    def sports_info(self):
        print("Sports: Inter-college Badminton Captain")

class EngineeringStudent(Course, Sports):  # Combines Hierarchical + Multiple
    def student_profile(self):
        print("Engineering student with sports distinction.")


# --- Verification Code ---
if __name__ == "__main__":
    print("--- 1. Single Inheritance Demo ---")
    d = Dog("Tommy", "Golden Retriever")
    d.eat()
    d.bark()

    print("\n--- 2. Multilevel Inheritance Demo ---")
    tesla = ElectricCar()
    tesla.vehicle_info()
    tesla.car_info()
    tesla.battery_info()

    print("\n--- 3. Multiple Inheritance Demo ---")
    kid = Child()
    kid.parenting_style()
    kid.culinary_skills()
    kid.hobbies()

    print("\n--- 4. Hierarchical Inheritance Demo ---")
    sq = Square()
    sq.draw()
    print("Square Area:", sq.area(4))

    print("\n--- 5. Hybrid Inheritance Demo ---")
    eng = EngineeringStudent()
    eng.uni_info()
    eng.course_info()
    eng.sports_info()
    eng.student_profile()
