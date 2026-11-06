"""
================================================================================
LECTURE 75: Python Project 5 - Silent / Blind Auction Intro (#lec71)
LECTURE 76: Python Project 5 - Silent Auction Complete Implementation (#lec72)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Blind / Silent Auction Concept:
- Ek secret bidding system jahan har bidder apna naam aur bid amount deta hai bina kisi doosre ko pata chale.
- Screen clear ho jati hai taaki agla bidder pehle wale ka bid na dekh sake.
- Sabhi bids lene ke baad program find karta hai ki highest bidder kaun hai aur auction kisne jeeti.

Dictionary Algorithm:
- `bids = {}`
- Loop me `bids[name] = bid_price` add karte jao.
- Max finding algorithm:
  * `highest_bid = 0`, `winner = ""`
  * Har bidder ke liye check karo: `if bid_amount > highest_bid: highest_bid = bid_amount, winner = name`.
"""

import os

AUCTION_HAMMER = """
             ___________
             \\         /
              )_______(
              |"""""""|_.-._,.---------.,_.-._
              |       | | |               | | ''-.
              |       |_| |_             _| |_..-'
              |_______| '-' `'---------'` '-'
              )"""""""(
             /_________\\
             .-------------.
            /_______________\\
"""

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

def run_silent_auction(bids_data=None):
    print(AUCTION_HAMMER)
    print("==========================================")
    print("    WELCOME TO THE SECRET AUCTION PROGRAM ")
    print("==========================================")

    bids = {}

    # If simulated bids provided (for automated testing):
    if bids_data:
        bids = bids_data
    else:
        bidding_finished = False
        while not bidding_finished:
            name = input("What is your name? ")
            price = int(input("What is your bid? $"))
            bids[name] = price
            should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
            if should_continue == "no":
                bidding_finished = True
            elif should_continue == "yes":
                # Clear terminal screen
                os.system('cls' if os.name == 'nt' else 'clear')

    winner, highest_bid = find_highest_bidder(bids)
    print(f"\nThe winner is {winner} with a winning bid of ${highest_bid}! 🏆")
    return winner, highest_bid

if __name__ == "__main__":
    # Test simulation
    sample_bids = {
        "Alice": 250,
        "Bob": 420,
        "Jenny": 550,
        "Charlie": 310
    }
    print("Simulating Auction with participants:")
    for person, amount in sample_bids.items():
        print(f"  {person}: ${amount}")
    run_silent_auction(sample_bids)
