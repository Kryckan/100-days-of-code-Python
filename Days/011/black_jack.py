import os
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []


def thank_you():
    quit()


def welcome():
    os.system("cls")
    print(logo)

    print("Welcome to a game of Black Jack! \n")
    print(
        "The goal of this game is to get as close to 21 as possible without going over.\n"
    )


def start_hand():
    list.clear(dealer_hand)
    list.clear(player_hand)
    for i in range(0, 2):
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))


def player_hand_show():
    print("You have the cards: ")
    print(player_hand)
    print(f"With a total of: {sum(player_hand)}")


def dealer_hand_show():
    print("The dealer has the cards: ")
    print(dealer_hand)
    print(f"With a total of: {sum(dealer_hand)}")


def check_won():
    if sum(dealer_hand) < 22 and sum(dealer_hand) >= sum(player_hand):
        print(f"Sorry. Dealer won with {sum(dealer_hand)} to your {sum(player_hand)}")
        if input("Do you want to play again? y/n: ") == "y":
            game()
        else:
            thank_you()
    elif sum(dealer_hand) > 21:
        print(f"Congratulations! The dealer got bust and you won!")
        if input("Do you want to play again? y/n: ") == "y":
            game()
        else:
            thank_you()
    else:
        print(
            f"Congratulations! You won with the hand {sum(player_hand)} over the dealers {sum(dealer_hand)}"
        )
        if input("Do you want to play again? y/n: ") == "y":
            game()
        else:
            thank_you()


def game():
    welcome()
    hit = True
    start_hand()
    print(f"Dealers hand: {dealer_hand[0]} & * ")

    while hit:
        if sum(player_hand) < 22:
            player_hand_show()
            if input("Do you want one more card? y/n: ") != "y":
                hit = False
            else:
                player_hand.append(random.choice(cards))
        else:
            player_hand_show()
            print(f"Sorry! You busted with a total of {sum(player_hand)}")
            hit = False
            if input("Do you want to play again? y/n: ") == "y":
                game()
            else:
                thank_you()

    dealer_hand_show()

    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
        dealer_hand_show()
    check_won()


game()
