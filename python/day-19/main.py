import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    angle = tim.heading() + 10
    tim.setheading(angle)

def turn_left():
    angle = tim.heading() - 10
    tim.setheading(angle)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()