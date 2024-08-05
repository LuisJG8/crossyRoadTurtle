import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")

t_float = 0.1

game_is_on = True
while game_is_on:
    time.sleep(t_float)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    scoreboard.write_t()

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.write_t()
        scoreboard.score += 1
        t_float *= 0.9

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False