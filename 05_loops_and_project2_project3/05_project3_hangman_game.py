"""
================================================================================
LECTURE 57: Hangman Game Introduction (#lec53)
LECTURE 58: Hangman Game Flowchart & Game Architecture (#lec54)
LECTURE 59: Python Project 3 - Hangman Game Complete Implementation (#lec55)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Game Architecture:
1. Ek word list me se random word choose hota hai (`chosen_word`).
2. Display blanks list create hoti hai: `["_", "_", "_", ...]`.
3. Player ke paas 6 lives hoti hain (stages of hangman).
4. While loop tab tak chalega jab tak:
   - Player word guess kar le ("_" bache hi na -> WIN)
   - Ya player ki lives 0 ho jaye -> LOSE
5. Agar guessed letter word me hai:
   - Har matching index par blank ko letter se replace kar do.
6. Agar guessed letter word me NAHI hai:
   - Lives ko 1 se ghatao (`lives -= 1`) aur agla hangman stage print karo.
"""

import random

# Hangman ASCII Art Stages (6 Lives)
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    """
       --------
       |      |
       |
       |
       |
       |
       -
    """
]

WORD_LIST = ["python", "variable", "developer", "function", "engineer", "algorithm"]

def play_hangman(secret_word=None, test_guesses=None):
    print("==========================================")
    print("       WELCOME TO THE HANGMAN GAME        ")
    print("==========================================")

    # Word selection
    chosen_word = secret_word if secret_word else random.choice(WORD_LIST)
    word_length = len(chosen_word)
    lives = 6

    # Display list initially with underscores
    display = ["_"] * word_length
    guessed_letters = []

    print(f"Secret word has {word_length} letters: {' '.join(display)}")

    # Simulating or interactive guessing
    simulated_index = 0

    while "_" in display and lives > 0:
        if test_guesses is not None and simulated_index < len(test_guesses):
            guess = test_guesses[simulated_index].lower()
            simulated_index += 1
            print(f"\nGuessed Letter: {guess}")
        else:
            guess = input("Guess a letter: ").lower()

        # Check duplicate guess
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        guessed_letters.append(guess)

        # Check if guess is in word
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
            print("Good Guess!")
        else:
            lives -= 1
            print(f"Wrong Guess! '{guess}' is not in the word. Lives left: {lives}")

        print(f"Word: {' '.join(display)}")
        print(HANGMAN_STAGES[lives])

    # End game result
    if "_" not in display:
        print("🎉 CONGRATULATIONS! YOU WON! Secret word was:", chosen_word)
        return True
    else:
        print("💀 GAME OVER! YOU LOST! Secret word was:", chosen_word)
        return False

if __name__ == "__main__":
    # Test simulation to demonstrate game winning flow:
    test_word = "python"
    test_inputs = ['p', 'y', 'z', 't', 'h', 'o', 'n']
    play_hangman(secret_word=test_word, test_guesses=test_inputs)
