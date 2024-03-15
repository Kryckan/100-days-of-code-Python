import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")


display = []
word_lenght = len(chosen_word)
for letter in range(word_lenght):
    display.append("_")
print(display)

while not "".join(display) == chosen_word:
    guess = input("Guess a letter: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    print(display)

print("You won! The word is " + "".join(display))
