import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_cars()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if(player.ycor() > 280):
        player.go_to_start()
        car.increase_level()
        score.level_up()


screen.exitonclick()
