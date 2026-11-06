"""
================================================================================
LECTURE 88: Object-Oriented Programming (OOP) Introduction (#lec84)
LECTURE 89: Classes and Objects in Python (#lec85)
LECTURE 90: self Parameter & __init__() Constructor (#lec86)
LECTURE 91: Methods in Python - Instance, Class (@classmethod) & Static (@staticmethod) (#lec87)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. OOP vs Procedural Programming:
   - Procedural (POP): Functions aur sequence of instructions par focus karta hai (C, Pascal). Code scalable nahi hota jab projects bade hote hain.
   - OOP: Real-world entities ko model karta hai using Objects jo Attributes (Data/Properties) aur Methods (Behavior/Functions) combine karte hain.

2. Class vs Object:
   - Class: Blueprint / Template / Naksha hoti hai (e.g. Car design).
   - Object (Instance): Blueprint se bani real physical entity (e.g. Red Honda Civic).

3. `__init__()` Method:
   - Python ka Constructor. Jab bhi naya object banta hai (`obj = Car()`), yeh automatically call hota hai.
   - Object ke attributes initialize karne ke kaam aata hai.

4. `self` Parameter (Top Interview Question):
   - `self` CURRENT OBJECT INSTANCE ko point karta hai.
   - Isse Python ko pata chalta hai ki kis object ke attributes read ya modify karne hain.
   - Python implicitly pass karta hai: `car1.drive()` internally ban jata hai `Car.drive(car1)`.

5. 3 Types of Methods in Python:
   - Instance Method: Pehla argument `self` leta hai. Specific instance data access/modify karta hai.
   - Class Method (`@classmethod`): Pehla argument `cls` leta hai. Class-level data modify karta hai (Factory methods).
   - Static Method (`@staticmethod`): Na `self` leta hai na `cls`. Normal utility function jo class ke namespace me rehta hai.
"""

class Student:
    # --- Class Attribute (Sabhi students ke liye shared) ---
    school_name = "Delhi Public School"
    total_students_count = 0

    # --- Constructor (__init__) ---
    def __init__(self, name, roll_no, marks):
        # Instance Attributes (Har student ke liye unique)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.total_students_count += 1

    # --- 1. Instance Method ---
    def display_details(self):
        print(f"Student: {self.name} | Roll: {self.roll_no} | Marks: {self.marks} | School: {self.school_name}")

    def is_passed(self):
        return self.marks >= 40

    # --- 2. Class Method (@classmethod) ---
    @classmethod
    def change_school_name(cls, new_school):
        cls.school_name = new_school
        print(f"School name changed to: {cls.school_name}")

    @classmethod
    def from_string(cls, student_str):
        """Alternative Constructor / Factory Method (Classic Interview Pattern)"""
        name, roll_no, marks = student_str.split("-")
        return cls(name, int(roll_no), float(marks))

    # --- 3. Static Method (@staticmethod) ---
    @staticmethod
    def is_holiday(day):
        """Utility function: does not access self or cls"""
        return day.lower() in ["sunday", "saturday"]


# --- Demonstration & Verification ---
if __name__ == "__main__":
    print("--- Creating Objects via Standard Constructor ---")
    s1 = Student("Aman", 101, 85.5)
    s2 = Student("Rohan", 102, 38.0)

    s1.display_details()
    s2.display_details()
    print(f"Is {s1.name} passed? {s1.is_passed()}")
    print(f"Is {s2.name} passed? {s2.is_passed()}")

    print("\n--- Alternative Constructor via @classmethod ---")
    s3 = Student.from_string("Priya-103-92.0")
    s3.display_details()

    print(f"Total students enrolled: {Student.total_students_count}")

    print("\n--- Testing @staticmethod ---")
    print("Is Sunday a holiday?", Student.is_holiday("Sunday"))
    print("Is Monday a holiday?", Student.is_holiday("Monday"))
