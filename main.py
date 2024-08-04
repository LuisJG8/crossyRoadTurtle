import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


car_list = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

for i in range(9):
    car_manager = CarManager()
    car_list.append(car_manager)
    car_manager.move()

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.write_t()

    # car_manager.move()

    if player.distance(car_manager) < 30:
        car_manager.game_over()
        game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.write_t()
        scoreboard.score += 1