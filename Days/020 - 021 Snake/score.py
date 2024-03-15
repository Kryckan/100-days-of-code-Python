from turtle import Screen, Turtle

screen = Screen()
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.speed_count = 0
        self.level_speed = 0.2
        self.level = 1
        self.ht()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.write(
            f"Score: {self.score_count} Level: {self.level}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.speed_count += 1
        self.write(
            f"Score: {self.score_count} Level: {self.level}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.speed_increase()

    def speed_increase(self):
        if self.speed_count == 4:
            self.level += 1
            self.level_speed -= 0.01
            self.speed_count = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!",
            align=ALIGNMENT,
            font=("Courier", 24, "normal"),
        )
