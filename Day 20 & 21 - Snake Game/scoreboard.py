from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt") as score_store:
            high = score_store.read()
            self.high_score = int(high)
            # score_store.close()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align="center",
                   font=("Courier", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center",
                   font=("Courier", 20, "normal"))
        self.hideturtle()

    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("data.txt", "w") as write_score:
                str_high = str(self.high_score)
                write_score.write(str_high)
                # write_score.close()
        self.score = 0
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center",
                   font=("Courier", 20, "normal"))
