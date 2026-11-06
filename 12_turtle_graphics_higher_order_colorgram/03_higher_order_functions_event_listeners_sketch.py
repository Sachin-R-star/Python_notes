"""
================================================================================
LECTURE 123: Python Higher Order Functions (#lec120)
LECTURE 124: Python Event Listeners in Turtle (#lec121)
LECTURE 125: Coding Exercise #33 - Etch-A-Sketch Project (#lec122)
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Higher Order Functions (HOF) kya hote hain?
   - Python mein functions "First-Class Citizens" hote hain.
   - Ek function jo kisi DOOSRE FUNCTION ko argument ke roop me accept kare, ya fir ek function ko RETURN kare, use Higher Order Function kehte hain.
   - Built-in HOFs: `map()`, `filter()`, `sorted(key=...)`.

2. Event Listeners in Turtle & GUIs:
   - `screen.listen()`: Canvas ko keyboard inputs monitor karne ke liye activate karta hai.
   - `screen.onkey(key="w", fun=move_forward)`:
     * IMPORTANT RULE: Function pass karte waqt PARENTHESES `()` NAHI lagate!
     * `move_forward` (bina brackets) = Function ka reference pass kiya (Callback).
     * `move_forward()` (brackets ke saath) = Function turant execute ho jayega jo galat hai!

3. Exercise #33 - Etch-A-Sketch Game Controls:
   - 'W' / 'w' : Move Forward
   - 'S' / 's' : Move Backward
   - 'A' / 'a' : Turn Left (Counter-Clockwise)
   - 'D' / 'd' : Turn Right (Clockwise)
   - 'C' / 'c' : Clear screen and reset turtle to home center
"""

# =====================================================================
# 1. HIGHER ORDER FUNCTIONS DEMO
# =====================================================================
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

# Higher Order Function: accepts a function 'func' as an argument
def calculate(n1, n2, func):
    """Higher order function calculating result using passed operation"""
    return func(n1, n2)

print("--- 1. Testing Custom Higher Order Function ---")
print("calculate(10, 5, add)      :", calculate(10, 5, add))       # 15
print("calculate(10, 5, multiply) :", calculate(10, 5, multiply))  # 50

# Built-in Higher Order Functions (map, filter):
numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("map() square result        :", squares)
print("filter() evens result      :", evens)


# =====================================================================
# 2. LECTURE 124 & 125: Exercise #33 - Etch-A-Sketch Logic
# =====================================================================
class EtchASketchController:
    """Headless-safe Etch-A-Sketch State Simulator"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0  # 0: East, 90: North, 180: West, 270: South
        self.history = []

    def move_forward(self, distance=10):
        self.history.append(f"Forward {distance} units")
        print(f"Action: Forward by {distance}")

    def move_backward(self, distance=10):
        self.history.append(f"Backward {distance} units")
        print(f"Action: Backward by {distance}")

    def turn_left(self, angle=10):
        self.heading = (self.heading + angle) % 360
        self.history.append(f"Turned left to {self.heading} deg")
        print(f"Action: Turn Left -> Heading: {self.heading}°")

    def turn_right(self, angle=10):
        self.heading = (self.heading - angle) % 360
        self.history.append(f"Turned right to {self.heading} deg")
        print(f"Action: Turn Right -> Heading: {self.heading}°")

    def clear(self):
        self.history.clear()
        self.x = 0
        self.y = 0
        self.heading = 0
        print("Action: Screen Cleared & Turtle Reset to Origin (0, 0)")


def run_gui_etch_a_sketch():
    try:
        import turtle
        screen = turtle.Screen()
        screen.title("Etch-A-Sketch App")
        tim = turtle.Turtle()

        def fwd():
            tim.forward(15)

        def bwd():
            tim.backward(15)

        def left():
            tim.left(15)

        def right():
            tim.right(15)

        def reset():
            tim.clear()
            tim.penup()
            tim.home()
            tim.pendown()

        screen.listen()
        # Binding key events to functions (callbacks):
        screen.onkey(key="w", fun=fwd)
        screen.onkey(key="s", fun=bwd)
        screen.onkey(key="a", fun=left)
        screen.onkey(key="d", fun=right)
        screen.onkey(key="c", fun=reset)

        print("Press W/S/A/D to draw, C to clear. Close window to finish.")
        screen.mainloop()
    except Exception as e:
        print(f"(GUI Notice: {e})")


if __name__ == "__main__":
    print("\n--- 2. Simulating Etch-A-Sketch Keypress Events ---")
    controller = EtchASketchController()
    controller.move_forward(20)
    controller.turn_left(45)
    controller.move_forward(30)
    controller.turn_right(90)
    controller.clear()
