from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def collision_y(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.collision_x()
