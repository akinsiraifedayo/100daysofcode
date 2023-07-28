from turtle import Turtle
L_SCORE_POSITION = (-100, 200)
R_SCORE_POSITION = (100, 200)
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(R_SCORE_POSITION)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, move=True, font=FONT)
        self.goto(L_SCORE_POSITION)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, move=True, font=FONT)

    def l_wins(self):
        self.l_score += 1
        self.update_score()

    def r_wins(self):
        self.r_score += 1
        self.update_score()

