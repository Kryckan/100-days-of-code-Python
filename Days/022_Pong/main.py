"""A simple Pong game created using Python's turtle module."""

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score

SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.setup(width=800, height=600)
SCREEN.title("Pong")

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
score = Score()


def new_game():
    """
    Resets the game by moving the ball to the center and setting its direction
    based on the last point winner.
    """
    ball.goto(0, 0)

    if score.last_point == 1:
        ball.setheading(ball.start_p1())
    elif score.last_point == 2:
        ball.setheading(ball.start_p2())
    game()
    score.last_point = 0


SCREEN.listen()
SCREEN.onkey(key="Up", fun=player_1.go_up)
SCREEN.onkey(key="Down", fun=player_1.go_down)
SCREEN.onkey(key="a", fun=player_2.go_up)
SCREEN.onkey(key="z", fun=player_2.go_down)
SCREEN.onkey(key="space", fun=new_game)


def game():
    """
    Starts and controls the main game loop.
    """
    game_is_on = True
    score.update_score(None)
    while game_is_on:
        time.sleep(ball.move_speed)
        SCREEN.update()
        ball.move()
        ball.wall_bounce()

        if ball.xcor() > 330 and ball.distance(player_1) < 50:
            ball.p1_bounce()
        elif ball.xcor() < -330 and ball.distance(player_2) < 50:
            ball.p2_bounce()
        elif ball.xcor() > 390:
            score.clear()
            score.update_score("p2")
            SCREEN.update()
            ball.move_speed = 0.01
            game_is_on = False
        elif ball.xcor() < -390:
            score.clear()
            score.update_score("p1")
            SCREEN.update()
            ball.move_speed = 0.01
            game_is_on = False


game()
SCREEN.exitonclick()
