"""
This module defines the Paddle class for a Pong game, which
inherits from the Turtle class.
It includes methods to initialize the paddle, move it up,
and move it down.
"""

from turtle import Turtle


class Paddle(Turtle):
    """
    Class representing a paddle for the pong game.
    """

    def __init__(self, paddle_lr):
        """
        Initialize the paddle with the given side.
        """

        super().__init__()
        self.speed("fastest")
        self.pu()
        self.goto(paddle_lr)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        """
        Move the paddle up by 40 units if it's not above
        a certain threshold.
        """
        if not self.ycor() >= 240:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down by 40 units if it's not below
        a certain threshold.
        """
        if not self.ycor() <= -240:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)
