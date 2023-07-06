import os
import random

import art
from game_data import data as game_items

player_choice = int(-1)
compares = []
round_counter = 0
continue_game = True
correct_answer = True


def random_item():
    return random.choice(game_items)


def clear_console():
    os.system("cls")


def greet():
    print(art.logo)
    print(
        "Welcome to a game of Higher or Lower \n"
        "This is a game where you guess which of the two has the most followers on Instagram."
    )
    placeholder = input("Press Enter to get started!")


def check_answer():
    global correct_answer
    if player_choice == 0:
        if compares[0]["follower_count"] > compares[1]["follower_count"]:
            print("\nGood job! You were right!")
            print(
                f'{compares[0]["name"]} has '
                f'{compares[0]["follower_count"]} million followers, compared to '
                f'{compares[1]["name"]} with '
                f'{compares[1]["follower_count"]} million followers'
            )
            correct_answer = True
        else:
            print("\nTo bad. You lost ")
            print(
                f'{compares[0]["name"]} has '
                f'{compares[0]["follower_count"]} million followers, compared to '
                f'{compares[1]["name"]} with '
                f'{compares[1]["follower_count"]} million followers'
            )
            correct_answer = False


def check_duplicate():
    if compares[0] == compares[1]:
        compares.pop(1)
        compares.append(random_item())


def game():
    global correct_answer
    global compares
    global round_counter
    global continue_game
    continue_game = True
    compares.clear()
    compares.append(random_item())
    compares.append(random_item())
    greet()

    while continue_game:
        global player_choice
        check_duplicate()
        print(f"Round {round_counter}")
        print(f'\n{compares[0]["name"]}')
        print(f'{compares[0]["description"]} from {compares[0]["country"]}')
        print(art.vs)
        print(f'{compares[1]["name"]}')
        print(f'{compares[1]["description"]} from {compares[1]["country"]}')
        player_choice = (
            int(
                input(
                    f'Which has the most followers? 1 for {compares[0]["name"]} or 2 for {compares[1]["name"]}: '
                )
            )
            - 1
        )
        round_counter += 1
        check_answer()
        if correct_answer is not True:
            continue_game = False
            if input("Do you want to play again? y/n") == "y":
                game()
            else:
                quit()
        else:
            if player_choice == 0:
                compares.pop(1)
            else:
                compares.pop(0)
            compares.append(random_item())
            continue_game = True


game()
