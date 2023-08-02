import random
from turtle import Turtle

START_HEADINGS = [-135.0, -45.0, 45.0, 135.0]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.shape("circle")
        self.setheading(random.choice(START_HEADINGS))

    def move(self):
        self.forward(10)

    def wall_bounce(self):
        if self.ycor() >= 280:
            self.setheading(self.heading() * -1)
        elif self.ycor() <= -280:
            self.setheading(360 - self.heading())

    def p1_bounce(self):
        if self.heading() < 90:
            self.setheading(180 - self.heading())
        else:
            self.setheading((360 - self.heading()) + 180)

    def p2_bounce(self):
        if self.heading() < 180:
            self.setheading(180 - self.heading())
        else:
            self.setheading(180 - self.heading())
