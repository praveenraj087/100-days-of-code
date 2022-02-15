from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-250, 260)
        self.write(f"Level: {self.level}", align="left",
                   font=FONT)
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left",
                   font=FONT)
        self.hideturtle()

    def game_over(self):
        self.level = 1
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
