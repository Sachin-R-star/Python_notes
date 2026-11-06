"""
================================================================================
LECTURE 06: Coding Exercise #1 - Printing & Formatting
LECTURE 07: print() Function, Escape Sequences & String Concatenation
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. print() Function:
   - Output screen/console par show karne ke liye use hota hai.
   - Default arguments:
     * `sep=' '`: Multiple items ke beech by default ek space aati hai.
     * `end='\n'`: Print ke baad cursor nayi line par chala jata hai.

2. String Concatenation:
   - Do ya zyada strings ko '+' operator se jodna (merge karna).
   - Rule: String ke saath sirf string hi concatenate hoti hai. Number ke saath `+` karoge to TypeError aayega.

3. Escape Characters:
   - `\n`: New line (agli line pe jana)
   - `\t`: Tab space (4 spaces)
   - `\"` ya `\'`: Quotes ke andar quotes print karne ke liye
   - `\\`: Backslash print karne ke liye
"""

# --- 1. Basic print() & Quotes ---
# Single quotes, double quotes ya triple quotes use kar sakte hain
print("Hello Jenny's Lectures")
print('Single quotes bhi valid hain')
print("""Triple quotes se multi-line
string bina \\n ke print ho jati hai.""")

# --- 2. String Concatenation using '+' ---
# Do strings ko merge karna
first_name = "Rahul"
last_name = "Sharma"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Concatenation error demo (Interview Trap):
# print("Age: " + 25)  # TypeError: can only concatenate str (not "int") to str
# Solution: Typecast karna padega
print("Age: " + str(25))

# --- 3. Escape Sequences ---
# \n se line change hoti hai
print("Line 1\nLine 2\nLine 3")

# \t se horizontal tab space aati hai
print("Name:\tJenny")

# Quotes inside quotes
print("She said, \"Python is awesome!\"")
print('He said, \'Yes it is!\'')

# Raw String (prefix 'r'): escape characters ko ignore kar deta hai (Regex & File paths me bohot use hota hai)
print(r"C:\Users\SACHIN\new_folder\test.txt")

# --- 4. print() parameters: sep and end ---
# sep: Separator between arguments
print("Python", "Java", "C++", sep=" | ")

# end: Line end character (default is '\n', yahan hum space ya comma kar sakte hain)
print("Hello", end=" ---> ")
print("World!")  # Same line pe print hoga

# --- LECTURE 06: EXERCISE #1 Solution ---
# Task: Print output exactly formatted like this:
# First Program - Python print function
# It is declared like this:
# print('what to print')
print("\n--- Exercise #1 Output ---")
print("First Program - Python print function")
print("It is declared like this:")
print("print('what to print')")
