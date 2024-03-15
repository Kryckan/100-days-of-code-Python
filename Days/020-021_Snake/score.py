from turtle import Screen, Turtle

screen = Screen()
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.high_score = 0
        self.speed_count = 0
        self.level_speed = 0.2
        self.level = 1
        self.ht()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.speed_count += 1
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.speed_increase()

    def speed_increase(self):
        if self.speed_count == 4:
            self.level += 1
            self.level_speed -= 0.01
            self.speed_count = 0

    def reset(self):
        self.clear()
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            self.write(
                f"Score: {self.score_count} Level: {self.level}, High Score: {self.high_score}",
                align=ALIGNMENT,
                font=FONT,
            )
        self.score_count = 0
        self.level = 1
        self.level_speed = 0.2
        self.speed_count = 0
