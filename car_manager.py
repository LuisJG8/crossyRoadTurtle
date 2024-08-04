from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
random_col = random.choice(COLORS)
ran_x = random.randint(-300, 300)
ran_y = random.randint(-300, 300)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random_col)
        self.goto(300, 0)
        self.shapesize(stretch_wid=1, stretch_len=2.5)


    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def game_over(self):
        self.color("red")
        self.write('GAME OVER', align="center", font=("Arial", 30, "normal"))

    # def more_cars(self):
    #     for i in range(0, 9):
