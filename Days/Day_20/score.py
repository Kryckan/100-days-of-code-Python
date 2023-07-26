from turtle import Screen, Turtle

screen = Screen()


class Score:
    def __init__(self):
        self.score_count = 0
        self.score = Turtle()
        self.score.ht()
        self.score.pu()
        self.score.goto(0, 280)
        self.score.color("white")

    def show_score(self):
        self.score.clear()
        self.score.write(
            f"Score: {self.score_count}", align="center", font=("Arial", 14, "normal")
        )
