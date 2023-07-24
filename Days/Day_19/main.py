from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.speed("normal")


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)


screen.exitonclick()
