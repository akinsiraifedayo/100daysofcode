# import colorgram
# all_colors = colorgram.extract("spot.jpg", 20)
# colors_list = []
# for colors in all_colors:
#     color = colors.rgb
#     r = color[0]
#     g = color[1]
#     b = color[2]
#     rgb = (r, g, b)
#     colors_list.append(rgb)
# print(colors_list)
import turtle
from turtle import Turtle, Screen
import random
colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]
tim = Turtle()
tim.hideturtle()
turtle.colormode(255)


def draw_line(radius, space):
    tim.dot(radius, color)
    tim.penup()
    tim.fd(space)
    tim.pendown()


def return_to_left(w, s):
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.speed("fastest")
    tim.forward(s * w)
    tim.speed("slow")
    tim.right(180)


tim.penup()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
tim.pendown()

height = 10
width = 10
space = 50
radius = 20
for h in range(height):
    for w in range(width):
        color = random.choice(colors_list)
        draw_line(radius, space)
    return_to_left(width, space)


screen = Screen()
screen.exitonclick()
