import os
from turtle import Screen, Turtle

screen = Screen()
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_count: int = 0
        self.high_score: int = self.read_highscore()
        self.speed_count: int = 0
        self.level_speed = 0.2
        self.level = 1
        self.ht()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.read_highscore()}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self) -> None:
        self.clear()
        self.score_count += 1
        self.speed_count += 1
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.read_highscore()}",
            align=ALIGNMENT,
            font=FONT,
        )
        self.speed_increase()

    def speed_increase(self) -> None:
        if self.speed_count == 4:
            self.level += 1
            self.level_speed -= 0.01
            self.speed_count = 0

    def reset(self) -> None:
        self.clear()
        if self.score_count > self.high_score:
            self.update_highscore()

        self.score_count = 0
        self.level = 1
        self.level_speed = 0.2
        self.speed_count = 0
        self.write(
            f"Score: {self.score_count} Level: {self.level}, High Score: {self.read_highscore()}",
            align=ALIGNMENT,
            font=FONT,
        )

    def read_highscore(self) -> int:
        # Path relative to the current script
        directory = os.path.dirname(__file__)
        file_path = os.path.join(directory, "data.txt")

        try:
            with open(file_path, mode="r") as file:
                contents = file.read()
                return int(contents)
        except FileNotFoundError:
            with open(file_path, mode="w") as file:
                file.write("0")
            return 0

    def update_highscore(self) -> None:
        # Path relative to the current script
        directory = os.path.dirname(__file__)
        file_path = os.path.join(directory, "data.txt")

        if self.score_count > self.high_score:
            new_high_score = self.score_count
            with open(file_path, mode="w") as file:
                file.write(str(new_high_score))
