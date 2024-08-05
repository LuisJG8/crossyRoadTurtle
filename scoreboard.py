from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.score = 0
        self.color("black")

    def write_t(self):
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        the_write = Turtle()
        the_write.color("red")
        the_write.write('GAME OVER', align="center", font=("Arial", 30, "normal"))