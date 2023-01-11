import random
import time

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

RPS = [ROCK, PAPER, SCISSORS]
pc_rps = random.choice(RPS)

print("Welcome to a game of Rock, Paper, Scissors! \n")
choice = (
    int(input("What do you chose? 1 for Rock, 2 for Paper, and 3 for Scissors ")) - 1
)
print(RPS[choice])
print("Rock!")
time.sleep(0.5)
print("Paper!")
time.sleep(0.5)
print("Scissors!")
time.sleep(0.5)
print("Lizzard!")
time.sleep(0.5)
print("Spock!")
time.sleep(0.5)
print(pc_rps)

if choice == 0:
    if pc_rps == ROCK:
        print("It's a draw!")
    elif pc_rps == PAPER:
        print("You lose!")
    else:
        print("You win!!!")

if choice == 1:
    if pc_rps == ROCK:
        print("You Win!!!")
    elif pc_rps == PAPER:
        print("It's a draw")
    else:
        print("You lose!")

if choice == 2:
    if pc_rps == ROCK:
        print("You lose!")
    elif pc_rps == PAPER:
        print("You Win!!!")
    else:
        print("It's a draw!")
print("\n")
