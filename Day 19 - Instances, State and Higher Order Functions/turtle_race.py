from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "Make your bet", "Which turtle will win the race?: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = [-70, -40, -10, 20, 50, 80]
all_tr = []

for i in range(0, 6):
    tr = Turtle(shape="turtle")
    tr.penup()
    tr.color(color[i])
    tr.goto(x=-230, y=pos[i])
    all_tr.append(tr)

if user_bet:
    is_race_on = True

# print(all_tr)
while is_race_on:
    for tr in all_tr:
        if tr.xcor() > 230:
            is_race_on = False
            winning_color = tr.pencolor()
            if(winning_color == user_bet):
                print("You've won!")
            else:
                print("You've lose!")
        rand_dist = random.randint(0, 10)
        tr.forward(rand_dist)


screen.exitonclick()
