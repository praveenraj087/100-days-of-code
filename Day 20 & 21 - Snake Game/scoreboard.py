from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align="center",
                   font=("Courier", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center",
                   font=("Courier", 20, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center",
                   font=("Courier", 20, "normal"))
