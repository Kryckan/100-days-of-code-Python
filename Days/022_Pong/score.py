"""
Module for managing the score display in a Pong game.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 48, "normal")


class Score(Turtle):
    """
    A class to represent the score in a Pong game.
    """

    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.last_point = 0
        self.ht()
        self.pu()
        self.goto(0, 220)
        self.color("white")

    def update_score(self, point):
        """
        Updates the score based on the player who scored the point.

        Args:
            point (str): The player who scored the point. "p1" for
        """
        if point == "p1":
            self.score_player1 += 1
            self.last_point = 1
        elif point == "p2":
            self.score_player2 += 1
            self.last_point = 2
        self.write(
            f"{self.score_player2}   {self.score_player1}",
            align=ALIGNMENT,
            font=FONT,
        )
