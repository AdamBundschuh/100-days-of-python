import turtle
from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(1)
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


directions = [0, 90, 180, 270]


def draw_spirograph(gap_size):
    gap_int = int(360 / gap_size)
    for i in range(gap_int):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(4)

screen = Screen()
screen.exitonclick()
