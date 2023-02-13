from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high()
        self.color("white")
        self.penup()
        self.goto(0, 260)

    def get_high(self):
        with open("data.txt") as data:
            h_score = int(data.read())
            return h_score

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                new_highscore = str(self.score)
                data.write(new_highscore)
            self.high_score = self.get_high()
        self.score = 0
        self.write_score()