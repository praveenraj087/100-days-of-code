from mimetypes import init
from msilib.schema import Class
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(cor, 200)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.color("white")
        self.clear()
        self.write(self.score, align="center",
                   font=("Courier", 80, "normal"))
        self.hideturtle()

    def update_score(self):
        self.write(self.score, align="center",
                   font=("Courier", 80, "normal"))
