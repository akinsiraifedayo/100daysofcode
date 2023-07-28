import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

move_speed = 10
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        # if car.xcor() - 30 < 0 and player.ycor() in range(int(car.ycor() - 20), int(car.ycor() + 20)):
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()
        if car.xcor() < -350:
            car_manager.all_cars.remove(car)
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.new_level()




