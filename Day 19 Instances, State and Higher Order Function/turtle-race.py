import turtle
from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

turtle_colors = ["red", "blue", "green", "orange", "purple", "yellow"]
all_turtles = []

x_pos = -215
y_pos = -50

for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x_pos, y_pos)
    all_turtles.append(new_turtle)
    y_pos += 25

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You've lost.")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
