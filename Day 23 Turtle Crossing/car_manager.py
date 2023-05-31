from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
TIMING = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.more_cars = True
        self.timing = TIMING
        self.move_speed = 0.1

    def new_car(self):
        random_y = randint(-250, 260)
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.goto(320, random_y)
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())

            if car.xcor() < -320:
                self.car_list.remove(car)

    def add_cars(self):
        if self.timing == TIMING:
            self.new_car()
            self.timing = 0

        self.timing += 1

    def speed_up(self):
        self.move_speed *= 0.7
