from turtle import Turtle
UP = 90
DOWN = 270
FORWARD = 20


class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)
        self.y = self.ycor()
        self.x = self.xcor()

    def up(self):
        if self.ycor() < 230:
            self.y += FORWARD
            self.goto(y=self.y, x=self.x)

    def down(self):
        if self.ycor() > -230:
            self.y -= FORWARD
            self.goto(y=self.y, x=self.x)

