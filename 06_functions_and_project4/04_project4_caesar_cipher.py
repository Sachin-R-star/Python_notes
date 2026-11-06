"""
================================================================================
LECTURE 69: Python Project 4 - Caesar Cipher Intro (Part 1) (#lec65)
LECTURE 70: Python Project 4 - Caesar Cipher Complete Implementation (#lec66)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Caesar Cipher Concept:
- Ek ancient encryption technique jo Julius Caesar secret messages bhejne ke liye use karta tha.
- Substitution Cipher: Har alphabet ko alphabet list me aage ya peeche shift kar dete hain fixed number of places (Shift Key) se.
- Example:
  * Word: "abc", Shift: 2 -> "cde"
  * Wrap around: "z" ko 2 se shift karoge toh modulo `% 26` ki wajah se wapas "b" aayega!

Unified Algorithm Formula:
- `new_position = (current_position + shift_amount) % 26`
- Encrypt ke liye: `shift = +shift_amount`
- Decrypt ke liye: `shift = -shift_amount`
"""

import string

alphabet = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']

def caesar_cipher(text, shift, direction):
    result_text = ""
    direction = direction.lower()

    # Shift amount wrap-around optimization (if shift > 26)
    shift = shift % 26

    # Decryption me shift subtract hota hai
    if direction == "decode":
        shift = -shift

    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            original_index = alphabet.index(char.lower())
            new_index = (original_index + shift) % 26
            new_char = alphabet[new_index]
            result_text += new_char.upper() if is_upper else new_char
        else:
            # Numbers, spaces, symbols ko unchanged rakhte hain
            result_text += char

    return result_text


# --- Demonstration of Encode & Decode ---
if __name__ == "__main__":
    print("==========================================")
    print("         CAESAR CIPHER PROJECT            ")
    print("==========================================")

    original_message = "Hello, Python Interview 2026! Zulu."
    shift_key = 5

    # 1. Encryption
    encrypted_msg = caesar_cipher(text=original_message, shift=shift_key, direction="encode")
    print(f"Original Text : {original_message}")
    print(f"Shift Key     : {shift_key}")
    print(f"Encrypted     : {encrypted_msg}")

    # 2. Decryption
    decrypted_msg = caesar_cipher(text=encrypted_msg, shift=shift_key, direction="decode")
    print(f"Decrypted     : {decrypted_msg}")

    # Verification
    assert original_message == decrypted_msg
    print("Cipher verification: SUCCESS! (Original matches Decrypted)")
