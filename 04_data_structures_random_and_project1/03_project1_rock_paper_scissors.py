"""
================================================================================
LECTURE 40: Python Project 1 - Rock, Paper, Scissors Game (#lec39)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Game Rules:
- Rock beats Scissors (Rock crushes scissors)
- Scissors beats Paper (Scissors cut paper)
- Paper beats Rock (Paper covers rock)
- Same choice -> Draw / Tie

Logic:
- User choice: 0 for Rock, 1 for Paper, 2 for Scissors.
- Computer choice: `random.randint(0, 2)`.
- Conditions check:
  * user_choice == computer_choice -> Tie
  * user == 0 and computer == 2 -> User wins
  * user == 2 and computer == 1 -> User wins
  * user == 1 and computer == 0 -> User wins
  * Baaki sab cases me Computer wins!
"""

import random

# ASCII Art for choices
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

def play_rock_paper_scissors(user_choice):
    print("==========================================")
    print("         ROCK, PAPER, SCISSORS            ")
    print("==========================================")

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice! You lose automatically.")
        return

    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game Outcome Logic
    if user_choice == computer_choice:
        print("Result: It's a DRAW!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
        print("Result: Congratulations, YOU WIN! 🎉")
    else:
        print("Result: YOU LOSE! Better luck next time. 🤖")

# Demo run:
if __name__ == "__main__":
    # Test choice: 0 = Rock, 1 = Paper, 2 = Scissors
    user_input = 0  # In interactive mode: int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    play_rock_paper_scissors(user_input)
