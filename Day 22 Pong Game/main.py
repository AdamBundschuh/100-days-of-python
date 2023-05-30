import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_W = 800
SCREEN_H = 600
RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.title("Adam's Pong Game")
screen.tracer(0)

l_paddle = Paddle(LEFT_PADDLE)
r_paddle = Paddle(RIGHT_PADDLE)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect Wall Collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.8

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
