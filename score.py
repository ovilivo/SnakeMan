from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 22, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.scoreboard()
    def scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()
