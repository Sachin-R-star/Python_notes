"""
================================================================================
LECTURE 122: Python Project 11 - Turtle Race Project (#lec119)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
Turtle Race Game Architecture:
1. Setup:
   - Screen width: 500, height: 400.
   - 6 Turtles banaye jaate hain with Rainbow Colors: `['red', 'orange', 'yellow', 'green', 'blue', 'purple']`.
   - Sabhi turtles ko Starting Line par align karte hain: `x = -230`, y-positions: `[-70, -40, -10, 20, 50, 80]`.
2. Betting:
   - User se input lete hain screen prompt ya console par: "Which turtle will win the race? Enter color:".
3. Race Execution (While Loop):
   - Har frame par har turtle random distance `random.randint(0, 10)` aage badhega.
   - Jaise hi kisi turtle ka `xcor() > 230` ho jata hai, wo Finish Line cross kar leta hai.
   - Winning color declare hota hai: Agar user ka bet match kiya toh "You won!", warna "You lost!".
"""

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_X = -230
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]
FINISH_LINE_X = 230

def run_turtle_race_simulation(user_bet="red"):
    print("==========================================")
    print("         TURTLE RACE PROJECT              ")
    print("==========================================")
    print(f"User placed bet on: '{user_bet.upper()}' turtle.")
    print("Racers:", COLORS)

    # Simulated race logic (works in both GUI and Headless mode)
    # Track x coordinates of all 6 racers
    racer_positions = {color: START_X for color in COLORS}
    race_on = True
    winner = None

    step_count = 0
    while race_on:
        step_count += 1
        for color in COLORS:
            # Move random distance forward
            rand_distance = random.randint(1, 10)
            racer_positions[color] += rand_distance

            # Check for finish line
            if racer_positions[color] >= FINISH_LINE_X:
                race_on = False
                winner = color
                break

    print(f"\nRace finished in {step_count} steps!")
    print(f"The winner is the {winner.upper()} turtle! 🏁")

    if winner.lower() == user_bet.lower():
        print(f"🎉 Congratulations! You won the bet on {winner}!")
        return True
    else:
        print(f"💀 Bad luck! The {winner} turtle won, you lost your bet.")
        return False

# GUI Turtle Implementation
def start_gui_race():
    try:
        import turtle
        screen = turtle.Screen()
        screen.setup(width=500, height=400)
        screen.title("Turtle Race Championship")

        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        if not user_bet:
            user_bet = "red"

        all_turtles = []
        for i in range(len(COLORS)):
            racer = turtle.Turtle(shape="turtle")
            racer.color(COLORS[i])
            racer.penup()
            racer.goto(x=START_X, y=Y_POSITIONS[i])
            all_turtles.append(racer)

        is_race_on = True
        while is_race_on:
            for turtle_racer in all_turtles:
                if turtle_racer.xcor() > FINISH_LINE_X:
                    is_race_on = False
                    winning_color = turtle_racer.pencolor()
                    if winning_color.lower() == user_bet.lower():
                        print(f"You've won! The {winning_color} turtle is the winner! 🎉")
                    else:
                        print(f"You've lost! The {winning_color} turtle is the winner! ❌")
                    break

                rand_dist = random.randint(0, 10)
                turtle_racer.forward(rand_dist)

        screen.exitonclick()
    except Exception as e:
        print(f"(GUI Note: {e} -> Falling back to algorithmic race simulation)")
        run_turtle_race_simulation(user_bet="blue")

if __name__ == "__main__":
    # Test simulation
    run_turtle_race_simulation(user_bet="blue")
