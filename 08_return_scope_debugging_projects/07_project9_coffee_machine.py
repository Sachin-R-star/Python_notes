"""
================================================================================
LECTURE 87: Python Project 9 - Coffee Machine Simulation Project (#lec83)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Real-World Architecture of Coffee Machine:
1. Resources Tracking:
   - Machine me Water (ml), Milk (ml), Coffee (g), aur Money ($) ka stock hota hai.
2. Menu Specifications:
   - Espresso   : 50ml Water, 18g Coffee, $1.50
   - Latte      : 200ml Water, 150ml Milk, 24g Coffee, $2.50
   - Cappuccino : 250ml Water, 100ml Milk, 24g Coffee, $3.00
3. Operations:
   - "report" command: Remaining resources aur collected profit print karega.
   - Resource Check: Dekhta hai ki coffee banane ke liye stock me sufficient paani/doodh/coffee hai ya nahi.
   - Coin Calculation: Quarters ($0.25), Dimes ($0.10), Nickels ($0.05), Pennies ($0.01).
   - Change & Make Coffee: Agar paise poore hain, change return karega aur stock deduct karke drink serve karega.
"""

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_profit = 0.0

def print_report():
    print("\n--- Coffee Machine Status Report ---")
    print(f"Water  : {resources['water']}ml")
    print(f"Milk   : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money  : ${money_profit:.2f}\n")

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item, required_amount in order_ingredients.items():
        if required_amount > resources[item]:
            print(f"Sorry, there is not enough {item}!")
            return False
    return True

def process_coins(quarters=0, dimes=0, nickels=0, pennies=0):
    """Returns the total calculated from coins inserted."""
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    global money_profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        money_profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough money. ${money_received:.2f} refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item, required_amount in order_ingredients.items():
        resources[item] -= required_amount
    print(f"Here is your {drink_name} ☕️. Enjoy!\n")

def order_coffee_demo(drink_choice, quarters, dimes, nickels, pennies):
    print(f"--- Customer ordered: {drink_choice.upper()} ---")
    if drink_choice not in MENU:
        print("Invalid choice!")
        return

    drink = MENU[drink_choice]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins(quarters, dimes, nickels, pennies)
        print(f"Cost: ${drink['cost']:.2f} | Inserted: ${payment:.2f}")
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(drink_choice, drink["ingredients"])

if __name__ == "__main__":
    print_report()
    # Order Latte with exact coins (10 quarters = $2.50)
    order_coffee_demo("latte", quarters=10, dimes=0, nickels=0, pennies=0)
    print_report()
