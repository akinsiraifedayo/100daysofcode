from turtle import Screen
from board import Board
from ball import Ball
from scoreboard import Scoreboard
import time


right_paddle = Board(350, 0)
left_paddle = Board(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)
screen.listen()

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
print(ball.x)
game_is_on = True
while game_is_on:
    time.sleep(0.1 * ball.fast)
    screen.update()
    crossed_x = False
    if ball.xcor() > 320 or ball.xcor() < -320:
        crossed_x = True
    if ((ball.distance(right_paddle) < 50) and crossed_x) or (ball.distance(left_paddle) < 50 and crossed_x):
        ball.bounce_x()
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_wins()
        right_paddle.goto(350, 0)
        left_paddle.goto(-350, 0)

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_wins()
        right_paddle.goto(350, 0)
        left_paddle.goto(-350, 0)
    else:
        ball.move()
    # elif ball.xcor() < -380:
    #     ball.move(10, ball.y)













screen.exitonclick()
