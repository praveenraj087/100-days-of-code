from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle1 = Paddle(350)
l_paddle2 = Paddle(-350)
ball = Ball()
l_score = Scoreboard(-100)
r_score = Scoreboard(100)
screen.listen()
screen.onkey(r_paddle1.move_up, "Up")
screen.onkey(r_paddle1.move_down, "Down")
screen.onkey(l_paddle2.move_up, "w")
screen.onkey(l_paddle2.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.08)
    screen.update()
    ball.move_ball()
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.collision_y()

    if((ball.distance(r_paddle1) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle2) < 50 and ball.xcor() < -320)):
        ball.collision_x()

    if(ball.xcor() > 380):
        ball.reset_position()
        l_score.increase_score()

    if (ball.xcor() < -380):
        ball.reset_position()
        r_score.increase_score()


screen.exitonclick()
