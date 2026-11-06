"""
================================================================================
LECTURE 84: Python Project 7 - Guess The Number Game (#lec80)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Game Rules & Logic:
1. Computer 1 se 100 ke beech ek secret number choose karta hai.
2. Difficulty Levels:
   - 'Easy' level: Player ko 10 attempts milte hain.
   - 'Hard' level: Player ko sirf 5 attempts milte hain.
3. Har guess par computer feedback deta hai:
   - Agar guess bada hai: "Too high."
   - Agar guess chota hai: "Too low."
   - Agar guess barabar hai: "You got it! The answer was X."
4. Attempts decrease hote hain jab tak user guess na kar le ya attempts 0 na ho jaye.
"""

import random

LOGO = """
  / _ \\_   _  ___  ___ ___  /__   \\ |__   ___    /\\ \\ / /_   _ _ __ ___ | |__   ___ _ __ 
 / /_\\/ | | |/ _ \\/ __/ __|   / /\\/ '_ \\ / _ \\  /  \\ V /| | | | '_ ` _ \\| '_ \\ / _ \\ '__|
/ /_\\\\| |_| |  __/\\__ \\__ \\  / /  | | | |  __/ / /\\ \\| || |_| | | | | | | |_) |  __/ |   
\\____/ \\__,_|\\___||___/___/  \\/   |_| |_|\\___| \\/  \\_/   \\__,_|_| |_| |_|_.__/ \\___|_|   
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, actual_answer, turns):
    """Checks answer against guess. Returns remaining turns."""
    if guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}! 🎉")
        return 0

def play_guess_game(secret_number=None, difficulty="easy", simulated_guesses=None):
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = secret_number if secret_number else random.randint(1, 100)
    turns = EASY_LEVEL_TURNS if difficulty.lower() == "easy" else HARD_LEVEL_TURNS

    guess = 0
    sim_idx = 0

    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")

        if simulated_guesses is not None and sim_idx < len(simulated_guesses):
            guess = simulated_guesses[sim_idx]
            sim_idx += 1
            print(f"Simulated Guess: {guess}")
        else:
            guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print(f"You've run out of guesses, you lose! The correct answer was {answer}.")
            return False

    return True

if __name__ == "__main__":
    # Test simulation
    print("Running simulation with Secret Number = 65, difficulty='hard':")
    play_guess_game(secret_number=65, difficulty="hard", simulated_guesses=[50, 75, 65])
