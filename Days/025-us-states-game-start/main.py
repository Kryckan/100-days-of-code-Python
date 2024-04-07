import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Days/025-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.speed(0)  # Set the main turtle's speed to the fastest
exit = False

correct_guesses: set[str] = set()
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 270)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

answers: pd.DataFrame = pd.read_csv("Days/025-us-states-game-start/50_states.csv")


def update_score_display():
    score_display.clear()
    score_display.write(
        f"Score: {len(correct_guesses)}", align="center", font=("Courier", 24, "normal")
    )


def new_turtle(x: int, y: int, state: str):
    state_turtle = turtle.Turtle()
    state_turtle.speed(0)  # Set drawing speed to the fastest
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(int(x), int(y))
    state_turtle.write(state, align="center")
    screen.update()  # Force screen update after drawing


def process_state_guess() -> bool:
    global exit
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    )
    answer_titled: str = answer_state.title() if answer_state else ""
    if (
        answer_titled in answers["state"].values
        and answer_titled not in correct_guesses
    ):
        correct_guesses.add(answer_titled)
        update_score_display()
        return True
    if answer_titled == "Exit":
        exit = True
    return False


while True:
    if exit:
        break
    if process_state_guess():
        state_name = list(correct_guesses)[-1]
        state_data = answers[answers.state == state_name]
        x_cor, y_cor = state_data.x.iloc[0], state_data.y.iloc[0]
        new_turtle(x_cor, y_cor, state_name)
        screen.update()

turtle.mainloop()
