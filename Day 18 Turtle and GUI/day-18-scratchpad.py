import turtle
from turtle import Turtle, Screen
from colors import color_list
import random

screen = Screen()
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.pensize(20)
turtle.colormode(255)
tim.setx(-300)
tim.sety(-300)
screen_w = screen.canvwidth
screen_h = screen.canvheight
print(screen_w)
print(screen_h)


def random_color():
    """Returns a random rgb color in tuple format"""
    color_tuple = random.choice(color_list)
    return color_tuple


def new_row():
    """Moves the turtle into position to start a new row."""
    new_x = tim.pos()[0] - 500
    new_y = tim.pos()[1] + 50
    tim.goto(new_x, new_y)


def draw_row():
    """Draws a row of ten dots"""
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)


for _ in range(10):
    draw_row()
    new_row()


screen.exitonclick()
