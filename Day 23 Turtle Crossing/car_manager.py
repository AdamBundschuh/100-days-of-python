from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []


    def new_car(self):
        random_y = randint(-270, 270)
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.goto(200, random_y)
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())
