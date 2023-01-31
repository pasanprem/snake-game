from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

all_turtles = []

for _ in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(x= ( _ * 10), y=0)






screen.exitonclick()