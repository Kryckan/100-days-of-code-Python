import time
from turtle import Screen

from food import Food
from score import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()

game_is_on: bool = True
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.heading_up)
screen.onkeypress(key="Left", fun=snake.heading_left)
screen.onkeypress(key="Down", fun=snake.heading_down)
screen.onkeypress(key="Right", fun=snake.heading_right)


while game_is_on:
    screen.update()
    time.sleep(score.level_speed)
    snake.add_segment()

    if snake.head.distance(food) < 15:
        food.spawn_food()
        for seg in snake.segments:
            if seg.distance(food) < 15:
                food.spawn_food()
        score.increase_score()
        snake.add_segment_part = True
    snake.move()

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        score.reset()
        screen.update()
        snake.reset()

    for seg in snake.segments[2:]:
        if snake.head.distance(seg) < 1:
            score.reset()
            screen.update()
            snake.reset()


screen.exitonclick()
screen.mainloop()
