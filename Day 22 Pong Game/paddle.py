from turtle import Turtle

WIDTH = 5
LENGTH = 1


class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(coords)


    def up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -240:
            self.goto(self.xcor(), new_y)
