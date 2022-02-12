import random
import colorgram
import turtle as t

tr = t.Turtle()
t.colormode(255)
# colors_rgb = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     colors_rgb.append(rgb)
# print(colors_rgb)

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57),
              (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]


for j in range(1, 11):
    for i in range(10):
        rand_color = random.choice(color_list)
        tr.dot(20, rand_color)
        tr.penup()
        tr.fd(50)
    y_value = (j*50)
    tr.setpos(0, y_value)
screen = t.Screen()
screen.exitonclick()
