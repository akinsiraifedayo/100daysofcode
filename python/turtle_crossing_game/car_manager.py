from  turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_X = int(600/2 + 50)
SCREEN_Y = int(600/2 -50)



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_level(self):
        self.move_speed += MOVE_INCREMENT

    def move(self):
        self.forward(self.move_speed)

    def generate_y(self):
        for i in range(int(-SCREEN_Y), int(SCREEN_Y), 20):
            self.y.append(i)

    def create_car(self):
        if random.randint(0, 5) == 0:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, +250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)










