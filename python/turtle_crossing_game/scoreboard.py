from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.write(font= FONT, arg=f"Level: {self.level}")
        self.penup()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(font= FONT, arg=f"Level: {self.level}")

    def game_over(self):
        self.goto(0, 0)
        self.write(font=FONT, align="center", arg=f"GameOver!")



