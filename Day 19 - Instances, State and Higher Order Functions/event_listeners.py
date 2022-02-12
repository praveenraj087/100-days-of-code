import turtle as t

tr = t.Turtle()
t.colormode(255)


def move_forward():
    tr.fd(10)


def move_backward():
    tr.bk(10)


def tilt_left():
    current_heading = tr.heading()
    tr.setheading(current_heading+10)


def tilt_right():
    current_heading = tr.heading()
    tr.setheading(current_heading-10)


def clear():
    tr.clear()
    tr.penup()
    tr.home()
    tr.pendown()


screen = t.Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(tilt_left, "a")
screen.onkey(tilt_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
