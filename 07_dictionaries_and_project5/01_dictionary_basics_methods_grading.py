"""
================================================================================
LECTURE 71: Dictionaries in Python & Built-in Methods (#lec67)
LECTURE 72: Coding Exercise #23 - Student Grading Program (#lec68)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Dictionaries in Python:
   - Key-Value pairs me data store karta hai: `{key: value}`.
   - KEYS immutable (hashable) honi chahiye (Strings, Numbers, Tuples). List ya set key nahi ban sakti!
   - Keys UNIQUE hoti hain. Duplicate key likhne par purani value OVERWRITE ho jati hai.
   - Values kisi bhi datatype ki ho sakti hain aur duplicate bhi chalegi.
   - Python 3.7+ se dictionaries INSERTION-ORDERED hoti hain.

2. Important Dict Methods:
   - `dict[key]`: Key se value nikalta hai (Key nahi mili toh `KeyError` aayega).
   - `dict.get(key, default)`: SAFE retrieval (Key nahi mili toh `KeyError` nahi aayega, `default` return karega).
   - `keys()`: Sabhi keys ka view object deta hai.
   - `values()`: Sabhi values ka view object deta hai.
   - `items()`: `(key, value)` tuples ka view object deta hai (Looping ke liye best).
   - `update({k: v})`: Naye pairs add ya existing update karta hai.
   - `pop(key)`: Specified key-value ko remove karke value return karta hai.

3. Exercise #23 - Student Grading Program:
   - Scores to Grades mapping:
     * 91 - 100: "Outstanding"
     * 81 - 90 : "Exceeds Expectations"
     * 71 - 80 : "Acceptable"
     * 70 or lower: "Fail"
"""

# --- 1. Dictionary Creation & Methods ---
student = {
    "name": "Jenny",
    "course": "Python",
    "year": 2026,
    "active": True
}

print("Original Dict:", student)

# Safe access with .get():
print("Access with []:", student["name"])
print("Safe access with .get():", student.get("gpa", "Not Found (Default)"))

# Adding and updating items:
student["gpa"] = 3.9               # Adding new key
student["year"] = 2027              # Updating existing key
student.update({"city": "Delhi", "active": False})
print("After updates:", student)

# Iteration:
print("\nIterating over items():")
for key, value in student.items():
    print(f"  {key} -> {value}")


# --- 2. LECTURE 72: Exercise #23 - Student Grading Program ---
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for name, score in student_scores.items():
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[name] = grade

print("\n--- Exercise #23: Student Grades ---")
for name, grade in student_grades.items():
    print(f"{name:10s} (Score: {student_scores[name]:2d}) : {grade}")
