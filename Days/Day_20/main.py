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
speed = 0.2

game_is_on: bool = True
level: int = 1
food_counter = 0
score = Score()
score_count: int = 0

screen.listen()
screen.onkeypress(key="Up", fun=snake.heading_up)
screen.onkeypress(key="Left", fun=snake.heading_left)
screen.onkeypress(key="Down", fun=snake.heading_down)
screen.onkeypress(key="Right", fun=snake.heading_right)


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


while game_is_on:
    screen.update()
    score.show_score()
    time.sleep(speed)
    snake.add_segment()

    food.check_food()
    if distance(snake.snake_head_pos(), food.food_pos()) < 15:
        food.take_food()
        food_counter += 1
        score.score_count += 1
        snake.add_segment_part = True
        if food_counter >= 5:
            speed -= 0.01
            food_counter = 0
    snake.move()

screen.exitonclick()
screen.mainloop()
