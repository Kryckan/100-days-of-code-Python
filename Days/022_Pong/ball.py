"""
This module defines the Ball class for a Pong game,
including its movement, interactions with walls
and paddles, and starting positions.
"""

import random
from turtle import Turtle

START_HEADINGS_P1 = [-135.0, 135.0]
START_HEADINGS_P2 = [-45.0, 45.0]


class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.

    Attributes:
        move_speed (float): The speed at which the ball moves.
    Methods:
        move(): Moves the ball forward by 10 units.
        wall_bounce(): Changes the ball's direction
        when it hits the top or bottom wall.
        p1_bounce(): Changes the ball's direction and speed
        when it bounces off player 1's paddle.
        p2_bounce(): Changes the ball's direction and speed
        when it bounces off player 2's paddle.
        start_p1(): Selects a random starting direction
        for the ball towards player 1.
    """

    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 0)
        self.shape("circle")
        self.setheading(45)
        self.move_speed = 0.01

    def move(self):
        """
        Moves the ball forward by 10 units.
        """
        self.forward(10)

    def wall_bounce(self):
        """
        Changes the ball's direction when it hits
        the top or bottom wall.
        """
        if self.ycor() >= 280:
            self.setheading(self.heading() * -1)
        elif self.ycor() <= -280:
            self.setheading(360 - self.heading())

    def p1_bounce(self):
        """
        Changes the ball's direction and speed when
        it bounces off player 1's paddle.
        """
        if self.heading() < 90:
            self.setheading(180 - self.heading())
        else:
            self.setheading((360 - self.heading()) + 180)
        self.move_speed *= 0.9

    def p2_bounce(self):
        """
        Changes the ball's direction and speed when
        it bounces off player 2's paddle.
        """
        if self.heading() < 180:
            self.setheading(180 - self.heading())
        else:
            self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def start_p1(self):
        """
        Select a random starting direction for the
        ball towards player 1.
        """
        return random.choice(START_HEADINGS_P1)

    def start_p2(self):
        """
        Select a random starting direction for the
        ball towards player 2.
        """
        return random.choice(START_HEADINGS_P2)
