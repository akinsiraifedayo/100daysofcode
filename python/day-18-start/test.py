import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")
colors =["red", "blue", "black", "SeaGreen", "CornflowerBlue", "IndianRed", "green", "wheat"]
tim.pensize(15)
# for i in range(4):
#     tim.right(90)
#     tim.forward(100)

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


# for sides in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(sides)



def random_walk():
    tim.forward(30)
    angle = random.choice([0, 90, 180, 270])
    tim.setheading(angle)

# for i in range(10000):
#     tim.pencolor(random_color())
#     random_walk()

turtle.reset()
turtle.shape("circle")
turtle.shapesize(5,2)
turtle.tilt(30)
turtle.fd(50)
turtle.tilt(30)
turtle.fd(50)















screen = Screen()
screen.exitonclick()