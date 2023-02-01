from turtle import Turtle

class Snake():

    segments = []

    for _ in range(3):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(x= ( _ * 10), y=0)
        segments.append(t)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)