from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")
    
class Gameboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.color("white")
        self.goto(300, 50)
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.player1_score} | {self.player2_score}", align=ALIGNMENT, font=FONT)
        