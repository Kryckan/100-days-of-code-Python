import random
from turtle import Screen, Turtle

screen = Screen()

tim = Turtle()
tim.shape("circle")
tim.color("red")
tim.pen(pensize=10)
tim.speed("fastest")
screen.colormode(255)


def set_color():
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    return color


def walk(steps):
    num_of_steps = steps
    for _ in range(num_of_steps):
        tim.pencolor(set_color())
        tim.setheading(random.choice([0, 90, 180, 270]))
        tim.forward(30)


walk(100)

screen.exitonclick()
