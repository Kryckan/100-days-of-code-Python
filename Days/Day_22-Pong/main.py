import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(key="Up", fun=player_1.go_up)
screen.onkey(key="Down", fun=player_1.go_down)
screen.onkey(key="a", fun=player_2.go_up)
screen.onkey(key="z", fun=player_2.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    ball.wall_bounce()

    if ball.xcor() > 330 and ball.distance(player_1) < 50:
        ball.p1_bounce()
    elif ball.xcor() < -330 and ball.distance(player_2) < 50:
        ball.p2_bounce()
    elif ball.xcor() > 390 or ball.xcor() < -390:
        game_is_on = False


screen.exitonclick()
