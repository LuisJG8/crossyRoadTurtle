from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

        def __init__(self):
            self.all_cars = []

        def create_car(self):
            random_chance = random.randint(1, 6)
            if random_chance == 1:
                new_cars = Turtle("square")
                new_cars.shapesize(stretch_wid=1, stretch_len=2.5)
                new_cars.penup()
                new_cars.color(random.choice(COLORS))
                ran_y = random.randint(-250, 250)
                new_cars.goto(300, ran_y)
                # new_x = new_cars.xcor() - STARTING_MOVE_DISTANCE
                # new_cars.goto(new_x, new_cars.ycor())
                self.all_cars.append(new_cars)

        def move_cars(self):
            for car in self.all_cars:
                car.backward(STARTING_MOVE_DISTANCE)