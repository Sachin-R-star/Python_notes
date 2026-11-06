"""
================================================================================
LECTURE 99: File Handling in Python (#lec95)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. File Handling kya hai?
   - Disk par files ko Create, Read, Update (Append) aur Delete karne ka process.
   - Syntax: `f = open("filename.txt", "mode")`

2. File Modes (Must-Know for Interviews):
   - `'r'`  (Read Only): File exist karni chahiye, warna `FileNotFoundError`. Default mode. Pointer start par hota hai.
   - `'w'`  (Write Only): Agar file exist nahi karti toh bana deta hai. Agar exist karti hai toh PURANA DATA OVERWRITE (TRUNCATE) kar deta hai!
   - `'a'`  (Append Only): Data ko file ke END me add karta hai (Purana data safe rehta hai). Pointer end par hota hai.
   - `'r+'` (Read + Write): File start se overwrite karti hai, file exist karni chahiye.
   - `'w+'` (Write + Read): File ko truncate karke naye sire se write aur read allow karta hai.
   - `'a+'` (Append + Read): Append aur read dono allow karta hai.
   - `'b'`  (Binary Mode): Images, videos, PDFs ke liye (`'rb'`, `'wb'`).

3. Important File Methods:
   - `read(size)`: Pura content ya given bytes tak string return karta hai.
   - `readline()`: Sirf ek line padhta hai cursor tak.
   - `readlines()`: Sabhi lines ko list of strings bana kar return karta hai `['line1\n', 'line2\n']`.
   - `tell()`: Current cursor/pointer ki byte position batata hai.
   - `seek(offset)`: Cursor/pointer ko specific byte position par move karta hai.

4. `with` Statement (Context Manager):
   - Best Practice! Manually `f.close()` likhne ki zaroorat nahi hoti.
   - Exception aane par bhi file automatically aur safely CLOSE ho jati hai (prevents resource leaks).
"""

import os

test_filename = "demo_file_interview.txt"

# --- 1. Writing to a File ('w' mode) ---
with open(test_filename, "w", encoding="utf-8") as f:
    f.write("Line 1: Python File Handling Tutorial\n")
    f.write("Line 2: Jenny's Lectures Python 2026\n")
    f.writelines([
        "Line 3: First bullet point\n",
        "Line 4: Second bullet point\n"
    ])
print("Successfully written to file using 'w' mode.")


# --- 2. Reading from a File ('r' mode) ---
print("\n--- Reading Full Content (.read()) ---")
with open(test_filename, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print("--- Reading Line by Line (.readline()) ---")
with open(test_filename, "r", encoding="utf-8") as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    print("Readline 1:", line1)
    print("Readline 2:", line2)

print("\n--- Reading into List (.readlines()) ---")
with open(test_filename, "r", encoding="utf-8") as f:
    lines_list = f.readlines()
    print("List of lines:", [l.strip() for l in lines_list])


# --- 3. Appending to a File ('a' mode) ---
with open(test_filename, "a", encoding="utf-8") as f:
    f.write("Line 5: This line was appended at the end!\n")
print("\nAppended new line using 'a' mode.")


# --- 4. seek() and tell() Pointer Manipulation ---
with open(test_filename, "r", encoding="utf-8") as f:
    print(f"\nInitial pointer position via tell(): {f.tell()}")
    chunk = f.read(10)
    print(f"Read 10 bytes: '{chunk}'")
    print(f"Pointer position after reading 10 bytes: {f.tell()}")

    # Reset pointer to start:
    f.seek(0)
    print(f"Pointer reset to 0 via seek(0): {f.tell()}")
    print("Read first 6 bytes after reset:", f.read(6))


# --- Cleanup test file ---
if os.path.exists(test_filename):
    os.remove(test_filename)
    print(f"\nCleaned up temporary file '{test_filename}'.")
