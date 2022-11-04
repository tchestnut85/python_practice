from turtle import Turtle, Screen
from random import randint

TITLE = "Place a bet"
PROMPT = "Which turtle will win the race? Enter a color: "


def print_results(bet, winner):
    result = "lose"
    if bet == winner:
        result = "win"

    print(f"The winner is... {winner.upper()} TURTLE!")
    print(f"You bet on the {bet} turtle, you {result}!")


def start_race():
    colors = ("red", "orange", "yellow", "green", "blue", "purple")
    turtles = {}

    screen = Screen()
    screen.setup(width=500, height=400)

    is_race_finished = False
    winner = ""

    user_bet = screen.textinput(title=TITLE, prompt=PROMPT)

    for i, color in enumerate(colors):
        color = colors[i]
        turtles[color] = Turtle(shape="turtle")
        current_turtle = turtles[color]
        y_value = -100 + (i * 50)

        current_turtle.color(color)
        current_turtle.penup()
        current_turtle.goto(x=-230, y=y_value)

    while user_bet and not is_race_finished:
        for color, turtle in turtles.items():
            distance = randint(0, 20)
            turtle.forward(distance)
            if turtle.xcor() >= 200:
                is_race_finished = True
                winner = color.lower()

        if winner:
            turtles[winner].right(360)

    print_results(user_bet, winner)

    screen.exitonclick()


start_race()
