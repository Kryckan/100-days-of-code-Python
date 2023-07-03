import colorsys
from turtle import Screen, Turtle

screen = Screen()
tim = Turtle()
tim.shape("circle")
tim.color("red")
tim.pen(pensize=1)
tim.speed("fastest")
tim.ht()
screen.colormode(255)
rainbow_colors: list[int] = []


def create_rainbow_colors(num_colors):
    step = 360 / num_colors

    for i in range(num_colors):
        hue = i * step
        saturation = 1.0
        value = 1.0
        rgb = colorsys.hsv_to_rgb(hue / 360, saturation, value)

        red = int(rgb[0] * 255)
        green = int(rgb[1] * 255)
        blue = int(rgb[2] * 255)

        rainbow_colors.append((red, green, blue))


def walk(circles, radius):
    current_angle = 0
    angle = 360 / circles
    rad = radius
    create_rainbow_colors(circles)
    run_nr = 0
    while current_angle < 360:
        tim.setheading(current_angle)
        tim.pencolor(rainbow_colors[run_nr])
        tim.circle(rad)
        current_angle += angle
        run_nr += 1


walk(100, 170)
screen.exitonclick()
