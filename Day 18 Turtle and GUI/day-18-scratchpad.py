import turtle
from turtle import Turtle, Screen
import random

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)

# 10 x 10
# 20 diameter
# 50 space between

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.pensize(20)
turtle.colormode(255)
tim.setx(-300)
tim.sety(-300)


def random_color():
    color_tuple = random.choice(color_list)
    return color_tuple


def new_row():
    """Moves the turtle into position to start a new row."""
    new_x = tim.pos()[0] - 500
    new_y = tim.pos()[1] + 50
    tim.goto(new_x, new_y)


def draw_row():
    """Draws a row of ten dots"""
    print(f'Position before row loop: {tim.position()}')
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)
    print(f'Position after row loop: {tim.position()}')


for _ in range(10):
    draw_row()
    new_row()

screen = Screen()
screen.exitonclick()
