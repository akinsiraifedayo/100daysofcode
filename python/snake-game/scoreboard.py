from turtle import Turtle
POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = None
        self.open_highscore()
        self.color("white")
        self.goto(POSITION)
        self.penup()
        self.hideturtle()
        self.update_score()

    def open_highscore(self):
        with open("data.txt", mode="r") as highscore_txt:
            self.high_score = int(highscore_txt.read())

    def save_highscore(self, new_score):
        with open("data.txt", mode="w") as highscore_txt:
            highscore_txt.write(new_score)


    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore(new_score=str(self.high_score))
        self.score = 0
        self.update_score()



