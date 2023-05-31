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
scoreboard = Scoreboard()

screen.listen()
screen.getcanvas().bind('<Up>', player.move)

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    car_manager.add_cars()

    # Detect collision wih car
    for car in car_manager.car_list:
        if car.distance(player) < 30:
            screen.onkey(None, "Up")
            game_is_on = False
            screen.update()

    # Detect score
    if player.ycor() > 290:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.speed_up()
        screen.update()

    screen.update()
    time.sleep(car_manager.move_speed)

screen.exitonclick()
