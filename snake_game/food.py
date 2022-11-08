from turtle import Turtle
import random

COLORS = ("red", "orange", "yellow", "green", "blue", "purple")
SHAPE = "turtle"
BOUNDARY = 270
SIZE = 0.75


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-BOUNDARY, BOUNDARY)
        random_y = random.randint(-BOUNDARY, BOUNDARY)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
