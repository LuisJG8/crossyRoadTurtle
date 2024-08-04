from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 45
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("green")
        self.shape("turtle")
        self.tiltangle(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def respawn(self):
        self.goto(MOVE_DISTANCE)