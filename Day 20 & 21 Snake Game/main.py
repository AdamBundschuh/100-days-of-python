import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


def snake_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgpic("art/background.gif")
    screen.title("Adam's Snake Game")
    screen.tracer(0)
    screen.register_shape("art/apple.gif")
    screen.register_shape("art/snake.gif")
    screen.register_shape("art/snake_head.gif")
    screen.register_shape("art/snake_head_right.gif")
    screen.register_shape("art/snake_head_up.gif")
    screen.register_shape("art/snake_head_down.gif")

    def reset_game():
        snake.reset()
        food.reset()
        scoreboard.reset()
        snake_game()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.onkey(screen.bye, "x")

    screen.onkey(reset_game, "r")

    game_is_on = True
    while game_is_on:
        screen.update()
        snake.move()
        time.sleep(0.1)

        # Detect collision with walls
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.body:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

        # Detect collision with food
        if snake.head.distance(food) < 16:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

    screen.exitonclick()


snake_game()
