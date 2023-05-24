from turtle import Turtle

ALIGN = "center"
SCORE_FONT = ('Cascadia Code', 14, 'bold')
GAME_OVER_FONT = ('Cascadia Code', 24, 'bold')
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, move=MOVE, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, move=MOVE, font=GAME_OVER_FONT)
