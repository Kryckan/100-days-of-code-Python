# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

import random

flip = random.randint(0, 1)

if flip == 1:
    print("Heads")
else:
    print("Tails")
