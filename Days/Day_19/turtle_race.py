import random
from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=500, height=400)
start_race = False

user_guess = screen.textinput(
    title="Male your bet", prompt="What color turtle will win? Enter a color: "
)

colors: list = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles: list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + (turtle_index * 30))
    all_turtles.append(new_turtle)


if user_guess:
    start_race: bool = True

while start_race:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color: str = turtle.pencolor()
            if winning_color == user_guess:
                print(
                    f"You've won! The {winning_color} \
                    turtle is the winner!"
                )
            else:
                print(
                    f"You've lost! The {winning_color} \
                    turtle is the winner!"
                )
            start_race: bool = False


screen.exitonclick()
