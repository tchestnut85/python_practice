# pylint: disable=no-member

from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOUNDARY = 280


def start_game():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # if snake gets food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            snake.extend()
            food.refresh()

        did_hit_x_boundary = snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY
        did_hit_y_boundary = snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY

        # if snake hits a wall
        if did_hit_x_boundary or did_hit_y_boundary:
            game_is_on = False
            scoreboard.game_over()

        # if snake hits itself
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


start_game()
