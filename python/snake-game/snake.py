from turtle import Turtle
import random
STARTING_POSITIONS = [(0 , 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLORS = ["#f5f4e8", "#c50d66", "#f07810", "#eec60a", "#57D1C9", "#ED5485", "#FFFBCB", "#FFE869"]


class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = STARTING_POSITIONS
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color(random.choice(COLORS))
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=x, y=y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




