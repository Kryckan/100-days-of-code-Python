import os
from codecs import ignore_errors

import art

type: ignore_errors


print(art.logo)
print("Welcome to the secret auction program! \n")

bidders = {}


def new_bidder():
    while True:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        bidders[name] = bid
        more_bidders = input("Are there any more bidders? Type 'yes' or 'no'. ")
        os.system("cls")
        if more_bidders == "no":
            break
    reveal()


def reveal():
    max_bidder = max(bidders, key=bidders.get)

    os.system("cls")
    print(
        f"Max bid was placed by {max_bidder} with an amount of ${bidders[max_bidder]}"
    )


new_bidder()
