from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def respawn(self):
        self.goto(STARTING_POSITION)

# class Player:
#
#     def t_tim(self):
#         tim = Turtle()
#         tim.penup()
#         tim.goto(STARTING_POSITION)
#         tim.color("green")
#         tim.shape("turtle")
#         tim.tiltangle(90)
#         tim.goto(STARTING_POSITION)
#
#     def move_up(self):
#         new_y = Player.t_tim().ycor() + MOVE_DISTANCE
#         Player.t_tim().goto(Player.t_tim().xcor(), new_y)
#
#     def respawn(self):
#         self.goto(MOVE_DISTANCE)