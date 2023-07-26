import random
from turtle import Turtle


class Food:
    def __init__(self):
        self.food_position: list = []
        self.food_taken: bool = True

    def spawn_food(self):
        new_food = Turtle("circle")
        new_food.color("red")
        new_food.penup()
        new_food_xcor = random.randrange(-280, 280, 20)
        new_food_ycor = random.randrange(-280, 280, 20)
        new_food.goto(new_food_xcor, new_food_ycor)

        self.food_position.append(new_food)

    def check_food(self):
        if self.food_taken:
            self.spawn_food()
            self.food_taken = False

    def food_pos(self):
        return self.food_position[0].pos()

    def take_food(self):
        self.food_position[0].ht()
        self.food_position.clear()
        self.food_taken = True
