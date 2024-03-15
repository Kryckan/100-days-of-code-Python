import os
import random

tries = int(0)
the_number = int(0)
guessed_number = int(0)


def clear_console():
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def greet():
    clear_console()
    global tries
    print("Welcome to the number guessing game!")
    print("You have to guess the correct number which is between 1 - 100.")
    if input("Choose level. Easy or Hard e / h ") == "e":
        tries = 10
    else:
        tries = 5


def set_random_number():
    global the_number
    the_number = random.randint(1, 101)


def guess():
    global guessed_number
    print(f"You have {tries} left. ")
    if guessed_number != 0:
        print(f"The last guessed number was {guessed_number} ")
    guessed_number = int(input("Guess a number between 1 - 100 "))
    clear_console()


def game():
    greet()
    set_random_number()
    global tries

    while tries > 0:
        guess()
        if guessed_number == the_number:
            print("Congratulations! You found the right number! ")
            print(f"The secret number was {the_number}")
            break
        elif guessed_number > the_number:
            print("Sorry, the number is lower.")
            tries -= 1
        elif guessed_number < the_number:
            print("Sorry, the number is higher.")
            tries -= 1


game()
