from turtle import Screen, Turtle

screen = Screen()
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.high_score = self.read_highscore()
        self.speed_count = 0
        self.level_speed = 0.2
        self.level = 1
        self.ht()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.read_highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.clear()
        self.score_count += 1
        self.speed_count += 1
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.read_highscore()}",
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
            self.update_highscore()
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

        self.score_count = 0
        self.level = 1
        self.level_speed = 0.2
        self.speed_count = 0

    def read_highscore(self):
        try:
            with open("data.txt", mode="r") as file:
                contents = file.read()
                return int(contents)
        except FileNotFoundError:
            with open("data.txt", mode="w") as file:
                file.write("0")
            return 0

    def update_highscore(self):
        if self.score_count > self.high_score:
            new_high_score = self.score_count
            with open("data.txt", mode="w") as file:
                file.write(str(new_high_score))
