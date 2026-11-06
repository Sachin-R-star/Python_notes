"""
================================================================================
LECTURE 86: Python Project 8 - Higher Lower Game Complete Code (#lec82)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Game Rules & Architecture:
1. Dataset me public figures/accounts ki list hoti hai jisme unka Name, Follower Count, Description, aur Country hoti hai.
2. Two accounts display hote hain:
   - Compare A: Name, a Description, from Country.
   - VS
   - Against B: Name, a Description, from Country.
3. User ko guess karna hota hai: Kiske followers zyada hain? Type 'A' ya 'B'.
4. Game Loop Logic:
   - Agar user ka guess sahi hai: Score + 1 hoga, Account B ban jayega naya Account A, aur ek naya Account B randomly select hoga.
   - Agar guess galat hai: Game turant over ho jayega aur final score print hoga.
"""

import random

HIGHER_LOWER_LOGO = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \\/ _ \\/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /   /____/_      _____ _____
  / /   / __ \\| | /| / / _ \\/ ___/
 / /___/ /_/ /| |/ |/ /  __/ /    
/_____/\____/ |__/|__/\\___/_/     
"""

VS_LOGO = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Celebrity / Brand data
DATA = [
    {'name': 'Instagram', 'follower_count': 670, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 620, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'follower_count': 500, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'follower_count': 430, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 400, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 395, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 268, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Taylor Swift', 'follower_count': 280, 'description': 'Musician', 'country': 'United States'}
]

def format_data(account):
    """Format account data into printable representation"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_higher_lower(guess, a_followers, b_followers):
    """Returns True if user guessed correctly, False otherwise"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_higher_lower(simulated_rounds=None):
    print(HIGHER_LOWER_LOGO)
    score = 0
    game_should_continue = True

    account_a = random.choice(DATA)
    account_b = random.choice(DATA)

    round_idx = 0

    while game_should_continue:
        # Account A and B same nahi hone chahiye
        while account_a == account_b:
            account_b = random.choice(DATA)

        print(f"\nCompare A: {format_data(account_a)}")
        print(VS_LOGO)
        print(f"Against B: {format_data(account_b)}")

        if simulated_rounds is not None and round_idx < len(simulated_rounds):
            guess = simulated_rounds[round_idx].lower()
            round_idx += 1
            print(f"Simulated Guess: {guess.upper()}")
        else:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_higher_lower(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b  # B becomes next A
            account_b = random.choice(DATA)
            if simulated_rounds is not None and round_idx >= len(simulated_rounds):
                print(f"Simulation completed! Final Score: {score}")
                break
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

    return score

if __name__ == "__main__":
    # Test simulation
    print("Simulating Higher Lower Game:")
    play_higher_lower(simulated_rounds=['b', 'a'])
