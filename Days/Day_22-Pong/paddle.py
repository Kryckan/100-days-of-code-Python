from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_lr):
        super().__init__()
        self.speed("fastest")
        self.pu()
        self.goto(paddle_lr)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        if not self.ycor() >= 240:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.ycor() <= -240:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
