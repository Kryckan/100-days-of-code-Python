import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        xcor = random.randrange(-280, 280, 20)
        ycor = random.randrange(-280, 280, 20)
        self.goto(xcor, ycor)
