import random
from turtle import Screen, Turtle

screen = Screen()

tim = Turtle()
tim.shape("circle")
tim.color("red")
tim.speed("fastest")
screen.colormode(255)


def set_color():
    color = (
        int(random.randint(0, 255)),
        int(random.randint(0, 255)),
        int(random.randint(0, 255)),
    )
    return color


def calc_angle(sides):
    angle = 360 / sides
    return angle


def draw_shape(angle, sides):
    tim.pencolor(set_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


def run(num_of_shapes):
    sides = 3
    angle = 0
    shapes = num_of_shapes

    for _ in range(shapes):
        angle = calc_angle(sides)
        draw_shape(angle, sides)
        sides += 1


run(10)
screen.exitonclick()
