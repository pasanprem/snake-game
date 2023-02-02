from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='Left', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
