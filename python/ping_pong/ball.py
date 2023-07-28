from turtle import Turtle
DISTANCE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 10
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.move()
        self.fast = 1



    def move(self):
        self.goto((self.xcor() + self.x), (self.ycor() + self.y))

    def bounce_y(self):
        self.y *= -1
        self.move()

    def bounce_x(self):
        self.x *= -1
        self.move()
        if self.fast > 0.1:
            self.fast -= 0.1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.fast = 1


