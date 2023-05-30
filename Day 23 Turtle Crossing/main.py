import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()



screen.listen()
screen.onkey(player.move, "Up")

car_timing = 1

game_is_on = True
while game_is_on:
    if car_timing % 3 == 0:
        car_manager.new_car()

    print(car_timing)
    print(car_timing % 1)

    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()
    car_timing += 1
