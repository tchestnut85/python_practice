from turtle import Screen
from gameboard import Gameboard

"""
Steps for Pong game:
create the screen
create and move paddle
create another paddle
create the ball and make it move
detect collision with wall and bounce
detect collision with paddle
detect when paddle misses
keep score
"""

WIDTH = 800
HEIGHT = 600

def start_game():
    gameboard = Gameboard()
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    screen.listen()

    screen.exitonclick()

    is_game_active = True

    # while is_game_active:

start_game()
