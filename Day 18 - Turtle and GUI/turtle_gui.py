import turtle as t
import random

tr = t.Turtle()
t.colormode(255)
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(gap):
    tr.speed(0)
    for i in range(int(360/gap)):
        tr.color(random_color())
        current_hdg = tr.heading()
        tr.circle(100)
        tr.setheading(current_hdg + gap)


draw_circle(5)

screen = t.Screen()
screen.exitonclick()
