import random
from turtle import Turtle

START_HEADINGS_P1 = [-135.0, 135.0]
START_HEADINGS_P2 = [-45.0, 45.0]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.shape("circle")
        self.setheading(45)
        self.move_speed: float = 0.01

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
        self.move_speed *= 0.9

    def p2_bounce(self):
        if self.heading() < 180:
            self.setheading(180 - self.heading())
        else:
            self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def start_p1(self):
        return random.choice(START_HEADINGS_P1)

    def start_p2(self):
        return random.choice(START_HEADINGS_P2)
