from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self) -> None:
        self.all_tr = []
        self.create_snake()
        self.head = self.all_tr[0]

    def create_snake(self):
        for i in START_POS:
            self.add_snake(i)

    def extend(self):
        self.add_snake(self.all_tr[-1].position())

    def add_snake(self, i):
        tr = Turtle("square")
        tr.penup()
        tr.color("White")
        tr.goto(i)
        self.all_tr.append(tr)

    def move(self):
        for i in range(len(self.all_tr)-1, 0, -1):
            new_x = self.all_tr[i-1].xcor()
            new_y = self.all_tr[i-1].ycor()
            self.all_tr[i].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    def move_up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(90)

    def move_down(self):
        if(self.head.heading() != UP):
            self.head.setheading(270)

    def move_left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(180)

    def move_right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(0)
