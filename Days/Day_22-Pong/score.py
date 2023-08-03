from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cascadia Code", 48, "normal")


class Score(Turtle):
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
