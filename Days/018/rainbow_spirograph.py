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


def create_rainbow_colors(num_colors):
    """A function that returns a list of rainbow colors.
    The number of colors is specified by the input parameter.

    Args:
        num_colors (INT): The number of colors to be returned.

    Returns:
        list: A list of colors in RGB format.
    """
    colors = []
    step = 360 / num_colors
    for i in range(num_colors):
        hue = i * step
        rgb = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
        colors.append((int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)))
    return colors


def draw(circles, radius):
    colors = create_rainbow_colors(circles)
    current_angle = 0
    angle = 360 / circles
    for i in range(circles):
        tim.setheading(current_angle)
        tim.pencolor(colors[i])
        tim.circle(radius)
        current_angle += angle


draw(100, 170)  # input number of circles and radius to draw
screen.exitonclick()
