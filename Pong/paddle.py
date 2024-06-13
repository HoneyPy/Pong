from turtle import *


class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1.0)
        self.setpos(x,y)
        self.speed("fastest")
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)